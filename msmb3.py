from base import MSMBuilderApp, RootApplication

# import all of the apps
from app import *

# register all of the apps as subcommands
subcommands = {}
for subclass in MSMBuilderApp.__subclasses__():
    if subclass.name in subcommands:
        msg = ('subcommand %s is not unique. you need to override'
               ' it in your new subclass' % subclass.name)
        raise ConfigurationError(msg)
    if subclass != RootApplication:
        subcommands[subclass.name] = (subclass.path,  subclass.short_description)
RootApplication.subcommands = subcommands


if __name__ == '__main__':
    app = RootApplication.instance()
    app.initialize()
    app.start()