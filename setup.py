from distutils.core import setup


files = ["things/*"]

setup(name = "valclust",
    version = "0.1.7",
    description = "Clustering Validation and Analysis",
    author = "Vahid Mirjalili",
    author_email = "vmirjalily@gmail.com",
    url = "https://github.com/mirjalil/valclust",

    packages = ['valclust', 'valclust.InternalValidity',
	'doc', 'tests'],

    #package *needs* these files.
    package_data = {'valclust':[]},
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
	"Intended Audience :: Information Technology",
	"Operating System :: OS Independent",
    ],

    scripts = [],
    long_description = """

A collection of tools for validation and analysis of clustering results.

Currently Supported:  
   * Summary Statistics of Clustering: singletons, cluster sizes
   * Internal Indecies: Inter \& Intra Pairwise Distance Sampling
   * External Validation:  Purity, NMI, MCC, Binary Contingency


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


