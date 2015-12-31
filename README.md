# rsquarelabs

[![Documentation Status](https://readthedocs.org/projects/rsquarelabs-core/badge/?version=dev)](http://docs.rsquarelabs.org/en/dev/?badge=dev)

This is the library of automation pipeline modules 

[Website](http://rsquarelabs.org) |
[Documentation](http://docs.rsquarelabs.org/) |
[Installation](http://docs.rsquarelabs.org/en/dev/install/) |
[Mailing List](https://groups.google.com/d/forum/rsquarelabs-core) |
[Gitter Chat](https://gitter.im/rsquarelabs/rsquarelabs-core) |


## Installing the package
`pip install rsquarelabs-core`

**we currently support python 2.7 only**

## Usage
```
#first: import package 
from rsquarelabs_core import gromacs

#second: call the method you want to execute
gromacs.create_water_box()

```



### Features 
1. Start a light weight webserver
2. commands for /usr/local/bin/







### Developers Notes 
1. bin/ - contains the scripts that can be moved to /usr/local/bin or /usr/bin
2. docs/ - contains the documentation of the tool
3. rsquarelabs_core/ - contains the tools/modules 
4. examples/ - sample usage scripts 


