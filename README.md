# msmbuilder_config

This is an experiment using the IPython configuration system for msmbuilder.


## installation
none.

## getting started

```
$ python msmb.py --help
```

## code
- `base.py` contains code that sets up the configuration system. Basically some base classes
- `msmb.py` is the entry point script. the goal is to keep as little logic in here as possible.
- `app.py` current, all of the "scripts"/subcommands are in here. each subcommand is a class that
subclasses the same `MSMBuilderApp` base class.
