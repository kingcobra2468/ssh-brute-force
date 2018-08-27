import math
import multiprocessing 
import connection
import numpy
import sys
import time
import itertools

class brute():
    
    def __init__(self):
        pass 

    def buildString(self, asciiCode):
        string = str()
        for x in asciiCode:
            string+=chr(x)
        return string

    def genPass(self):
        index = numpy.arange(33,127, dtype = int)
        currentIndex = numpy.size(index) - 1
        connect = connection.connection(sys.argv[1], sys.argv[2])
        currentSize = 1
        while not connect.passFound(connect):      
            for x in itertools.permutations(index, currentSize): #program for same values repeating
                process=multiprocessing.Process(connect.attemptConnection(self.buildString(x)))
                if connect.passFound(connect):
                    print("Pass Found {}".format(self.buildString(x)))
                    break
                #self.buildString(x)
            currentSize+=1

test = brute()
test.genPass()
                





