# Code-Samples

Set of new coding libraries and frameworks involves some basic concepts 
understanding and configuration. 

The configuration is not always an easy and obvious task. Thus, here I will 
put working and checked configurations.

Additionally, most new libraries involve some code prototyping to learn the 
basic ideas behind their functioning. **Code_samples** is where the concepts 
are gathered.  
 
This project subsequent folders contain code samples for tools that I have 
approached and configurations that have proven to be working.

Below are instructions to prepare environment:

#### PyEnv
To install and switch arbitrary python version as well as conda one can use: https://github.com/pyenv/pyenv
Installing with dedicated script: https://github.com/pyenv/pyenv-installer

#### Python3
0. Find installed python versions: `whereis python`
1. Install Python3 on your linux distro. Ubuntu 16.04 LTS+ ship with both 
Python 3 and Python 2 pre-installed
2. Test default python version if any: 
 ``` bash
 $ python -V
Python 2.7.12
```
If the default version is `2.x` use `python3` command to use version 3.
``` 
$ python3 -V 
Python 3.5.2 
```
3. Install **PIP** - package manager for python3 dedicated libs, frameworks etc.
```sudo apt-get install -y python3-pip```

##### Python 3 - VirtualEnv
VirtualEnv is a way to create isolated running and package configuration that
is separate form system-wide python installs. Here are steps to create own 
virtual env:

1. Install for Python 3.x dev package and the virtual env package
```bash
 $ sudo apt-get install python3-dev python-virtualenv # for Python 3.n
 ```
2. VirtEnv is a directory where the specific packages are going to be stored:
    * make the dir: `mkdir myVEdir`
    * install VE with Python3, that inherits the packages already installed 
    system-wide e.g. in `/usr/lib/python2
    .7/site-packages`
     
        ```$ virtualenv --system-site-packages -p python3 <path/to/myVEdir> ```
     
        If you want isolation from the global system, do not use 
        `--system-site-packages` flag.
3. **Activate** the virtualenv:

```
$ source <path/to/myVEdir>/bin/activate$
(myVEdir)$
```
Now you can see that:
```
(myVEdir)$ which python
<path/to/myVEdir>/bin/python
(myVEdir)$ python -V
Python 3.5.2
```
    
   * To **deactivate VE**: `(myVEdir)$ deactivate`
   * To **remove VE**: `rm -rf <path/to/myVEdir>`
   
4. Install `pip` for VE `(myVEdir)$ easy_install -U pip`

    * check `pip` version in VE: `pip list | grep pip`
    * find pip packages and versions: `pip freeze`
        * only packages that are in VE (ie. not inherited from system): `pip 
        freeze --local`
        
5. To develop a code from eg. GitHub cloned repo use local package: 
Python `setup.py install` is used to install (typically third party) packages 
that you're not going to be developing/editing/debugging yourself. <br />
For your own stuff, you want to get your package installed and then be able 
to frequently edit your code and not have to re-install your package—this is 
exactly what python `setup.py develop` does: installs the package (typically 
just a source folder) in a way that allows you to conveniently edit your 
code after its installed to the (virtual) environment and have the changes 
take effect immediately. <br />
Note that it is highly recommended to rather use:
 * `pip install .` (install) and 
 * `pip install -e <path>` (developer install) to install packages from path 
 (or from [remote repo](https://packaging.python.org/tutorials/installing-packages/#installing-from-vcs)),
  as invoking`setup.py` directly will do the wrong things for many 
  dependencies like pulling prereleases and incompatible packages versions 
  and make the package hard to uninstall with pip. <br /> <br />
Difference: `pip install -e` uses wheel while `python setup.py develop`
doesn't use it. <br /> <br />
With install, you could achieve the same behavior by using `pip install -e 
/path/to/package --no-use-wheel`

Now, to use any of the subdirectories' tools, just increment their included 
README instructions to test the attached python code or Jupyter notebook (`
.ipynb`) files. To use Jupter first refer to its dedicated
[instructions](Jupyter/README.md).

---
###### LICENSING
Code: AGPL-3.0 Content:
[![CC-by-SA-4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)


