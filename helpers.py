import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import statistics

def createFileNames(numFiles):
    """
    Returns a list of file names.
    """
    names = []
    for i in range(numFiles):
        names.append(f'file{i}.bin')
    return names


def createPacket(packetSize):
    """
    Returns a byteArray of the size specified by packetSize.
    """
    data = ''
    for i in range(packetSize - 1):
        data = data + 'A'
    return bytearray(data + 'B', 'utf-8')


def generatePlot(data, title, save, show):
    """
    Generates a plot of the specified title with the data provided.  Gives an option to save to a png.
    """
    data.sort()
    ax = plt.subplot()
    plt.plot(data)
    plt.title(title)
    anchoredText = AnchoredText(f'max: {max(data)} (sec)\nmean: {statistics.mean(data)} (sec)\nmin: {min(data)} (sec)', loc=2)
    ax.add_artist(anchoredText)
    ax.set_ylabel('Time (s)')
    ax.set_xlabel('Trial (sorted by time)')
    if show == True:
        plt.show()
    if save == True:
        plt.savefig(f'{title}.png')
    ax.remove()
