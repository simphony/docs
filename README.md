# SimPhoNy documentation

To access the documentation, please visit:
[https://simphony.readthedocs.io](https://simphony.readthedocs.io/en/v4.0.0/).

If you find any error or problem with the documentation,
please [create an issue](https://github.com/simphony/docs/issues).

## Local rendering

### HTML

Start a server, generate the docs and listen for changes in the source files.
This can be done by using docker or installing the development environment
directly on your machine. Next are installation guides for Docker and Linux.

#### Docker

First, build the Docker image by running the following command:

```shell
$ docker build -f local_build.Dockerfile -t simphony-docs .
```

Then, start the program by running:

```shell
$ docker run --rm -v $PWD:/app -p 8000:8000 --name simphony-docs simphony-docs
```

#### Linux

At an OS level (these commands work on Linux Debian):

```shell
$ sudo apt install pandoc graphviz default-jre
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
$ sphinx-autobuild docs build
```

The documentation will be available on
[`http://127.0.0.1:8000`](http://127.0.0.1:8000).

### PDF (LaTeX)

To generate a PDF of the documentation, simply run (from the root project
folder):

```sh
make -C docs latexpdf
```

The generated PDF can be found under build/latex/SymPhoNy_docs.pdf
