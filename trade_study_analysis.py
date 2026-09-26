import matplotlib.pyplot as plt
import pandas as pd

# 1. Load exact OpenRocket trade study data
data = {
    "fin_sweep_deg": [0, 10, 20, 30, 40, 50],
    "stability_calibers": [1.82, 1.83, 1.81, 1.76, 1.65, 1.46],
    "apogee_m": [637, 640, 646, 657, 672, 686],
    "max_velocity_ms": [189, 190, 190, 191, 192, 192],
}

df = pd.DataFrame(data)

# 2. Create dual-axis figure
fig, ax1 = plt.subplots(figsize=(9, 5))

# Plot Apogee on Primary Y-Axis (Blue)
color_apogee = "tab:blue"
ax1.set_xlabel("Fin Sweep Angle (degrees)", fontsize=11, fontweight="bold")
ax1.set_ylabel(
    "Apogee Altitude (m)", color=color_apogee, fontsize=11, fontweight="bold"
)
ax1.plot(
    df["fin_sweep_deg"],
    df["apogee_m"],
    color=color_apogee,
    marker="o",
    linewidth=2.5,
    label="Apogee (m)",
)
ax1.tick_params(axis="y", labelcolor=color_apogee)
ax1.grid(True, linestyle="--", alpha=0.4)

# Plot Stability on Secondary Y-Axis (Red)
ax2 = ax1.twinx()
color_stab = "tab:red"
ax2.set_ylabel(
    "Static Stability (Calibers)",
    color=color_stab,
    fontsize=11,
    fontweight="bold",
)
ax2.plot(
    df["fin_sweep_deg"],
    df["stability_calibers"],
    color=color_stab,
    marker="s",
    linestyle="--",
    linewidth=2.5,
    label="Stability (cal)",
)
ax2.tick_params(axis="y", labelcolor=color_stab)

# Add 1.5 Caliber Safety Limit Line
ax2.axhline(
    y=1.5,
    color="black",
    linestyle=":",
    linewidth=2,
    label="Min Stability Limit (1.5 cal)",
)

# Plot Formatting
plt.title(
    "Parametric Trade Study: Fin Sweep Angle vs. Performance & Stability",
    fontsize=13,
    pad=15,
)
fig.tight_layout()

# Save image for GitHub / Portfolio
plt.savefig("fin_sweep_trade_study.png", dpi=300)
plt.show()
