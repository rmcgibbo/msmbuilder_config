from IPython.config.configurable import Configurable
from IPython.utils.traitlets import Unicode, Int


class RMSD(Configurable):
    atom_indices_fn = Unicode('atomindices.dat', config=True,
        help='Path to atom indices file')

    def __init__(self, config=None):
        super(RMSD, self).__init__(config=config)
        print 'loading up an RMSD object, with atom_indices=', self.atom_indices_fn

    def prepare_trajectory(self):
        pass
