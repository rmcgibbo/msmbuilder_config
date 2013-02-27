import os, sys
from IPython.config.application import Application
from IPython.utils.traitlets import Bool
from IPython.config.loader import (Config, PyFileConfigLoader,
    ConfigFileNotFound)
from IPython.utils.text import wrap_paragraphs, indent, dedent


class ConfigurationError(Exception):
    pass

class MSMBuilderApp(Application):
    #######################################################################
    # BEGIN options that need to be overridden in every subclass (subapp)
    #######################################################################
    name = None
    path = None
    short_description = None
    long_description = None
    subcommands = None
    #######################################################################
    # END options that need to be overridden in every subclass (subapp)
    #######################################################################
    config_file_paths = ['.']
    config_file_name = 'msmbuilder_config.py'
    
    display_banner = Bool(True, config=True,
        help="Whether to display a banner upon starting MSMBuilder."
    )
        
    def print_description(self):
        print self.short_description
        print self.long_description
        print ''
        
    def initialize(self, argv=None):
        super(MSMBuilderApp, self).initialize(argv)
        self.load_config_file()
        if self.display_banner:
            print 'DRAWING BANNER'

    def start(self):
        if self.subapp is not None:
            self.subapp.update_config(self.config)
            return self.subapp.start()
            

    def print_subcommands(self):
        if not self.subcommands:
            return
    
        lines = ["Subcommands"]
        lines.append('-'*len(lines[0]))
        for subc, (cls, help) in self.subcommands.iteritems():
            lines.append(subc)
            if help:
                lines.append(indent(dedent(help.strip())))
        lines.append('')
        
        print os.linesep.join(lines)
    
    
    def load_config_file(self, suppress_errors=True):
        """Load the config file.

        By default, errors in loading config are handled, and a warning
        printed on screen. For testing, the suppress_errors option is set
        to False, so errors will make tests fail.
        """
        self.log.debug("Searching path %s for config files", self.config_file_paths)
        base_config = 'msmbuilder_config.py'
        self.log.debug("Attempting to load config file: %s" %
                       base_config)
        try:
            Application.load_config_file(
                self,
                base_config,
                path=self.config_file_paths
            )
        except ConfigFileNotFound:
            # ignore errors loading parent
            self.log.debug("Config file %s not found", base_config)
            pass
        if self.config_file_name == base_config:
            # don't load secondary config
            return
        self.log.debug("Attempting to load config file: %s" %
                       self.config_file_name)
        try:
            Application.load_config_file(
                self,
                self.config_file_name,
                path=self.config_file_paths
            )
        except ConfigFileNotFound:
            # Only warn if the default config file was NOT being used.
            if self.config_file_specified:
                msg = self.log.warn
            else:
                msg = self.log.debug
            msg("Config file not found, skipping: %s", self.config_file_name)
        except:
            # For testing purposes.
            if not suppress_errors:
                raise
            self.log.warn("Error loading config file: %s" %
                          self.config_file_name, exc_info=True)


class RootApplication(MSMBuilderApp):
    name = 'msmb'
    path = 'base.MSMBuilderApp'
    short_description = ('MSMBuilder: Extensible software for building Markov'
        ' State Models for Biomolecular Conformational Dynamics')
    long_description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed nibh ut orci
suscipit scelerisque. Sed ligula augue, blandit ac eleifend eleifend, dapibus
ac sapien. Duis eu tortor ac erat porta vulputate. Phasellus ac nisl quis magna
eleifend tempor feugiat vehicula odio. Praesent porta, nunc vel eleifend 
elementum, sem justo dapibus massa, sed ultrices sapien felis nec urna. Praesent
et congue orci. Quisque diam turpis, volutpat vitae viverra at, sodales eget 
orci. Etiam et condimentum lectus. Nullam mollis egestas lobortis. Donec lorem 
odio, ullamcorper at imperdiet ut, commodo a neque. Suspendisse tristique ligula
nec tellus viverra rhoncus. Vivamus viverra, sapien at elementum congue, quam 
nibh egestas nulla, vitae convallis diam est at."""
    aliases = None

# def load_default_config():
#     """Load the default config file"""
#     cl = PyFileConfigLoader(default_config_file_name, '.')
#     try:
#         config = cl.load_config()
#     except ConfigFileNotFound:
#         # no config found
#         config = Config()
#     return config
