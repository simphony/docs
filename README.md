## Build Status
**latest** - [![Documentation latest](https://readthedocs.org/projects/simphony/badge/?version=latest)](https://simphony.readthedocs.io/en/latest/?badge=latest)  
**dev** - [![Documentation dev](https://readthedocs.org/projects/simphony/badge/?version=dev)](https://simphony.readthedocs.io/en/latest/?badge=dev)

# SimPhoNy docs
To access the documentation, please visit: https://simphony.readthedocs.io/en/latest/

If you find any error or problem with the documentation, please [create an issue](https://github.com/simphony/docs/issues)

## Local Installation
 
For convenience, a Dockerfile has been created for setting up easily a local development environment for the docs.

First, build the Docker image by running the following command:
```shell
$ docker build -t simphony-docs .
```

Then, start the program by running:
```shell
$ docker run --rm -v $PWD:/app -p 8000:8000 simphony-docs
```

Alternatively, you can set up the development environment without using Docker. As as first step, some requirements have to be manually installed:
- [osp-core](https://github.com/simphony/osp-core)
- pandoc
- LaTeX requirements
  ```shell
  sudo apt install pandoc
  sudo apt-get install texlive-latex-recommended \
                     texlive-latex-extra \
                     texlive-fonts-recommended \
                     latexmk 
  ```

Then run the following command to render the documentation locally:
```
python3 setup.py install
```
This will create a new `build` folder under `./docs`. Now you can browse the rendered HTML files directly on your browser by simply opening the file `./docs/build/html/index.html`, or view the generated LaTeX document file by opening `docs/build/latex/SimPhoNy_docs.pdf`.