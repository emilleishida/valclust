import sys
import valclust
import numpy as np
import valclust.external as exv


d = np.loadtxt("tests/example.dat")

def test_largeData_MCC():
   sys.stderr.write( "\t\tWelcome to ValClust!\n\t\tPerforming a large test ...\n")

   obj = exv.CompareCluster(X=None, y=d[:,0], g=d[:,1])

   sys.stderr.write("Num sing: %d\n" %obj._num_singletons())

   obj.summary()

   sys.stderr.write("N-Distinct %d\n" %(obj.n_distinct()))

   for i in range(10):
      sys.stderr.write("Cluster %3d :: Size %3d   Purity %.3f\n"%(i, obj.ysize[i,1], obj.clusterPurity(i+1)))


   sys.stderr.write("Purity: %.3f   WeightedPurity: %.3f\n" %(obj.totalPurity()[0], obj.totalPurity()[1]))

   pass
