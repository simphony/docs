
# SimPhoNy docs
To access the documentation, please visit: https://simphony-docs.readthedocs.io/en/latest/

If you find any error or problem with the documentation, please [create an issue](https://github.com/simphony/docs/issues)

## Local installation
First, some requirements have to be manually installed:
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


If you want to render the documentation locally, you can run:
```
python3 setup.py install
```

This will render the html and generate a LaTeX pdf (in `docs/build/latex/SimPhoNy_docs.pdf`).