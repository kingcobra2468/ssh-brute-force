import math
import enum
import threading
import connection
import numpy
import sys

class brute(threading.Thread):
    def __init__(self, threadCount):
        self.createThreads(threadCount)

    def buildString(self, asciiCode):
        string = str()
        for x in asciiCode:
            string+=chr(x)
        return string

    def threads(self, password):
        attempt = threading.Thread(
                target=connect.attemptConnection, 
                args = self.buildString(index))

    def genPass(self):
        index=numpy.empty(dtype=int)
        index=numpy.append(index, 33) #126
        currentIndex = numpy.size(index) - 1
        connect = connection.connection(sys.argv[1], sys.argv[2])
        while !connection.connection.__passfound():
            for curIndex in reversed(range(numpy.size(index))):     
                if num[0] == 126:
                    index.fill(33)
                    numpy.append(index, 33)
                    break
                else:
                    for indexes in range(numpy.size(index)-curIndex, numpy.size(index),1)
                        index[indexes] = 33
                while index[curIndex] != 126:
                    index[curIndex] += 1
                    return index

                





