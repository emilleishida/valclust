from distutils.core import setup


files = ["things/*"]

setup(name = "valclust",
    version = "0.1.0",
    description = "Clustering Validation and Analysis",
    author = "Vahid Mirjalili",
    author_email = "vmirjalily@gmail.com",
    url = "https://github.com/mirjalil/valclust",

    packages = ['valclust', 'valclust.ExternalValidity',
	],

    #package *needs* these files.
    package_data = {'valclust':[]},

    scripts = [],
    long_description = """

A collection of tools for validation and analysis of clutering solutions.

 Contact
=============

email: vmirjalily@gmail.com
Twitter: https://twitter.com/vmirly

URL for this project: https://github.com/mirjalil/valclust

""", 
    #classifiers = [],
    license='GPLv3',
    platforms='any',
) 


