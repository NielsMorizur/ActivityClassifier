import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use("TkAgg")

walkingDataN = pd.read_csv('Niels_Walking.csv')
jumpingDataN = pd.read_csv('Niels_Jumping.csv')
walkingDataV = pd.read_csv('Vicky_Walking.csv')
jumpingDataV = pd.read_csv('Vicky_Jumping.csv')
walkingDataC = pd.read_csv('ConnorWalking.csv')
jumpingDataC = pd.read_csv('ConnorJumping.csv')

walkingDataN = walkingDataN.iloc[:15090, :-1]
jumpingDataN = jumpingDataN.iloc[:15090, :-1]
walkingDataV = walkingDataV.iloc[:15090, :-1]
jumpingDataV = jumpingDataV.iloc[:15090, :-1]
walkingDataC = walkingDataC.iloc[:15090, :-1]
jumpingDataC = jumpingDataC.iloc[:15090, :-1]

window_sizes = [20, 50, 500]

# Filtered Data
filterWalkC_20 = walkingDataC.rolling(window=window_sizes[0]).mean()
filterWalkC_50 = walkingDataC.rolling(window=window_sizes[1]).mean()
filterWalkC_500 = walkingDataC.rolling(window=window_sizes[2]).mean()

filterJumpC_20 = jumpingDataC.rolling(window=window_sizes[0]).mean()
filterJumpC_50 = jumpingDataC.rolling(window=window_sizes[1]).mean()
filterJumpC_500 = jumpingDataC.rolling(window=window_sizes[2]).mean()

filterWalkN_20 = walkingDataN.rolling(window=window_sizes[0]).mean()
filterWalkN_50 = walkingDataN.rolling(window=window_sizes[1]).mean()
filterWalkN_500 = walkingDataN.rolling(window=window_sizes[2]).mean()

filterJumpN_20 = jumpingDataN.rolling(window=window_sizes[0]).mean()
filterJumpN_50 = jumpingDataN.rolling(window=window_sizes[1]).mean()
filterJumpN_500 = jumpingDataN.rolling(window=window_sizes[2]).mean()

filterWalkV_20 = walkingDataV.rolling(window=window_sizes[0]).mean()
filterWalkV_50 = walkingDataV.rolling(window=window_sizes[1]).mean()
filterWalkV_500 = walkingDataV.rolling(window=window_sizes[2]).mean()

filterJumpV_20 = jumpingDataV.rolling(window=window_sizes[0]).mean()
filterJumpV_50 = jumpingDataV.rolling(window=window_sizes[1]).mean()
filterJumpV_500 = jumpingDataV.rolling(window=window_sizes[2]).mean()

# Original Unfiltered Data Plots
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x acceleration
axs[0].plot(walkingDataC['Acceleration x (m/s^2)'], label='X Acceleration', color='purple')
axs[0].set_title('X Walk C Acceleration (Unfiltered)')
axs[0].legend()

