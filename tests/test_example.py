import sys
import valclust
import numpy as np
import valclust.external as exv


d = np.loadtxt("tests/example.dat")

def test_largeData_MCC():
   sys.stderr.write( "\t\tWelcome to ValClust!\n\t\tPerforming a large test ...\n")

   obj = exv.CompareCluster(X=None, y=d[:,0], g=d[:,1])

   sys.stderr.write("Num sing: %d" %obj._num_singletons())


   pass
