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



