import numpy as np
import pandas as pd
import h5py
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_curve, RocCurveDisplay, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

walkingDataN = pd.read_csv('Niels_Walking.csv')
jumpingDataN = pd.read_csv('Niels_Jumping.csv')
walkingDataV = pd.read_csv('Vicky_Walking.csv')
jumpingDataV = pd.read_csv('Vicky_Jumping.csv')
walkingDataC = pd.read_csv('ConnorWalking.csv')
jumpingDataC = pd.read_csv('ConnorJumping.csv')

# setting the last column of the data to 0 or 1 whether it is walking or jumping. To be used for labels
walkingDataN.loc[:, 'Absolute acceleration (m/s^2)'] = 0
jumpingDataN.loc[:, 'Absolute acceleration (m/s^2)'] = 1
walkingDataC.loc[:, 'Absolute acceleration (m/s^2)'] = 0
jumpingDataC.loc[:, 'Absolute acceleration (m/s^2)'] = 1
walkingDataV.loc[:, 'Absolute acceleration (m/s^2)'] = 0
jumpingDataV.loc[:, 'Absolute acceleration (m/s^2)'] = 1

walkingDataN = walkingDataN.iloc[:15090, :]
jumpingDataN = jumpingDataN.iloc[:15090, :]
walkingDataV = walkingDataV.iloc[:15090, :]
jumpingDataV = jumpingDataV.iloc[:15090, :]
walkingDataC = walkingDataC.iloc[:15090, :]
jumpingDataC = jumpingDataC.iloc[:15090, :]

# segments data into 5 second segments, storing them in an array
def segment_data(data):
    segments = []
    i = 0
    while i < len(data):
        k = i + 1
        while k < len(data)-1 and (data.loc[k].at['Time (s)'] - data.loc[i].at['Time (s)'] < 5) and (data.loc[k].at['Time (s)'] - data.loc[i].at['Time (s)'] >= 0):
            k += 1
        segment = data.iloc[i:k]
        segments.append(segment)
        i = k
    return segments

# segment all the data
walkSegmentsN = segment_data(walkingDataN)
jumpSegmentsN = segment_data(jumpingDataN)
walkSegmentsV = segment_data(walkingDataV)
jumpSegmentsV = segment_data(jumpingDataV)
walkSegmentsC = segment_data(walkingDataC)
jumpSegmentsC = segment_data(jumpingDataC)

# add all the 5 second segmented data together
shuffled_segments = walkSegmentsN+jumpSegmentsN + walkSegmentsV+jumpSegmentsV + walkSegmentsC+jumpSegmentsC
# shuffles the segments randomly
np.random.shuffle(shuffled_segments)
# concatenate the shuffled segments back together to make a dataframe
combined_data = pd.concat(shuffled_segments)
combined_data.reset_index(drop=True, inplace=True)

# extract the labels column
labels = combined_data.iloc[:, -1]

# split data into 90% training, 10% testing
X_train, X_test, Y_train, Y_test = \
    train_test_split(combined_data, labels, test_size=0.1, shuffle=False, random_state=0)

# resets the indices back to starting at 0
X_test.reset_index(drop=True, inplace=True)
Y_test.reset_index(drop=True, inplace=True)

# write data in HDF5 file
with h5py.File('./hdf5_data.h5', 'w') as hdf:
    G1 = hdf.create_group('/NielsMorizur')
    G1.create_dataset('walkData', data=walkingDataN)
    G1.create_dataset('jumpData', data=jumpingDataN)

    G2 = hdf.create_group('/ConnorGorman')
    G2.create_dataset('walkData', data=walkingDataC)
    G2.create_dataset('jumpData', data=jumpingDataC)

    G3 = hdf.create_group('/VickyWu')
    G3.create_dataset('walkData', data=walkingDataV)
    G3.create_dataset('jumpData', data=jumpingDataV)

    G4 = hdf.create_group('dataset')
    G4.create_dataset('Train', data=X_train)
    G4.create_dataset('Test', data=X_test)

