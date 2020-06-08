import matplotlib.pyplot as plt

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
    Generates a histogram of the specified title with the data provided.  Gives an option to save to a png.
    """
    plt.hist(data, density=1, bins=200)
    plt.title(title)
    if show == True:
        plt.show()
    if save == True:
        plt.savefig(f'{title}.png')
