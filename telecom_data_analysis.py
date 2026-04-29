import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. GENERATE SYNTHETIC TELECOM TRAFFIC DATA
np.random.seed(42)

time = pd.date_range(start='2025-01-01', periods=200, freq='h')
traffic = np.random.normal(loc=100, scale=20, size=len(time))

# Add anomaly (spike)
traffic[50] = 300
traffic[120] = 10

df = pd.DataFrame({
    'timestamp': time,
    'traffic': traffic
})

# 2. BASIC ANALYSIS
print("Traffic Statistics:")
print(df['traffic'].describe())

# 3. ANOMALY DETECTION (Simple Threshold)
mean = df['traffic'].mean()
std = df['traffic'].std()

threshold_upper = mean + 2*std
threshold_lower = mean - 2*std

df['anomaly'] = ((df['traffic'] > threshold_upper) | 
                 (df['traffic'] < threshold_lower))

print("\nDetected anomalies:")
print(df[df['anomaly']])

# 4. VISUALIZATION
plt.figure(figsize=(12,6))
plt.plot(df['timestamp'], df['traffic'], label='Traffic')

plt.scatter(df[df['anomaly']]['timestamp'], 
            df[df['anomaly']]['traffic'],
            color='red', label='Anomaly')

plt.title("Telecom Traffic Analysis with Anomaly Detection")
plt.xlabel("Time")
plt.ylabel("Traffic Volume")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()