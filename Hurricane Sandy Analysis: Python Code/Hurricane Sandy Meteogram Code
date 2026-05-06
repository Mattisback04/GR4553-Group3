import pandas as pd
import matplotlib.pyplot as plt

# Original data was extracted manually from the NDBC website and pasted into a CSV. 
# Remember to check for NANs!
sandy_buoy_data = pd.read_csv('buoy_data.csv')

# Combines the Date and time into one column and converts it to datatime
sandy_buoy_data.columns = sandy_buoy_data.columns.str.strip()
sandy_buoy_data["Datetime"] = pd.to_datetime(sandy_buoy_data["Date"] + " " + sandy_buoy_data["Time"])
sandy_buoy_data = sandy_buoy_data.sort_values("Datetime").set_index("Datetime")

sandy_buoy_data["Pressure"] = pd.to_numeric(sandy_buoy_data["Pressure"], errors="coerce")
sandy_buoy_data["Temp"] = pd.to_numeric(sandy_buoy_data["Temp"], errors="coerce")
sandy_buoy_data["Water Temp"] = pd.to_numeric(sandy_buoy_data["Water Temp"], errors="coerce")

fig, ax1 = plt.subplots(figsize=(12, 5))

# Pressure
ax1.plot(sandy_buoy_data.index, sandy_buoy_data["Pressure"], color="tab:blue", label="Pressure")
ax1.set_ylabel("Pressure (hPa)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax1.grid(True)
ax1.set_ylim(940, 1015)

# Temperature
# (sets the water temp and temp to the right y-axis and to share the right side y-axis that shares the same x-axis)
ax2 = ax1.twinx()
ax2.plot(sandy_buoy_data.index, sandy_buoy_data["Temp"], color="tab:red", label="Air Temp")
ax2.plot(sandy_buoy_data.index, sandy_buoy_data["Water Temp"], color="tab:green", label="Water Temp")
ax2.set_ylabel("Temperature (°C)")

# Legend
# (combines the axes so the meteogram shares the axes)
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles + handles2, labels + labels2)

plt.title("Atlantic City, NJ: Buoy Station ACYN4 Meteogram")
plt.show()
