import math
import tkinter as tk

# create a function to calculate track angle and ground speed
def calculate():
    # get inputs from user
    wind_dir = float(wind_dir_entry.get())
    wind_vel = float(wind_vel_entry.get())
    tas = float(tas_entry.get())
    hdg = float(hdg_entry.get())

    # convert inputs to radians
    wind_dir_rad = math.radians(wind_dir)
    hdg_rad = math.radians(hdg)

    # calculate track angle and ground speed
    crosswind = wind_vel * math.sin(wind_dir_rad - hdg_rad)
    headwind = wind_vel * math.cos(wind_dir_rad - hdg_rad)
    gs = tas - headwind
    if gs == 0:
        track_units = 0
    else:
        track_units = math.degrees(math.atan(crosswind / gs))

    # calculate refined track angle
    if track_units < 0:
        actual_track_ang = hdg + abs(round(track_units, -1))
    else:
        actual_track_ang = hdg - abs(round(track_units, -1))

    # display results
    result_label.config(text="Track Units: " + str(round(track_units, 2)) + " degrees\n\nActual track angle: " + str(round(actual_track_ang, 2)) + " degrees\nGround speed: " + str(round(gs, 2)) + " knots")

# create a window
window = tk.Tk()
window.title("Calculate Track and Ground Speed")

# set window size
window.geometry("800x600")

# Add a title label
title_label = tk.Label(window, text="Calculate Track And Ground Speed", font=("Cray", 26, "bold"))
title_label.pack(side="top", pady=20)


# create a label for wind direction
wind_dir_label = tk.Label(window, text="Wind Direction (in degrees): ", font=("Arial", 20))
wind_dir_label.pack(pady=10)

# create an entry box for wind direction
wind_dir_entry = tk.Entry(window, font=("Arial", 20), bd=2, relief="groove")
wind_dir_entry.pack()

# create a label for wind velocity
wind_vel_label = tk.Label(window, text="Wind Velocity (in knots): ", font=("Arial", 20))
wind_vel_label.pack(pady=10)

# create an entry box for wind velocity
wind_vel_entry = tk.Entry(window, font=("Arial", 20), bd=2, relief="groove")
wind_vel_entry.pack()

# create a label for true air speed
tas_label = tk.Label(window, text="True Air Speed (in knots): ", font=("Arial", 20))
tas_label.pack(pady=10)

# create an entry box for true air speed
tas_entry = tk.Entry(window, font=("Arial", 20), bd=2, relief="groove")
tas_entry.pack()

# create a label for heading
hdg_label = tk.Label(window, text="Heading (in degrees): ", font=("Arial", 20))
hdg_label.pack(pady=10)

# create an entry box for heading
hdg_entry = tk.Entry(window, font=("Arial", 20), bd=2, relief="groove")
hdg_entry.pack()

# create a button to calculate track angle and ground speed
calculate_button = tk.Button(window, text="Calculate", font=("Arial", 20), command=calculate, bg="green", fg="white")
calculate_button.pack(pady=20)

# create a label to display results
result_label = tk.Label(window, text="", font=("Arial", 20), fg="blue")
result_label.pack()

# start the event loop
window.mainloop()
