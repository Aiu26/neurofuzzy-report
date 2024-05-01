import matplotlib.pyplot as plt

# Define universe variables
x_traffic_flow = np.arange(0, 101, 1)
x_congestion = np.arange(0, 101, 1)
x_light_timing = np.arange(0, 101, 1)

# Calculate membership functions
low_traffic_flow = fuzz.trimf(x_traffic_flow, [0, 0, 50])
moderate_traffic_flow = fuzz.trimf(x_traffic_flow, [20, 50, 80])
high_traffic_flow = fuzz.trimf(x_traffic_flow, [50, 100, 100])

low_congestion = fuzz.trimf(x_congestion, [0, 0, 50])
moderate_congestion = fuzz.trimf(x_congestion, [20, 50, 80])
high_congestion = fuzz.trimf(x_congestion, [50, 100, 100])

short_light_timing = fuzz.trimf(x_light_timing, [0, 0, 50])
medium_light_timing = fuzz.trimf(x_light_timing, [20, 50, 80])
long_light_timing = fuzz.trimf(x_light_timing, [50, 100, 100])

# Plot membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 10))

ax0.plot(x_traffic_flow, low_traffic_flow, 'b', linewidth=1.5, label='Low Traffic Flow')
ax0.plot(x_traffic_flow, moderate_traffic_flow, 'g', linewidth=1.5, label='Moderate Traffic Flow')
ax0.plot(x_traffic_flow, high_traffic_flow, 'r', linewidth=1.5, label='High Traffic Flow')
ax0.set_title('Traffic Flow')
ax0.legend()

ax1.plot(x_congestion, low_congestion, 'b', linewidth=1.5, label='Low Congestion')
ax1.plot(x_congestion, moderate_congestion, 'g', linewidth=1.5, label='Moderate Congestion')
ax1.plot(x_congestion, high_congestion, 'r', linewidth=1.5, label='High Congestion')
ax1.set_title('Congestion')
ax1.legend()

ax2.plot(x_light_timing, short_light_timing, 'b', linewidth=1.5, label='Short Light Timing')
ax2.plot(x_light_timing, medium_light_timing, 'g', linewidth=1.5, label='Medium Light Timing')
ax2.plot(x_light_timing, long_light_timing, 'r', linewidth=1.5, label='Long Light Timing')
ax2.set_title('Light Timing')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
