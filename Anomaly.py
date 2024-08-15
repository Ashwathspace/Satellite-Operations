import pandas as pd
import time

def check_anomaly(filename):
    """
    This code checks if there is an anomaly in the wheels, if all the four wheels have consecutive 0 rpm for 100 consecutive time frames, then anomaly is detected
    """

    df = pd.read_csv(filename)

    # start time for runtime calculation
    start_time = time.time()

    columns_to_check = [4, 5, 6, 7] #takes the columns for wheels

    anomaly_detected = True
    for column in columns_to_check:
        data = df.iloc[:, column]

        consecutive_zeros = 0 #assign initial value to consecutive zeros
        for value in data:
            if pd.isna(value):
                continue  # Ignore NaN values
            elif value == 0:
                consecutive_zeros += 1
            else:
                consecutive_zeros = 0

            if consecutive_zeros >= 100:
                break  # Anomaly found in this column
        else:
            anomaly_detected = False  # No anomaly in this column
            break  # No need to check other columns

    if anomaly_detected:
        print("Anomaly detected!")
    else:
        print("No anomaly detected.")

    # End time measurement and calculate runtime
    end_time = time.time()
    runtime = end_time - start_time

    # Print runtime message
    print(f"Runtime for the code is {runtime:.2f} seconds.")


# Example usage, change values here to get anomaly detection for different csv files
check_anomaly("resources/delta.csv")
