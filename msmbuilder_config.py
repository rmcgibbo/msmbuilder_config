c = get_config()

c.MSMBuilderApp.display_banner = False
c.Cluster.project_fn = 'project.yaml'
c.Cluster.stride = 100
c.Cluster.metric = 'Pnorm'

#c.RMSD.atom_indices_fn = 'AtomIndices.dat'