# extracts 10 different features for each of the axes
# returns a dictionary containing the extracted features and their values
def extract_features(segment):
    features_dict = {}
    features_dict['minX'] = segment['Acceleration x (m/s^2)'].min()
    features_dict['minY'] = segment['Acceleration y (m/s^2)'].min()
    features_dict['minZ'] = segment['Acceleration z (m/s^2)'].min()

    features_dict['maxX'] = segment['Acceleration x (m/s^2)'].max()
    features_dict['maxY'] = segment['Acceleration y (m/s^2)'].max()
    features_dict['maxZ'] = segment['Acceleration z (m/s^2)'].max()

    features_dict['rangeX'] = features_dict['maxX'] - features_dict['minX']
    features_dict['rangeY'] = features_dict['maxY'] - features_dict['minY']
    features_dict['rangeZ'] = features_dict['maxZ'] - features_dict['minZ']

    features_dict['meanX'] = segment['Acceleration x (m/s^2)'].mean()
    features_dict['meanY'] = segment['Acceleration y (m/s^2)'].mean()
    features_dict['meanZ'] = segment['Acceleration z (m/s^2)'].mean()

    features_dict['medianX'] = segment['Acceleration x (m/s^2)'].median()
    features_dict['medianY'] = segment['Acceleration y (m/s^2)'].median()
    features_dict['medianZ'] = segment['Acceleration z (m/s^2)'].median()

    features_dict['stdX'] = segment['Acceleration x (m/s^2)'].std()
    features_dict['stdY'] = segment['Acceleration y (m/s^2)'].std()
    features_dict['stdZ'] = segment['Acceleration z (m/s^2)'].std()

    features_dict['varianceX'] = segment['Acceleration x (m/s^2)'].var()
    features_dict['varianceY'] = segment['Acceleration y (m/s^2)'].var()
    features_dict['varianceZ'] = segment['Acceleration z (m/s^2)'].var()

    features_dict['skewnessX'] = segment['Acceleration x (m/s^2)'].skew()
    features_dict['skewnessY'] = segment['Acceleration y (m/s^2)'].skew()
    features_dict['skewnessZ'] = segment['Acceleration z (m/s^2)'].skew()

    features_dict['kurtX'] = segment['Acceleration x (m/s^2)'].kurtosis()
    features_dict['kurtY'] = segment['Acceleration y (m/s^2)'].kurtosis()
    features_dict['kurtZ'] = segment['Acceleration z (m/s^2)'].kurtosis()

    features_dict['rmsX'] = np.sqrt(np.mean(segment['Acceleration x (m/s^2)'].values ** 2))
    features_dict['rmsY'] = np.sqrt(np.mean(segment['Acceleration y (m/s^2)'].values ** 2))
    features_dict['rmsZ'] = np.sqrt(np.mean(segment['Acceleration z (m/s^2)'].values ** 2))

    return features_dict

# checks if this segment is walking or jumping
def extract_labels(data):
    return data.iloc[0, -1]

# iterates through each segment in X_train and extracts the features
def extracting(data):
    segment_features = []
    segmented = segment_data(data)
    for segment in segmented:
        segment_features.append(extract_features(segment))
    return segment_features

# make a list of labels the same length as data for pipeline. A 0 for walking segment, 1 for jumping segment
def make_labels(data):
    feature_labels = []
    segmented = segment_data(data)
    for segment in segmented:
        feature_labels.append(extract_labels(segment))
    return feature_labels

features_df_train = pd.DataFrame(extracting(X_train))
feature_labels_train = make_labels(X_train)

print(features_df_train)

# fills potential NaNs
imputer = SimpleImputer(strategy='mean')
features_df_imputed_train = imputer.fit_transform(features_df_train)

# use z-score standardization to normalize the features of the segments
scaler = preprocessing.StandardScaler()
features_df_scaled_train = scaler.fit_transform(features_df_imputed_train)

l_reg = LogisticRegression(max_iter=10000)
clf = make_pipeline(l_reg)

clf.fit(features_df_scaled_train, feature_labels_train)

# use the classifier on the Test data
features_df_test = pd.DataFrame(extracting(X_test))
features_df_imputed_test = imputer.fit_transform(features_df_test)
features_df_scaled_test = scaler.fit_transform(features_df_imputed_test)
feature_labels_test = make_labels(X_test)

# classify the normalized test data features using the trained pipeline model
y_pred = clf.predict(features_df_scaled_test)
y_clf_prob = clf.predict_proba(features_df_scaled_test)

# calculate the accuracy score
acc = accuracy_score(feature_labels_test, y_pred)
print('accuracy is: ', acc)

# plot the ROC curve
fpr, tpr, _ = roc_curve(feature_labels_test, y_clf_prob[:, 1], pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
plt.show()

# calculate the AUC score
auc = roc_auc_score(feature_labels_test, y_clf_prob[:, 1])
print('the AUC is: ', auc)
