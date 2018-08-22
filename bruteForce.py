import math
import enum
import threading
import connection
import numpy
import sys
import time

class brute(threading.Thread):
    def __init__(self, threadCount):
        # self.createThreads(threadCount)
        pass 

    def buildString(self, asciiCode):
        string = str()
        for x in asciiCode:
            string+=chr(x)
        print("String %s" % string)
        return string

    def threads(self, password):
        attempt = threading.Thread(
                target=connect.attemptConnection, 
                args = self.buildString(index))

    def genPass(self):
        index=numpy.array([33], dtype=int) #126
        currentIndex = numpy.size(index) - 1
        connect = connection.connection(sys.argv[1], sys.argv[2])
        while not connect.passFound(connect):      
            for curIndex in reversed(range(numpy.size(index))):
                if index[0] == 126:
                    print("FOOOOR")
                    index.fill(33)
                    index=numpy.append(index, 33)
                    break
                else:
                    for indexes in range(curIndex, numpy.size(index),1):
                        index[indexes] = 33
                print(curIndex)
                time.sleep(3)
                while index[curIndex] != 126:
                    #Figure out recursive loops to file in x123 look into itertools
                    for x in reversed(range(curIndex + 1, numpy.size(index),1)):

                        while index[numpy.size(index) - 1] != 126:
                        index[x]+=1
                        self.buildString(index)
                    #print(index[curIndex], "SIZE %i" % numpy.size(index))
                    index[curIndex] += 1
                    #return index

            
test = brute(2)
test.genPass()
                





