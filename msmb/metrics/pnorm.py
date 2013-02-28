from IPython.config.configurable import Configurable
from IPython.utils.traitlets import Unicode, Int


class PNorm(Configurable):
    order = Int(2, config=True, help='Order of norm')
    
    def __init__(self, config):
        super(PNorm, self).__init__(config=config)
        print 'Loading up a pnorm, with order=%s' % order
