import pandas as pd
from scipy.stats.morestats import Std_dev

data = pd.read_csv(
    "sensor_data_200.txt",
    delimiter=" ",
    header=None,
    names=("date", "time", "ir", "lidar"),
)

# print(data)

import matplotlib.pyplot as plt

# data["lidar"].hist(bins=max(data["lidar"]) - min(data["lidar"]), align="left")
# plt.show()

mean1 = data["lidar"].mean()

data["lidar"].hist(
    bins=max(data["lidar"]) - min(data["lidar"]), align="left", color="orange"
)
# plt.vlines(mean1, ymin=0, ymax=5000, colors="red")
# plt.show()
from scipy.stats import norm

zs = range(190, 230)
ys = [norm.pdf(z, mean1, Std_dev)]