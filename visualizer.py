import matplotlib.pyplot as plt

def visualize(*datasets):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for data in datasets:
        ax.plot([i[0] for i in data], [i[1] for i in data], '-')
    plt.annotate("This is a test.", xy=(0.2, 0.2), xycoords='axes fraction')
    plt.show()
