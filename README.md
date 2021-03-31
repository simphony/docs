## Build Status
**latest** - [![Documentation latest](https://readthedocs.org/projects/simphony/badge/?version=latest)](https://simphony.readthedocs.io/en/latest/?badge=latest)  
**dev** - [![Documentation dev](https://readthedocs.org/projects/simphony/badge/?version=dev)](https://simphony.readthedocs.io/en/latest/?badge=dev)

# SimPhoNy docs
To access the documentation, please visit: [https://simphony.readthedocs.io](https://simphony.readthedocs.io).

If you find any error or problem with the documentation, please [create an issue](https://github.com/simphony/docs/issues).

## Local Installation
Installing the documentation locally will start a server that will generate the docs and
listen for changes in the source files. This can be done by using docker or installing the development environment directly on the you machine. Next are installation guides for Docker and a Linux OS.

### Docker

First, build the Docker image by running the following command:
```shell
$ docker build -t simphony-docs .
```

Then, start the program by running:
```shell
$ docker run --rm -v $PWD:/app -p 8000:8000 simphony-docs
```

### Linux
At an OS level (these commands work on Linux Debian):
```shell
$ sudo apt install pandoc graphviz
$ sudo apt-get install texlive-latex-recommended \
                       texlive-latex-extra \
                       texlive-fonts-recommended \
                       latexmk 
```
The python dependencies:
```shell
$ pip install -r requirements.txt
```

Now you can start the server and render the docs:
```
$ sphinx-autobuild docs/source docs/build/html
```
The documentation will be available on [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

To generate a PDF of the documentation, simply run (from the root project folder):
```sh
make -C docs latexpdf
```
The generated PDF can be found under docs/build/latex/SymPhoNy_docs.pdf