[![pipeline status](https://gitlab.cc-asp.fraunhofer.de/simphony/documentation/badges/master/pipeline.svg)](https://gitlab.cc-asp.fraunhofer.de/simphony/documentation/commits/master)

# SimPhoNy docs
To access the documentation, please visit: http://simphony.pages.fraunhofer.de/documentation/latest

If you find any error or problem with the documentation, please [create an issue](https://gitlab.cc-asp.fraunhofer.de/simphony/documentation/issues)

## Local installation
First, some requirements have to be manually installed:
- [osp-core](https://gitlab.cc-asp.fraunhofer.de/simphony/osp-core)
- pandoc
- LaTeX requirements
  ```shell
  sudo apt install pandoc
  sudo apt-get install texlive-latex-recommended \
                     texlive-latex-extra \
                     texlive-fonts-recommended \
                     latexmk 
  ```


If you want to render the documentation locally, you can run:
```
python3 setup.py build_sphinx
```

This will render the html and generate a LaTeX pdf (in `docs/build/latex/SimPhoNy_docs.pdf`).