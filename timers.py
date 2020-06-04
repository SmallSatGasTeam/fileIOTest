import datetime
from helpers import createPacket

def timeFullWrite(fileNames, defaults):
    """
    returns the time taken to open n binary files, 
    write a number of packets to them and close the files.
    """
    times = []
    byteArray = createPacket(defaults['packetSize'])
    for name in fileNames:
        for i in range(defaults['numWrites']):
            times.append(fullWrite(byteArray, name).total_seconds())
    return times


def fullWrite(byteArray, fileName):
    """
    Returns the time required to open a file, write a packet to it, and close the file.
    """
    start = datetime.datetime.now()
    f = open(fileName, 'a+b')
    f.write(byteArray)
    f.close()
    end = datetime.datetime.now()
    return end - start


def timeWritePacket(fileNames, defaults):
    """
    returns the times taken only to write n binary files m times.
    """
    times = []
    byteArray = createPacket(defaults['packetSize'])
    for name in fileNames:
        for i in range(defaults['numWrites']):
            times.append(writePacket(byteArray, name).total_seconds())
    return times


def writePacket(byteArray, fileName):
    """
    returns the time taken only to write to a single binary file.
    """
    f = open(fileName, 'w+b')
    start = datetime.datetime.now()
    f.write(byteArray)
    end = datetime.datetime.now()
    f.close()
    return end - start


def timeOpenBin(numTimes):
    """
    returns the times taken to open a binary file n times
    """
    times = []
    for i in range(numTimes):
        times.append(openBin().total_seconds())
    return times


def openBin():
    """
    returns the time taken to open a file in binary mode.
    """
    start = datetime.datetime.now()
    f = open('dummy.bin', 'w+b')
    end = datetime.datetime.now()
    delta = end - start
    f.close()
    return delta


def timeCloseBin(numTimes):
    """
    returns the time taken to close a file in binary mode.
    """
    times = []
    for i in range(numTimes):
        times.append(closeBin().total_seconds())
    return times


def closeBin():
    """
    returns the time taken to close a file in binary mode.
    """
    f = open('dummy.bin', 'w+b')
    start = datetime.datetime.now()
    f.close()
    end = datetime.datetime.now()
    delta = end - start
    return delta

