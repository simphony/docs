[![pipeline status](https://gitlab.cc-asp.fraunhofer.de/simphony/getting-started/badges/master/pipeline.svg)](https://gitlab.cc-asp.fraunhofer.de/simphony/getting-started/commits/master)

# SimPhoNy docs
To access the documentation, please visit: http://simphony.pages.fraunhofer.de/documentation

If you find any error or problem with the documentation, please [create an issue](https://gitlab.cc-asp.fraunhofer.de/simphony/documentation/issues)

## Local installation
If you want to render the documentation locally, you can install the current project via:
```
python3 setup.py install
```
As usual, we recommend using a virtual environment.

This will install the main requirements via `pip`.

However, other requirements must be manually installed:
- [osp-core](https://gitlab.cc-asp.fraunhofer.de/simphony/osp-core)
- pandoc `sudo apt install pandoc`

Once everything is installed, you can go to the docs folder and run `make`
```
cd docs
make html
```
_Note:_ use `make.bat html` in windows

### LaTeX pdf
You can also render the documentation as a LaTeX pdf.
For that, you should install some extra requirements:
```
sudo apt-get install texlive-latex-recommended \
                     texlive-latex-extra \
                     texlive-fonts-recommended \
                     latexmk 
```
Once everything is installed, you can go to the docs folder and generate the pdf
```
cd docs
make latexpdf
```
The generated file will be in `docs/build/latex/SimPhoNy_docs.pdf`