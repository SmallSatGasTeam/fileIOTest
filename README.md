# Binary File IO Test

## Introduction
The purpose of this test is to evaluate the speed at which python can open, write to, and close files in binary format.  This research is necessary to determine if a totally file based data storage method is viable for the Get Away Special Passive Attitude Control Satellite (GASPACS) mission.  The results were somewhat mixed but likely still within acceptable parameters for the mission.

## Methods
There were four processes tested in this procedure:
1. The time taken to open a binary file with Python.
2. The time taken to write a byte array of size 128 bytes to a binary file in Python.
3. The time taken to close a binary file with Python:
4. The time taken to open, write to, and close a binary file with the same byte array.
For each of the four trials, a 128 byte byte array was written to five files, 1000 times.  At the end of the trial, each file contained 5000 identical byte arrays.  Each byte array was a sequence of 127 "A" characters followed by one "B" character.  An ascii character is exactly one byte so the packet size came out to be exactly 128 bytes.  There should be no difference between writing a static byte array and writing random data to the file, as it takes the same amount of time to write a binary 0 to the file as it takes to write a binary 1. The trials were run on a Raspberry Pi Zero W.

## Results
The test code was written such that the only thing needed to run the experiment was Python3 and Pip.  The dependencies were installed by running `pip3 install -r requirements.txt` in the project directory, and then running `python3 main.py` to run the tests.  


