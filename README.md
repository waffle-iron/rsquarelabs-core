# rsquarelabs-core

[![Build Status](https://travis-ci.org/rsquarelabs/rsquarelabs-core.svg?branch=dev)](https://travis-ci.org/rsquarelabs/rsquarelabs-core)
[![Requirements Status](https://requires.io/github/rsquarelabs/rsquarelabs-core/requirements.svg?branch=dev)](https://requires.io/github/rsquarelabs/rsquarelabs-core/requirements/?branch=dev)

![rsquarelabs-core hero ](_docs/images/rsquarelabs-hero.jpg)

This is the library of automation pipeline modules

[Website](http://rsquarelabs.org) |
[Documentation](https://github.com/rsquarelabs/rsquarelabs-core/wiki/) |
[Installation](https://github.com/rsquarelabs/rsquarelabs-core/wiki/en/dev/install/) |
[Mailing List](https://groups.google.com/d/forum/rsquarelabs-core) |
[Gitter Chat](https://gitter.im/rsquarelabs/rsquarelabs-core)


## Summary
- [**Install**](#install)
- [**Features**](#features)
- [**Usage**](#usage)
- [**Why rsquarelabs-core?**](#why-rsquarelabs-core)
- [**Community**](#community)
- [**Roadmap**](#roadmap)
- [**Support**](#support)
- [**License**](#license)


## Install
```
pip install rsquarelabs-core
```
**we currently support python 2.7 only**

## Usage
```
# first: import the class that does protein-ligand minimisation
from rsquarelabs_core.engines.gromacs import ProteinLigMin

# Create and object with input files 
obj = ProteinLigMin(
    ligand_file='ligand.gro',
    ligand_topology_file='ligand.itp',
    protein_file='protein.pdb',
    working_dir='./',
    verbose=True,
    quiet=False
)

# call the method you want to start with
obj.create_topology()
obj.prepare_system()
obj.write_em_mdp()
obj.add_ions()
obj.write_emreal_mdp()
obj.minimize()

 

```

## Features
1. Start a light weight webserver
2. commands for /usr/local/bin/

## Why rsquarelabs-core
1. scaffolding the project
2. project management
3. Tracking the project via webclient


## Community
Want to join an open source project? Now it's your chance!

Don't know what you want to help out with? Well here are some areas that we could use help with:

- rsquarelabs-core scientific thoughts,
- rsquarelabs-core [technical stack](_docs/notes/technical-stack.md)
- rsquarelabs-core code - see [milestones](https://github.com/rsquarelabs/rsquarelabs-core/milestones) and [issues](https://github.com/rsquarelabs/rsquarelabs-core/issues) for more
- rsquarelabs-core [documentation](https://github.com/rsquarelabs/rsquarelabs-core/wiki), [tutorials](https://github.com/rsquarelabs/rsquarelabs-core/wiki/Tutorials) and [examples](https://github.com/rsquarelabs/rsquarelabs-core/wiki/Examples)
- rsquarelabs-core [website](http://rsquarelabs.org)
- If you want to join our community as a contributor, please leave a message as [@rrmerugu](https://twitter.com/rrmerugu)



## RoadMap
You can find a detailed Roadmap of rsquarelabs-core [here](https://github.com/rsquarelabs/rsquarelabs-core/milestones).

## Support
We support universties and research labs to install, configure and setup rl-core

## License
