import datetime

def createFileNames(numFiles):
    """
    Returns a list of file names.
    """
    names = []
    for i in range(numFiles):
        names.append(f'file{i}.bin')
    return names


def writePacket(byteArray, fileName):
    """
    Returns the time required to write a packet to a file.
    """
    start = datetime.datetime.now()
    f = open(fileName, 'a+b')
    f.write(byteArray)
    f.close()
    return datetime.datetime.now() - start


def createPacket(packetSize):
    """
    Returns a byteArray of the size specified by packetSize
    """
    data = ''
    for i in range(packetSize - 1):
        data = data + 'A'
    return bytearray(data + 'B', 'utf-8')

def timeWrite(fileNames, defaults):
    """
    returns the time taken to write a number of packets to binary files.
    """
    times = []
    byteArray = createPacket(defaults['packetSize'])
    for name in fileNames:
        for i in range(defaults['numWrites']):
            times.append(writePacket(byteArray, name))
    return times

