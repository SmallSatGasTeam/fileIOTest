import sys
import datetime
import matplotlib.pyplot as plt

from helpers import createFileNames, createPacket
from timers import timeFullWrite, timeWritePacket, timeOpenBin, timeCloseBin

# one character = one byte

if __name__ == '__main__':
    defaults = {'numFiles': 5, 'numWrites': 1000, 'numReads': 1000, 'packetSize': 128}
    fileNames = createFileNames(defaults['numFiles'])
    
    fullTimes = timeFullWrite(fileNames, defaults)
    print('fullTimes')
    writeTimes = timeWritePacket(fileNames, defaults)
    print('writeTimes')
    openTimes = timeOpenBin(defaults['numWrites'])
    print('openTimes')
    closeTimes = timeCloseBin(defaults['numWrites'])
    print('closeTimes')

    plt.hist(fullTimes, density=1, bins=100)
#    plt.savefig('fullTimes.png')
    plt.show()
    plt.hist(writeTimes, density=1, bins=100)
    plt.show()
    plt.hist(openTimes, density=1, bins=100)
    plt.show()
    plt.hist(closeTimes, density=1, bins=100)
    plt.show()
