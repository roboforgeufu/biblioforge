import matplotlib.pyplot as plt
import pandas as pd

def import_and_convert_csv(csv_file):
    df = pd.read_csv(csv_file)
    x, y, z = df.items()

    xs = []
    ys = []
    zs = []

    for i in range(len(df)):
        xs.append(x[1][i])
        ys.append(y[1][i])
        zs.append(z[1][i])
    
    return xs, ys, zs

def main():
    columns_array = ['R', 'G', 'B']

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    ax.set_zlim([0, 100])

    file_names = [
        'calibration_sensor_Port.S1_Color.BLUE_2020_04_11_02_38_00_002935.csv',
        'calibration_sensor_Port.S1_Color.BROWN_2020_04_11_02_39_22_229294.csv',
        'calibration_sensor_Port.S1_Color.BLACK_2020_04_11_02_39_39_117926.csv',
        'calibration_sensor_Port.S1_Color.GREEN_2020_04_11_02_39_05_486703.csv',
        'calibration_sensor_Port.S1_Color.RED_2020_04_11_02_38_48_567920.csv',
        'calibration_sensor_Port.S1_Color.WHITE_2020_04_11_02_40_17_819093.csv',
        'calibration_sensor_Port.S1_Color.YELLOW_2020_04_11_02_39_57_169476.csv'
    ]
    color_names = ['blue', 'brown', 'black', 'green', 'red', 'white', 'yellow']

    for i in range(len(color_names)):
        x_points, y_points, z_points = import_and_convert_csv(file_names[i])
        ax.scatter(x_points, y_points, z_points, color=color_names[i])
        x_points.clear()
        y_points.clear()
        z_points.clear()

    ax.set_xlabel(columns_array[0])
    ax.set_ylabel(columns_array[1])
    ax.set_zlabel(columns_array[2])

    plt.show()

main()