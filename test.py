import matplotlib.pyplot as plt
import numpy as np

# Random test data
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
print(all_data)
labels = ['x1', 'x2', 'x3']


# rectangular box plot
bplot1 = plt.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
colors = ['pink', 'lightblue', 'lightgreen']
for patch, color in zip(bplot1['boxes'], colors):
    patch.set_facecolor(color)
plt.grid(True)
plt.xlabel('Three separate samples')
plt.ylabel('Observed values')

# # fill with colors
# colors = ['pink', 'lightblue', 'lightgreen']
# for bplot in (bplot1):
#     for patch, color in zip(bplot['boxes'], colors):
        # patch.set_facecolor(color)

# # adding horizontal grid lines
# for ax in [ax1]:
#     ax.yaxis.grid(True)
#     ax.set_xlabel('Three separate samples')
#     ax.set_ylabel('Observed values')

plt.show()