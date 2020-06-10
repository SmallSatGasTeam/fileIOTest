import sys
import datetime
import matplotlib.pyplot as plt

from helpers import createFileNames, createPacket, generatePlot
from timers import timeFullWrite, timeWritePacket, timeOpenBin, timeCloseBin

# one character = one byte

if __name__ == '__main__':
    defaults = {'numFiles': 5, 'numWrites': 1000, 'numReads': 1000, 'packetSize': 128}
    fileNames = createFileNames(defaults['numFiles'])

#    generatePlot([1,2,3,4], 'test', False, True)
    
    fullTimes = timeFullWrite(fileNames, defaults)
    print('fullTimes')
    writeTimes = timeWritePacket(fileNames, defaults)
    print('writeTimes')
    openTimes = timeOpenBin(defaults['numWrites'])
    print('openTimes')
    closeTimes = timeCloseBin(defaults['numWrites'])
    print('closeTimes')

    generatePlot(fullTimes, 'time to open, write, and close', True, True)
#    generatePlot(writeTimes, 'time to write', True, True)
#    generatePlot(openTimes, 'time to open', True, True)
#    generatePlot(closeTimes, 'time to close', True, True)

