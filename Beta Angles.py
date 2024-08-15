import pandas as pd
import matplotlib.pyplot as plt
import time


def plot_data(csv_file):
    #This function takes in path to a csv file, plots the beta angles vs different satellites, since some of the graphs may coincide, this function also points to the location of each plot

    # Read CSV data
    df = pd.read_csv(csv_file)

    # start time for runtime calculation
    start_time = time.time()

    # Read number of columns
    col = len(df.columns)

    def assign_relative_days(csv_file):
        #This function calculates relative days for better presentation of data compared to the date

        df = pd.read_csv(csv_file)
        first_date = pd.to_datetime(df.iloc[0, 0])  # Convert first date to datetime
        df['Relative Day'] = df.iloc[:, 0].apply(pd.to_datetime) - first_date  # Calculate relative days
        df['Relative Day'] = df['Relative Day'].dt.days + 1  # Convert to integer days and start from Day 1
        return df

    df = assign_relative_days(csv_file)

    # Extract data for plotting
    x_data = df.iloc[:, col]
    y_data_list = df.iloc[:, 1:col]

    # Generate plot
    plt.figure(figsize=(10, 6))
    for i, y_data in enumerate(y_data_list.columns):
        plt.plot(x_data, y_data_list[y_data], label=y_data)
        if i>3: #generating x and y positions for position of annotation
            x_annot = (len(x_data) / abs(i-7))
        else:
            x_annot = (len(x_data) / (i+1))
        y_correspond = y_data_list.iloc[int(x_annot-1),i] #generating y position corresponding to x annotation to point the arrow towards
        y_annot = round((max(y_data_list.iloc[:,i]) + min(y_data_list.iloc[:,i]))/2) #y annotation location at average of y values
        plt.annotate(y_data, xy=(x_annot,y_correspond), xytext=(x_annot,y_annot), arrowprops= dict(color="red"))

    # End time measurement and calculate runtime
    end_time = time.time()
    runtime = end_time - start_time

    # Print runtime message
    print(f"Figure for generated in {runtime:.2f} seconds.")

    # Customize plot
    plt.xlabel("Relative Days")
    plt.ylabel("Beta Angle")
    plt.title(f"Day is relative to Day 0, current D0 is {df.iloc[0,0]}") #adding title to reflect Day 0
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage, change values here to get different plots
csv_file = "resources/beta_sun_deg.csv"
plot_data(csv_file)