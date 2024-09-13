import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(".\Logs\log_turn_PID.csv", sep=", ", decimal=".")

time = df["Time"]
kp = df["KP"]
kd = df["KD"]
ki = df["KI"]
pid = df["PID"]
angle = df["Angle"]

plt.plot(time, pid, color="blue")
plt.plot(time, angle, color="red")
plt.title("Angle and PID over time")
plt.xlabel("Time")

plt.show()
