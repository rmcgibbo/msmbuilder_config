from msmb.config.app import MSMBuilderApp
from msmb.metrics.rmsd import RMSD
from msmb.metrics.pnorm import PNorm
from IPython.utils.traitlets import Unicode, Int, Enum

class Cluster(MSMBuilderApp):
    # the "name" field will be how this app will be called from the command
    # line. For example, this app will be accessible as "msmb cluster ..."
    name = 'cluster'
    path = 'msmb.commands.cluster.Cluster'
    
    # short_description will be displayed when listing all of the commands,
    # and should be able to fit onto a single line
    short_description = 'Cluster trajectories into microstates.'
    
    # the long_description will be displayed when the user asks for help on
    # specifically *this* app
    long_description = """
Output: Assignments.h5, and other files depending on your choice of distance
metric and/or clustering algorithm.

Note that there are many distance metrics and clustering algorithms available
Many of which have multiple options and parameters."""

    # The configurable options are all "traits". They're declared here like
    # class varaibles, but at run time they'll be instance variables on the
    # class i.e. self.project_fn, self.stride, etc. The value of the instance
    # variable is set by either (a) the default value, decalred here (b) a
    # value specified in the config file, or (c) a value passed on the
    # command line.

    # ALso, any object can subclass Configurable and get access to these. It's
    # not just subcommands of the msmb3.py script that can receive
    # configuration options. We can also set configurable values for objects
    # like the metrics or "representations", or really anything else.

    project_fn = Unicode(u'project.yaml', config=True,
        help='Path to project info file')
    stride = Int(1, config=True, help='Subsample by striding')
    output_dir = Unicode(u'data/', config=True,
        help='''Output directory to save clustering data. This will include:
        (1) Assignments.h5 (If clustering is hierarchical or stride=1):
        Contains the state assignments (2) Assignments.h5.distances (If
        clustering is hierarchical or stride=1): Contains the distance to the
        generator according to the distance metric that was employed (3)
        Gens.lh5 Trajectory object representing the generators for each
        state''')
    metric_type = Enum(['RMSD', 'Pnorm'], default_value='RMSD', config=True,
        help='What distance metric to use?')
    representation = Enum(['Cartesian', 'Dihedral', 'ContinuousContact'],
        default_value='Cartesian', config=True, help='''What representation of
        system to use? This amounts to picking a coordinate system. The RMSD
        metric should operate on cartesian coordinates, but other metrics
        require a coordinate system that removes the rotational symmetry, such
        as the space of backbone dihedral angles (Dihedral)''')

    # This line lets the App know that the user might want to configure the
    # RMSD or PNorm classes as well. This is nice, because it means that when
    # the --help-all flag is passed, the configurable traits for the RMSD and
    # PNorm classes will also be shown to the user
    classes = [RMSD, PNorm]

    # by making the optins aliased, they get displayed to the user on the
    # standard -h, instead of only on --help-all
    # we might be able to do this in an automated way in the superclass
    aliases = dict(project_fn='Cluster.project_fn',
        stride='Cluster.stride',
        output_dir='Cluster.output_dir',
        metric_type='Cluster.metric_type',
        representation='Cluster.representation')

    # start is the "main" method for the app. 
    def start(self):
        self.log.info('Starting up Cluster')
        if self.metric_type == 'RMSD':
            metric = RMSD(config=self.config)
        elif self.metric_type == 'PNorm':
            metric = PNorm(config=self.config)
        else:
            raise Exception()
            
        print 'Starting to cluster -- calling library function'
        print self.project_fn
        print self.representation
        print self.config
