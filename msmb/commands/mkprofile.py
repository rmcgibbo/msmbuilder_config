from msmb.config.app import MSMBuilderApp

class MKProfile(MSMBuilderApp):
    name = 'mkprofile'
    path = 'msmb.commands.mkprofile.MKProfile'
    short_description = 'Create a sample configuration file'
    long_description = ''
    
    def start(self):
        print self.generate_config_file()
        