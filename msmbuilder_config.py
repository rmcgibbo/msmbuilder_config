# Configuration file for msmbuilder.

c = get_config()

#------------------------------------------------------------------------------
# MSMBuilderApp configuration
#------------------------------------------------------------------------------

# This is an application.

# MSMBuilderApp will inherit config from: Application

# Whether to display a banner upon starting MSMBuilder.
# c.MSMBuilderApp.display_banner = True

# The Logging format template
# c.MSMBuilderApp.log_format = '[%(name)s] %(message)s'

# Set the log level by value or name.
# c.MSMBuilderApp.log_level = 30

#------------------------------------------------------------------------------
# RootApplication configuration
#------------------------------------------------------------------------------

# This is an application.

# RootApplication will inherit config from: MSMBuilderApp, Application

# Whether to display a banner upon starting MSMBuilder.
# c.RootApplication.display_banner = True

# The Logging format template
# c.RootApplication.log_format = '[%(name)s] %(message)s'

# Set the log level by value or name.
# c.RootApplication.log_level = 30

#------------------------------------------------------------------------------
# Assign configuration
#------------------------------------------------------------------------------

# This is an application.

# Assign will inherit config from: MSMBuilderApp, Application

# Whether to display a banner upon starting MSMBuilder.
# c.Assign.display_banner = True

# The Logging format template
# c.Assign.log_format = '[%(name)s] %(message)s'

# Set the log level by value or name.
# c.Assign.log_level = 30

#------------------------------------------------------------------------------
# AtomIndices configuration
#------------------------------------------------------------------------------

# This is an application.

# AtomIndices will inherit config from: MSMBuilderApp, Application

# Whether to display a banner upon starting MSMBuilder.
# c.AtomIndices.display_banner = True

# The Logging format template
# c.AtomIndices.log_format = '[%(name)s] %(message)s'

# Set the log level by value or name.
# c.AtomIndices.log_level = 30

# Atoms to include in index file. One of four options: (1) minimal (CA, CB, C,
# N, O, recommended), (2) heavy, (3) alpha (carbons), or (4) all.  Use "all" in
# cases where protein nomenclature may be inapproprate, although you may want to
# define your own indices in such situations.  Note that "heavy" keeps all heavy
# atoms that are not symmetry equivalent.  By symmetry equivalent, we mean atoms
# identical under an exchange of labels.  For example, heavy will exclude the
# two pairs of equivalent carbons (CD, CE) in a PHE ring. Note that
# AtomIndices.dat should be zero-indexed--that is, a 0  in AtomIndices.dat
# corresponds to the first atom in your PDB.
# c.AtomIndices.atom_type = 'minimal'

#------------------------------------------------------------------------------
# Cluster configuration
#------------------------------------------------------------------------------

# This is an application.

# Cluster will inherit config from: MSMBuilderApp, Application

# Set the log level by value or name.
# c.Cluster.log_level = 30

# Subsample by striding
# c.Cluster.stride = 1

# Output directory to save clustering data. This will include: (1)
# Assignments.h5 (If clustering is hierarchical or stride=1): Contains the state
# assignments (2) Assignments.h5.distances (If clustering is hierarchical or
# stride=1): Contains the distance to the generator according to the distance
# metric that was employed (3) Gens.lh5 Trajectory object representing the
# generators for each state
# c.Cluster.output_dir = u'data/'

# Whether to display a banner upon starting MSMBuilder.
# c.Cluster.display_banner = True

# What distance metric to use?
# c.Cluster.metric_type = 'RMSD'

# What representation of system to use? This amounts to picking a coordinate
# system. The RMSD metric should operate on cartesian coordinates, but other
# metrics require a coordinate system that removes the rotational symmetry, such
# as the space of backbone dihedral angles (Dihedral)
# c.Cluster.representation = 'Cartesian'

# The Logging format template
# c.Cluster.log_format = '[%(name)s] %(message)s'

# Path to project info file
# c.Cluster.project_fn = u'project.yaml'

#------------------------------------------------------------------------------
# MKProfile configuration
#------------------------------------------------------------------------------

# This is an application.

# MKProfile will inherit config from: MSMBuilderApp, Application

# Whether to display a banner upon starting MSMBuilder.
# c.MKProfile.display_banner = True

# The Logging format template
# c.MKProfile.log_format = '[%(name)s] %(message)s'

# Set the log level by value or name.
# c.MKProfile.log_level = 30

# Output directory in which to save the file msmbuilder_config.py
# c.MKProfile.output_dir = '.'

#------------------------------------------------------------------------------
# RMSD configuration
#------------------------------------------------------------------------------

# Path to atom indices file
# c.RMSD.atom_indices_fn = 'atomindices.dat'

#------------------------------------------------------------------------------
# PNorm configuration
#------------------------------------------------------------------------------

# Order of norm
# c.PNorm.order = 2

