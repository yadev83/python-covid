# Python-Covid

[![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project is a CLI application that gives information about the covid-pandemic evolution in France through the use of a public API.

### Pre-requisite

To work with this project, you'll need...  

- Python 3.7 or above installed  
If you have Python installed and PiP ready, you can easily run the following command to install all the project dependencies at once :  
``pip install -r requirements.txt``  
On the other hand, you can install every requirement one by one :  
- The "requests" module installed for Python : ``pip install requests``  
- The "tabulate" module installed for Python : ``pip install tabulate``  

## To start the app

Just clone this repo and run  
``py src/app.py``  
and check that covid data !  

If you wish to run this app on a computer using windows without having a python installation, you can download a release package that contains an executable made out of the source code using py2exe. (WIP)  

## Made with

* [VS Code](https://code.visualstudio.com/) - A code editor that works well, made by Microsoft. Full of extensions made by the community, it supports a lot of languages, uses Git for merging and amending and a terminal is embedded in it.  
* [Py2exe](http://www.py2exe.org/) - An extension that allows python to build apps into windows executables. 
* [Doxygen](https://www.doxygen.nl/index.html) - An excellent tool for comments based documentation. It generates html content and a PDF.  

## Features  

* A basic help page when typing ``covid -h``  that gives help about all the commands of the app
* A main function that gives a table full of data about today's status in every dept when typing ``covid``  
* A table containing data for a specific dept when typing ``covid -dept <dpt_nb>``  
* A table for a specific date when typing ``covid -date <dd-mm-yyyy>``  

## Documentation  

Documentation for this project is available as a [website](https://yadev83.github.io/python-covid/index.html) or as a [pdf file](docs/reference_manual.pdf). All of it has been generated using Doxygen.  

## Versions
**Last Stable Version :** [1.0.2-d](https://github.com/yadev83/python-covid/releases/tag/v1.0.2-d)  
**Last Version :** [1.0.2-d](https://github.com/yadev83/python-covid/releases/tag/v1.0.2-d)  

Versions list : [Click here to see](https://github.com/yadev83/python-covid/tags)

_Versions are named like : Version M.m.p-state_  
_M is the major version number, m is the minor version number, p is the patch/hotfix number and state is the current version state, it could be : "d" -> dev, "a" -> alpha, "b" -> beta, nothing -> final product_

## Authors

* **Yanis ATTIA** _alias_ [@yadev83](https://github.com/yadev83)

## License

This project is under the ``GNU Public License (GPL) v3`` license - see the file [LICENSE.md](LICENSE.md) for more information

