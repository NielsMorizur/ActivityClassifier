import numpy as np
import pandas as pd
import h5py
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

walkingDataN = pd.read_csv('Niels_Walking.csv')
jumpingDataN = pd.read_csv('Niels_Jumping.csv')
walkingDataV = pd.read_csv('Vicky_Walking.csv')
jumpingDataV = pd.read_csv('Vicky_Jumping.csv')
walkingDataC = pd.read_csv('ConnorWalking.csv')
jumpingDataC = pd.read_csv('ConnorJumping.csv')

testingData = pd.read_csv('TestingData.csv')

# Setting the last column of the data to 0 or 1 whether it is walking or jumping. To be used for labels
# Don't need Absolute acceleration so decided to use it as the labels column instead of creating a new one
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


# Segments data into 5 second segments, storing them in an array
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

# Segment all the data
walkSegmentsN = segment_data(walkingDataN)
jumpSegmentsN = segment_data(jumpingDataN)
walkSegmentsV = segment_data(walkingDataV)
jumpSegmentsV = segment_data(jumpingDataV)
walkSegmentsC = segment_data(walkingDataC)
jumpSegmentsC = segment_data(jumpingDataC)

# Add all the 5 second segmented data together
shuffled_segments = walkSegmentsN+jumpSegmentsN + walkSegmentsV+jumpSegmentsV + walkSegmentsC+jumpSegmentsC
# Shuffle the segments randomly
np.random.shuffle(shuffled_segments)
# Concatenate the shuffled segments back together to make a dataframe
combined_data = pd.concat(shuffled_segments)
combined_data.reset_index(drop=True, inplace=True)

labels = combined_data.iloc[:, -1]

# Split data into 90% training, 10% testing
X_train, X_test, Y_train, Y_test = \
    train_test_split(combined_data, labels, test_size=0.1, shuffle=False, random_state=0)

# Resets the indices back to starting at 0
X_test.reset_index(drop=True, inplace=True)
Y_test.reset_index(drop=True, inplace=True)

# Write data in HDF5 file
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
#Z accel extraction
plt.figure(figsize=(10, 6))


plt.plot(walkingDataC.index, walkingDataC['Acceleration z (m/s^2)'].max() * np.ones_like(walkingDataC.index), marker='o', linestyle='-', color='green', label='Max Z Acc - Walking')
plt.plot(walkingDataC.index, walkingDataC['Acceleration z (m/s^2)'].min() * np.ones_like(walkingDataC.index), marker='o', linestyle='-', color='blue', label='Min Z Acc - Walking')


plt.plot(jumpingDataC.index, jumpingDataC['Acceleration z (m/s^2)'].max() * np.ones_like(jumpingDataC.index), marker='o', linestyle='-', color='orange', label='Max Z Acc - Jumping')
plt.plot(jumpingDataC.index, jumpingDataC['Acceleration z (m/s^2)'].min() * np.ones_like(jumpingDataC.index), marker='o', linestyle='-', color='red', label='Min Z Acc - Jumping')

plt.xlabel('Time')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Max and Min Z Acceleration for Walking and Jumping Data')
plt.legend()
plt.grid(True)
plt.show()
#Feature extraction, x and y variance
plt.figure(figsize=(10, 6))

walking_var_x = walkingDataC['Acceleration x (m/s^2)'].var()
walking_var_y = walkingDataC['Acceleration y (m/s^2)'].var()
jumping_var_x = jumpingDataC['Acceleration x (m/s^2)'].var()
jumping_var_y = jumpingDataC['Acceleration y (m/s^2)'].var()

plt.plot(walkingDataC.index, walking_var_x * np.ones_like(walkingDataC.index), marker='o', linestyle='-', color='green', label='Variance X Acc - Walking')

plt.plot(walkingDataC.index, walking_var_y * np.ones_like(walkingDataC.index), marker='o', linestyle='-', color='blue', label='Variance Y Acc - Walking')

plt.plot(jumpingDataC.index, jumping_var_x * np.ones_like(jumpingDataC.index), marker='o', linestyle='-', color='orange', label='Variance X Acc - Jumping')

plt.plot(jumpingDataC.index, jumping_var_y * np.ones_like(jumpingDataC.index), marker='o', linestyle='-', color='red', label='Variance Y Acc - Jumping')

plt.xlabel('Time')
plt.ylabel('Variance of Acceleration (m/s^2)')
plt.title('Variance of X and Y Acceleration for Walking and Jumping Data')
plt.legend()
plt.grid(True)
plt.show()

