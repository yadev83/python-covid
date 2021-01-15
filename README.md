# Python-Covid

[![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project is a CLI application that gives information about the covid-pandemic evolution in France through the use of a public API.

### Pre-requisite

To work with this project, you'll need...  

- Python 3.7 or above installed  
If you have Python installed and PiP ready, you can easily run the following command to install all the project dependencies at once :  
``pip install -r requirements.txt``  
On the other hand, you can install every requirement one by one even though I don't recommend it to avoid errors :  
- The "requests" module installed for Python    : ``pip install requests``  
- The "tabulate" module installed for Python    : ``pip install tabulate``  
- The "xlwt" module installed for Python        : ``pip install xlwt``

## To start the app

Just clone this repo and run  
``py src/app.py``  
and check that covid data !  

If you wish to run this app on a computer using windows without having a python installation, you can download a release package that contains an executable made out of the source code using py2exe and simply run the "app.exe" file contained in it.  

You can also build your own binaries out of the source code using the setup.py file in the root folder of the project.  
Simply run  ``pip install py2exe`` to install the "compiler". Py2Exe bundles your app in an exe file with the python interpreter, making it easy to run a python app on a windows machine that doesn't have python installed.  
Then place yourself in the root folder of the project and run ``python setup.py py2exe``. A "dist" folder will be created containing an "app.exe" executable file that contains the covid CLI.  

## Made with

* [VS Code](https://code.visualstudio.com/) - A code editor that works well, made by Microsoft. Full of extensions made by the community, it supports a lot of languages, uses Git for merging and amending and a terminal is embedded in it.  
* [Py2exe](http://www.py2exe.org/) - An extension that allows python to build apps into windows executables. 
* [Doxygen](https://www.doxygen.nl/index.html) - An excellent tool for comments based documentation. It generates html content and a PDF.  

## Features  

* A basic help page when typing ``covid -h``  that gives help about all the commands of the app
* A main function that gives a table full of data about today's status in every dept when typing ``covid``  
* A table containing data for a specific dept when typing ``covid --department <dpt_nb>``  
* A table for a specific date when typing ``covid --date <yyyy-mm-dd>``  
* It is possible to output everything to an excel file when typing ``covid --excel <my-output-file-name>``    

## Documentation  

Documentation for this project is available as a [website](https://yadev83.github.io/python-covid/index.html) or as a [pdf file](docs/reference_manual.pdf). All of it has been generated using Doxygen.  

## Versions
**Last Stable Version :** [1.1.0](https://github.com/yadev83/python-covid/releases/tag/v1.1.0)  
**Last Version :** [1.1.0](https://github.com/yadev83/python-covid/releases/tag/v1.1.0)  

**1.1.0 :** The first stable production version that contains a built executable for the covid CLI  
**1.0.2-d :** This version is only for the README file. It now links to the stable version and last version of the project  
**1.0.1-d :** First version. Calls all data for testing purposes.  

Versions list : [Click here to see](https://github.com/yadev83/python-covid/tags)  

## Authors

* **Yanis ATTIA** _alias_ [@yadev83](https://github.com/yadev83)

## License

This project is under the ``GNU Public License (GPL) v3`` license - see the file [LICENSE.md](LICENSE.md) for more information

