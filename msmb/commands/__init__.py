import os
import glob
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]

# from msmb.config.app import MSMBuilderApp
# from IPython.utils.traitlets import Unicode, Int, Enum
# 
# class Command(MSMBuilderApp):
#     name = "name"
#     path = 'msmb.commands.cluster.Cluster'
#     short_description = 'Short one line description.'
#     long_description = '''Long multinine description'''
