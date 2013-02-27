# msmbuilder_config

This is an experiment using the IPython configuration system for msmbuilder.


## installation
```
$ python setup.py install
```
This will install a single script named `msmb`.

## getting started

Try playing around with all of the `-h` options.
```
$ msmb --help
$ msmb --help-all
```

## code
- `msmb/config/app.py` contains code that sets up the configuration system.
Basically some base classes.
- `msmb/scripts/msmb` is the entry point script. The goal is to keep as
little logic in here as possible.
- `msmb/commands/` is where all the "scripts"/subcommands are. Each
subcommand is a class that subclasses the same `MSMBuilderApp` base class.
- `msmbuilder_config.py` is a configuration file. Every configurable option
can be set either in the file or directly on the command line. If specified
on the command line, it overrides what is listed in the file. Later on, it's
possible to search for the configuration files in different places -- maybe
in the current directory or maybe in your home directory or whatever. This
is not a big deal.
