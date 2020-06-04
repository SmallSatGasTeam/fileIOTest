import sys
import datetime

from helpers import createFileNames, createPacket, writePacket, timeWrite

# one character = one byte

if __name__ == '__main__':
    print(sys.argv)
    defaults = {'numFiles': 5, 'numWrites': 1000, 'numReads': 1000, 'packetSize': 128}
    fileNames = createFileNames(defaults['numFiles'])
    print(fileNames)
    
    times = timeWrite(fileNames, defaults)
    print(times)
#    print(f"average write time per {defaults['packetSize']} byte packet: {time / defaults['numWrites']}")







