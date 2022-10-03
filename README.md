The singularity folder contains a definition file and instructions to install psrchive compatible with python3.
If you just want to add the possibility to use psrchive with python3 or make the install yourself, the instructions are below.

## How to install psrchive on python 3

If you don't have psrchive installed, we would recommend you to follow the very complete explanation [here on psrchive installation guide](https://psrchive.sourceforge.net/installation.shtml)

Here, we suppose that psrchive is working fine, and if you are reading this it means you want to use psrchive on python3.  Unfortunately, i'm still trying to figure out how to make it work for both, it's somehow related to PATH and environnment variable. Let's keep this simple ; you won't be able to use both at the same time by adding the path of your python2 and python3 lib to the PYTHONPATH because there is a conflict between the versions and python tries to load the first psrchive.py it finds. It means that if you put python3 path before the python2, it will try to use the python3 psrchive.py EVERYTIME, even if you're under python2.
**edit** :
You can manage your path by using a .pth file that your pythonX will use to check which libaries and directories to use. 

**BUT**

You still can use either python2 and python 3 by just import the lib at the beggining of your script/notebook/ipython environnment.
Just add these few lines and should be ok.

```
import sys

sys.path.insert(1,'path/to/your/pythonX/')
```
Usually, the path is $ASTROSOFT/lib/python2.7/site-packages/ (or python3.6) where $ASTROSOFT is the variable environment for your pulsar software directory. Otherwise try to locate the psrchive.py and use the resulting location.


#### Set up your PYTHONPATH and VE to install
```
# PYTHON PATH
export PYTHONPATH=/usr/lib/python3.6/:$ASTROSOFT/lib/python3.6/site-packages
```
Verify that you have swig3.0 installed and add its path to your .bashrc
```
export SWIG=path/to/swig3.0
```


#### Libraries
To install psrchive python3 you should have these libraries (on python3 not python2!)

 - swig3
 - python3-dev
 - python3-numpy
 - python3-scipy
 - python3-matplotlib
 - ipython3
 - python3-sympy
 - python3-nose

Use apt-get install and set up $SWIG by its location, because psrchive will use this variable to choose the correct swig version, the swig2 won't work.

#### Configure PSRCHIVE
```
./configure F77=gfortran --prefix=$ASTROSOFT --enable-shared CFLAGS=-fPIC FFLAGS=-fPIC
```

It should work, but verify by trying to import psrchive on python3 and test it. (See datatest folders for some data, and the python script for some tests.)
