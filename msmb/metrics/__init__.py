import numpy as np

from IPython.config.configurable import Configurable
from IPython.utils.traitlets import Unicode, Int


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