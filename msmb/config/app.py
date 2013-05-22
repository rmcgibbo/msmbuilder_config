"""Base class for MSMBuilder commands
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from __future__ import print_function
# stdlib imports
import os

# ipython imports
from IPython.config.application import Application
from IPython.utils.traitlets import Bool
from IPython.utils.text import indent, dedent, wrap_paragraphs, marquee
from IPython.config.loader import ConfigFileNotFound

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------


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
    reference = None
    subcommands = None
    #######################################################################
    # END options that need to be overridden in every subclass (subapp)
    #######################################################################

    config_file_name = 'msmbuilder_config.py'
    option_description = u''

    display_banner = Bool(True, config=True,
        help="Whether to display a banner upon starting MSMBuilder.")

    def print_description(self):
        "Print the application description"
        lines = []
        lines.append(self.short_description)
        lines.append('='*len(self.short_description))
        lines.append('')

        if self.long_description:
            for l in wrap_paragraphs(self.long_description):
                lines.append(l)
                lines.append('')

        if self.reference:
            lines.append('Reference\n---------')
            for l in wrap_paragraphs(self.reference):
                lines.append(l)
                lines.append('')

        print(os.linesep.join(lines))

    def initialize(self, argv=None):
        """Do the first steps to configure the application, including
        finding and loading the configuration file"""
        # load the config file before parsing argv so that
        # the command line options override the config file options
        self.load_config_file()
        super(MSMBuilderApp, self).initialize(argv)
        #if self.display_banner:
        #    print('DRAWING MSMBUILDER BANNER')
        #    print('PLEASE CITE US?')

    def load_config_file(self):
        try:
            super(MSMBuilderApp, self).load_config_file(self.config_file_name,
                                                        config_file_paths())
            self.log.info('Config file loaded.')
        except ConfigFileNotFound:
            self.log.warning('No config file was found. I searched in %s' %
                ', '.join(config_file_paths()))

    def print_subcommands(self):
        """Print the list of subcommands under this application"""

        if not self.subcommands:
            return

        lines = ["Subcommands"]
        lines.append('-'*len(lines[0]))
        for subc, (cls, help) in self.subcommands.iteritems():
            lines.append(subc)
            if help:
                lines.append(indent(dedent(help.strip())))
        lines.append('')

        print(os.linesep.join(lines))

    def print_options(self):
        if not self.flags and not self.aliases:
            return
        lines = ['Options']
        lines.append('-'*len(lines[0]))
        print(os.linesep.join(lines))
        self.print_flag_help()
        self.print_alias_help()
        print()


class RootApplication(MSMBuilderApp):
    name = 'msmb'
    path = 'base.MSMBuilderApp'
    short_description = ('MSMBuilder: Software for building Markov '
                         'State Models for Biomolecular Dynamics')
    long_description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed nibh ut orci
suscipit scelerisque. Sed ligula augue, blandit ac eleifend eleifend, dapibus
ac sapien. Duis eu tortor ac erat porta vulputate. Phasellus ac nisl quis magna
eleifend tempor feugiat vehicula odio. Praesent porta, nunc vel eleifend
elementum, sem justo dapibus massa, sed ultrices sapien felis nec urna.
Praesent et congue orci. Quisque diam turpis, volutpat vitae viverra at,
sodales eget orci. Etiam et condimentum lectus. Nullam mollis egestas lobortis.
Donec lorem odio, ullamcorper at imperdiet ut, commodo a neque. Suspendisse
tristique  ligula nec tellus viverra rhoncus. Vivamus viverra, sapien at
elementum congue, quam nibh egestas nulla, vitae convallis diam est at."""

    def start(self):
        """Start the application's main loop.

        This will be overridden in subclasses"""
        if self.subapp is not None:
            return self.subapp.start()
        else:
            # if they don't choose a subcommand, display the help message
            self.parse_command_line('--help')
    
    def initialize(self, argv=None):
        super(RootApplication, self).initialize(argv)
        if self.display_banner:
            print('DRAWING MSMBUILDER BANNER')
            print('PLEASE CITE US?')

#-----------------------------------------------------------------------------
# Utility functions
#-----------------------------------------------------------------------------

def collect_subcommands():
    """Collect all of the subclasses of `MSMBuilderApp` that have been
    imported

    Returns
    -------
    subcommands : dict
        The keys in the dict are the `name` field of the subclass, and the
        values are the `path` field and the `short_description`.

    Examples
    --------
    >>> from msmb.commands import *
    >>> application.subcommands = collect_subcommands()
    """
    subcommands = {}
    for subclass in MSMBuilderApp.__subclasses__():
        if subclass.name in subcommands:
            msg = ('subcommand %s is not unique. you need to override'
                   ' it in your new subclass' % subclass.name)
            raise ConfigurationError(msg)
        if subclass != RootApplication:
            subcommands[subclass.name] = (subclass.path,
                                          subclass.short_description)
    return subcommands


def config_file_paths():
    """Get a list of paths where the msmbuilder_config.py file might be found
    """

    return ['.', os.path.expanduser('~/.msmbuilder')]
