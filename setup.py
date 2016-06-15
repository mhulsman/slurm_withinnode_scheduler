import sys
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup,find_packages,Extension
import distutils.sysconfig
import os
import os.path

setup(
    name="XSlurm",
    version="0.1",
    scripts = ['xsqueue', 'xsbatch', 'xscancel','xslurm','xslurm_chief','slurm_to_xslurm'],
     install_requires=['numpy>=1.4.1','psutil','dnspython'],
     py_modules=['xslurm_shared'],
     author = "M. Hulsman",
     author_email = "m.hulsman@tudelft.nl",
     description = "XSlurm is a batch system on top of SLURM, which allows for core-level scheduling on systems that only allow  node-level scheduling.",
     license = "LGPLv2.1",

)