# Plot y acceleration
axs[1].plot(walkingDataC['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Walk C Acceleration (Unfiltered)')
axs[1].legend()

# Plot z acceleration
axs[2].plot(walkingDataC['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk C Acceleration (Unfiltered)')
axs[2].legend()

plt.tight_layout()
plt.show()

# Same for jumping data
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x acceleration
axs[0].plot(jumpingDataC['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump C Acceleration (Unfiltered)')
axs[0].legend()

# Plot y acceleration
axs[1].plot(jumpingDataC['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Jump C Acceleration (Unfiltered)')
axs[1].legend()

# Plot z acceleration
axs[2].plot(jumpingDataC['Acceleration z (m/s^2)'], label='Z Acceleration', color='blue')
axs[2].set_title('Z Jump C Acceleration (Unfiltered)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkC_20['Acceleration x (m/s^2)'], label='X Acceleration', color='purple')
axs[0].set_title('X Walk C Acceleration (Filtered 20)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkC_20['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Walk C Acceleration (Filtered 20)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkC_20['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk C Acceleration (Filtered 20)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkC_50['Acceleration x (m/s^2)'], label='X Acceleration', color='purple')
axs[0].set_title('X Walk C Acceleration (Filtered 50)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkC_50['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Walk C Acceleration (Filtered 50)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkC_50['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk C Acceleration (Filtered 50)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkC_500['Acceleration x (m/s^2)'], label='X Acceleration', color='purple')
axs[0].set_title('X Walk C Acceleration (Filtered 500)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkC_500['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Walk C Acceleration (Filtered 500)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkC_500['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk C Acceleration (Filtered 500)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpC_20['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump C Acceleration (Filtered 20)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpC_20['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Jump C Acceleration (Filtered 20)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpC_20['Acceleration z (m/s^2)'], label='Z Acceleration', color='blue')
axs[2].set_title('Z Jump C Acceleration (Filtered 20)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpC_50['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump C Acceleration (Filtered 50)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpC_50['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Jump C Acceleration (Filtered 50)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpC_50['Acceleration z (m/s^2)'], label='Z Acceleration', color='blue')
axs[2].set_title('Z Jump C Acceleration (Filtered 50)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpC_500['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump C Acceleration (Filtered 500)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpC_500['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Jump C Acceleration (Filtered 500)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpC_500['Acceleration z (m/s^2)'], label='Z Acceleration', color='blue')
axs[2].set_title('Z Jump C Acceleration (Filtered 500)')
axs[2].legend()

plt.tight_layout()
plt.show()

# Redoing all the steps above but for Niels' data
# Original Unfiltered Data Plots
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x acceleration
axs[0].plot(walkingDataN['Acceleration x (m/s^2)'], label='X Acceleration', color='blue')
axs[0].set_title('X Walk N Acceleration (Unfiltered)')
axs[0].legend()

# Plot y acceleration
axs[1].plot(walkingDataN['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Walk N Acceleration (Unfiltered)')
axs[1].legend()

# Plot z acceleration
axs[2].plot(walkingDataN['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk N Acceleration (Unfiltered)')
axs[2].legend()

plt.tight_layout()
plt.show()

# Same for jumping data
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x acceleration
axs[0].plot(jumpingDataN['Acceleration x (m/s^2)'], label='X Acceleration', color='orange')
axs[0].set_title('X Jump N Acceleration (Unfiltered)')
axs[0].legend()

# Plot y acceleration
axs[1].plot(jumpingDataN['Acceleration y (m/s^2)'], label='Y Acceleration', color='purple')
axs[1].set_title('Y Jump N Acceleration (Unfiltered)')
axs[1].legend()

# Plot z acceleration
axs[2].plot(jumpingDataN['Acceleration z (m/s^2)'], label='Z Acceleration', color='yellow')
axs[2].set_title('Z Jump N Acceleration (Unfiltered)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkN_20['Acceleration x (m/s^2)'], label='X Acceleration', color='blue')
axs[0].set_title('X Walk N Acceleration (Filtered 20)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkN_20['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Walk N Acceleration (Filtered 20)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkN_20['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk N Acceleration (Filtered 20)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkN_50['Acceleration x (m/s^2)'], label='X Acceleration', color='blue')
axs[0].set_title('X Walk N Acceleration (Filtered 50)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkN_50['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Walk N Acceleration (Filtered 50)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkN_50['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk N Acceleration (Filtered 50)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkN_500['Acceleration x (m/s^2)'], label='X Acceleration', color='blue')
axs[0].set_title('X Walk N Acceleration (Filtered 500)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkN_500['Acceleration y (m/s^2)'], label='Y Acceleration', color='red')
axs[1].set_title('Y Walk N Acceleration (Filtered 500)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkN_500['Acceleration z (m/s^2)'], label='Z Acceleration', color='green')
axs[2].set_title('Z Walk N Acceleration (Filtered 500)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpN_20['Acceleration x (m/s^2)'], label='X Acceleration', color='orange')
axs[0].set_title('X Jump N Acceleration (Filtered 20)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpN_20['Acceleration y (m/s^2)'], label='Y Acceleration', color='purple')
axs[1].set_title('Y Jump N Acceleration (Filtered 20)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpN_20['Acceleration z (m/s^2)'], label='Z Acceleration', color='yellow')
axs[2].set_title('Z Jump N Acceleration (Filtered 20)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpN_50['Acceleration x (m/s^2)'], label='X Acceleration', color='orange')
axs[0].set_title('X Jump N Acceleration (Filtered 50)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpN_50['Acceleration y (m/s^2)'], label='Y Acceleration', color='purple')
axs[1].set_title('Y Jump N Acceleration (Filtered 50)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpN_50['Acceleration z (m/s^2)'], label='Z Acceleration', color='yellow')
axs[2].set_title('Z Jump N Acceleration (Filtered 50)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpN_500['Acceleration x (m/s^2)'], label='X Acceleration', color='orange')
axs[0].set_title('X Jump N Acceleration (Filtered 500)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpN_500['Acceleration y (m/s^2)'], label='Y Acceleration', color='purple')
axs[1].set_title('Y Jump N Acceleration (Filtered 500)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpN_500['Acceleration z (m/s^2)'], label='Z Acceleration', color='yellow')
axs[2].set_title('Z Jump N Acceleration (Filtered 500)')
axs[2].legend()

plt.tight_layout()
plt.show()

# Redoing again with Vicky's data
# Original Unfiltered Data Plots
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x acceleration
axs[0].plot(walkingDataV['Acceleration x (m/s^2)'], label='X Acceleration', color='cyan')
axs[0].set_title('X Walk V Acceleration (Unfiltered)')
axs[0].legend()

# Plot y acceleration
axs[1].plot(walkingDataV['Acceleration y (m/s^2)'], label='Y Acceleration', color='magenta')
axs[1].set_title('Y Walk V Acceleration (Unfiltered)')
axs[1].legend()

# Plot z acceleration
axs[2].plot(walkingDataV['Acceleration z (m/s^2)'], label='Z Acceleration', color='lime')
axs[2].set_title('Z Walk V Acceleration (Unfiltered)')
axs[2].legend()

plt.tight_layout()
plt.show()

# Same for jumping data
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x acceleration
axs[0].plot(jumpingDataV['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump V Acceleration (Unfiltered)')
axs[0].legend()

# Plot y acceleration
axs[1].plot(jumpingDataV['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Jump V Acceleration (Unfiltered)')
axs[1].legend()

# Plot z acceleration
axs[2].plot(jumpingDataV['Acceleration z (m/s^2)'], label='Z Acceleration', color='brown')
axs[2].set_title('Z Jump V Acceleration (Unfiltered)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkV_20['Acceleration x (m/s^2)'], label='X Acceleration', color='cyan')
axs[0].set_title('X Walk V Acceleration (Filtered 20)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkV_20['Acceleration y (m/s^2)'], label='Y Acceleration', color='magenta')
axs[1].set_title('Y Walk V Acceleration (Filtered 20)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkV_20['Acceleration z (m/s^2)'], label='Z Acceleration', color='lime')
axs[2].set_title('Z Walk V Acceleration (Filtered 20)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkV_50['Acceleration x (m/s^2)'], label='X Acceleration', color='cyan')
axs[0].set_title('X Walk V Acceleration (Filtered 50)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkV_50['Acceleration y (m/s^2)'], label='Y Acceleration', color='magenta')
axs[1].set_title('Y Walk V Acceleration (Filtered 50)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkV_50['Acceleration z (m/s^2)'], label='Z Acceleration', color='lime')
axs[2].set_title('Z Walk V Acceleration (Filtered 50)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x filtered acceleration
axs[0].plot(filterWalkV_500['Acceleration x (m/s^2)'], label='X Acceleration', color='cyan')
axs[0].set_title('X Walk V Acceleration (Filtered 500)')
axs[0].legend()

# Plot y filtered acceleration
axs[1].plot(filterWalkV_500['Acceleration y (m/s^2)'], label='Y Acceleration', color='magenta')
axs[1].set_title('Y Walk V Acceleration (Filtered 500)')
axs[1].legend()

# Plot z filtered acceleration
axs[2].plot(filterWalkV_500['Acceleration z (m/s^2)'], label='Z Acceleration', color='lime')
axs[2].set_title('Z Walk V Acceleration (Filtered 500)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpV_20['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump V Acceleration (Filtered 20)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpV_20['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Jump V Acceleration (Filtered 20)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpV_20['Acceleration z (m/s^2)'], label='Z Acceleration', color='brown')
axs[2].set_title('Z Jump V Acceleration (Filtered 20)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpV_50['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump V Acceleration (Filtered 50)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpV_50['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Jump V Acceleration (Filtered 50)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpV_50['Acceleration z (m/s^2)'], label='Z Acceleration', color='brown')
axs[2].set_title('Z Jump V Acceleration (Filtered 50)')
axs[2].legend()

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot x jump filtered acceleration
axs[0].plot(filterJumpV_500['Acceleration x (m/s^2)'], label='X Acceleration', color='yellow')
axs[0].set_title('X Jump V Acceleration (Filtered 500)')
axs[0].legend()

# Plot y jump filtered acceleration
axs[1].plot(filterJumpV_500['Acceleration y (m/s^2)'], label='Y Acceleration', color='orange')
axs[1].set_title('Y Jump V Acceleration (Filtered 500)')
axs[1].legend()

# Plot z jump filtered acceleration
axs[2].plot(filterJumpV_500['Acceleration z (m/s^2)'], label='Z Acceleration', color='brown')
axs[2].set_title('Z Jump V Acceleration (Filtered 500)')
axs[2].legend()

plt.tight_layout()
plt.show()
