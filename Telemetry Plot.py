import pandas as pd
import matplotlib.pyplot as plt
import time

#read the CSV files
df_alpha = pd.read_csv('resources/alpha.csv')
df_bravo = pd.read_csv('resources/bravo.csv')
df_charlie = pd.read_csv('resources/charlie.csv')
df_delta = pd.read_csv('resources/delta.csv')
df_echo = pd.read_csv('resources/echo.csv')
df_foxtrot = pd.read_csv('resources/foxtrot.csv')
df_golf = pd.read_csv('resources/golf.csv')

def plot_sensor_data(df_path):
  #This function takes in file path as input and outputs graphs corresponding to 3 gyro values, 4 wheel rpms, low voltage and bus voltage values with respect to relative time, the time of T0 is also shown

  # Extract filename from path (assuming path ending with ".csv")
  filename = df_path.split("/")[-1].split(".")[0]

  #start time for runtime calculation
  start_time = time.time()

  # Read CSV data
  df = pd.read_csv(df_path)

  # Convert timestamp to datetime
  df['times'] = pd.to_datetime(df['timestamp'], unit='ms')
  Tini = df['times'].iloc[0]

  # Set first timestamp as t0
  t0 = df["timestamp"].iloc[0]

  # Calculate relative time (using milliseconds)
  df["relative_time"] = df["timestamp"] - t0

  # Extract sensor data
  sensor_data = {
      "gyro_x (deg/sec)": df["gyro_x"],
      "gyro_y (deg/sec)": df["gyro_y"],
      "gyro_z (deg/sec)": df["gyro_z"],
      "wheel_s (rpm)": df["wheel_s"],
      "wheel_x (rpm)": df["wheel_x"],
      "wheel_y (rpm)": df["wheel_y"],
      "wheel_z (rpm)": df["wheel_z"],
      "low_voltage (v)": df["low_voltage"],
      "bus_voltage (v)": df["bus_voltage"],
  }

  # Create subplots
  fig, axes = plt.subplots(3, 3, figsize=(15, 10))

  # Add text with t0 value at the top of the figure
  fig.suptitle(f"Time is relative to Time Zero. For {filename} satellite the current T0 is {Tini.strftime('%Y-%m-%d %H:%M:%S.%f')}", fontsize=14)

  # Add margins and spacing between subplots
  plt.subplots_adjust(left=1.4, right=1.5, top=1.5, bottom=1.4, wspace=0.3, hspace=0.6)

  # Convert time (ms) to time in hrs
  df["relative_time_hrs"] = df["relative_time"] / 3600000

  # Plot sensor data vs time
  for i, (sensor_name, data) in enumerate(sensor_data.items()):
      row, col = divmod(i, 3)
      axes[row, col].plot(df["relative_time_hrs"], data, label=sensor_name)
      axes[row, col].set_xlabel("Relative Time (hrs)")
      axes[row, col].set_ylabel(sensor_name + " value")

  # Adjust layout
  plt.tight_layout()

  # End time measurement and calculate runtime
  end_time = time.time()
  runtime = end_time - start_time

  # Print runtime message
  print(f"Figure for {filename} generated in {runtime:.2f} seconds.")

  # Show plot
  plt.show()


# Usage example, change values here to get different plots
plot_sensor_data("resources/alpha.csv")