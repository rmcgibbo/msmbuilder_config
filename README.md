# msmbuilder_config

This is an experiment using the IPython configuration system for msmbuilder.


## installation
none.

## getting started

try playing around with all of the `-h` options
```
$ python msmb.py --help
$ python msmb.py --help-all
```

## code
- `base.py` contains code that sets up the configuration system. Basically some base classes
- `msmb.py` is the entry point script. the goal is to keep as little logic in here as possible.
- `app.py` current, all of the "scripts"/subcommands are in here. each subcommand is a class that
subclasses the same `MSMBuilderApp` base class.

- `msmbuilder_config.py` is a configuration file. Every configurable option can be set either in the file
or directly on the command line. If specified on the command line, it overrides what is listed in the file. Later
on, it's possible to search for the configuration files in different places -- maybe in the current directory or maybe
in your home directory or whatever. this is not a big deal.
