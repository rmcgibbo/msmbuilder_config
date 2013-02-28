from msmb.config.app import MSMBuilderApp
from msmb.metrics.rmsd import RMSD
from msmb.metrics.pnorm import PNorm


class Assign(MSMBuilderApp):
    name = 'assign'
    path = 'msmb.commands.assign.Assign'
    short_description = 'Assign trajectories to microstates.'
    long_description = """
Assign data that were not originally used in the clustering (because of
striding) to the microstates. This is applicable to all medoid-based
clustering algorithms, which includes all those implemented by Cluster.py
except the hierarchical methods. (For assigning to a hierarchical clustering,
use AssignHierarchical.py)

Outputs:
-Assignments.h5
-Assignments.h5.distances

Assignments.h5 contains the assignment of each frame of each trajectory to a
microstate in a rectangular array of ints. Assignments.h5.distances is an
array of real numbers of the same dimension containing the distance (according
to whichever metric you choose) from each frame to to the medoid of the
microstate it is assigned to."""

    def start(self):
        print 'starting assign -- calling library function'