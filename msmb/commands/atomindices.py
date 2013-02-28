from msmb.config.app import MSMBuilderApp
from IPython.utils.traitlets import Unicode, Int, Enum

class AtomIndices(MSMBuilderApp):
    name = "atomindices"
    path = 'msmb.commands.atomindices.AtomIndices'
    short_description = 'Construct list of atoms for RMSD calculations'
    long_description = '''This app will parse a PDB file to determine which
atoms to use in an RMSD calculation.
    '''
    
    atom_type = Enum(['minimal', 'heavy', 'alpha', 'all'], config=True,
        help='''Atoms to include in index file. One of four options: (1)
        minimal (CA, CB, C, N, O, recommended), (2) heavy, (3) alpha
        (carbons), or (4) all.  Use "all" in cases where protein
        nomenclature may be inapproprate, although you may want to define your
        own indices in such situations.  Note that "heavy" keeps all heavy
        atoms that are not symmetry equivalent.  By symmetry equivalent, we
        mean atoms identical under an exchange of labels.  For example, heavy
        will exclude the two pairs of equivalent carbons (CD, CE) in a PHE
        ring. Note that AtomIndices.dat should be zero-indexed--that is, a 0 
        in AtomIndices.dat corresponds to the first atom in your PDB.''',
        default_value='minimal')

    aliases = dict(atom_type='AtomIndices.atom_type')
    
    def start(self):
        raise NotImplementedError()