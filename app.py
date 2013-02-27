from base import MSMBuilderApp
from IPython.config.configurable import Configurable
from IPython.utils.traitlets import Unicode, Int, Enum

import numpy as np


###############################
# BEGIN EXAMPLE METRICS   
###############################

class RMSD(Configurable):
    atom_indices_fn = Unicode('atomindices.dat', config=True,
        help='Path to atom indices file')
    
    def __init__(self, config=None):
        super(RMSD, self).__init__(config=config)
        self.atom_indices = np.loadtxt(self.atom_indices_fn, dtype=np.int)
    
    def prepare_trajectory(self):
        pass

class PNorm(Configurable):
    order = Int(2, config=True, help='Order of norm')

###############################
# END EXAMPLE METRICS   
###############################


###############################
# BEGIN EXAMPLE SUBCOMMANDS
###############################

class Cluster(MSMBuilderApp):
    name = 'cluster'
    path = 'app.Cluster'
    short_description = 'Cluster trajectories into microstates.'
    long_description = """
Output: Assignments.h5, and other files depending on your choice of distance
metric and/or clustering algorithm.

Note that there are many distance metrics and clustering algorithms available
Many of which have multiple options and parameters."""

    project_fn = Unicode(u'project.yaml', config=True,
        help='Path to project info file')
    stride = Int(1, config=True, help='Subsample by striding')
    output_dir = Unicode(u'data/', config=True,
        help='''Output directory to save clustering data. This will include:
        (1) Assignments.h5 (If clustering is hierarchical or stride=1): Contains
        the state assignments (2) Assignments.h5.distances (If clustering is 
        hierarchical or stride=1): Contains the distance to the generator 
        according to the distance metric that was employed (3) Gens.lh5:
        Trajectory object representing the generators for each state''')
    metric_type = Enum(['RMSD', 'Pnorm'], default_value='RMSD', config=True,
        help='What distance metric to use?')
    representation = Enum(['Cartesian', 'Dihedral', 'ContinuousContact'],
        default_value='Cartesian', config=True, help='''What representation of 
        system to use? This amounts to picking a coordinate system. The RMSD
        metric should operate on cartesian coordinates, but other metrics require
        a coordinate system that removes the rotational symmetry, such as the space
        of backbone dihedral angles (Dihedral)''')
    classes = [RMSD, PNorm]
    
    
    # by making the optins aliased, they get displayed to the user on the
    # standard -h, instead of only on --help-all
    # we might be able to do this in an automated way in the superclass
    aliases = dict(project_fn='Cluster.project_fn',
        stride='Cluster.stride',
        output_dir='Cluster.output_dir',
        metric_type='Cluster.metric_type',
        representation='Cluster.representation')
        
    def start(self):
        self.log.info('Starting up Cluster')
        if self.metric_type == 'RMSD':
            metric = RMSD(config=self.config)
            metric.prepare_trajectory()




class Assign(MSMBuilderApp):
    name = 'assign'
    path = 'app.Assign'
    short_description = 'Assign trajectories to microstates.'
    long_description = """
Assign data that were not originally used in the clustering (because of
striding) to the microstates. This is applicable to all medoid-based clustering
algorithms, which includes all those implemented by Cluster.py except the
hierarchical methods. (For assigning to a hierarchical clustering, use 
AssignHierarchical.py)

Outputs:
-Assignments.h5
-Assignments.h5.distances

Assignments.h5 contains the assignment of each frame of each trajectory to a 
microstate in a rectangular array of ints. Assignments.h5.distances is an 
array of real numbers of the same dimension containing the distance (according 
to whichever metric you choose) from each frame to to the medoid of the 
microstate it is assigned to."""
    
    def start(self):
        print 'STARTING Assign!'
    