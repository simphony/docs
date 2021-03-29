FROM python:3.8-buster

RUN apt-get update
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-latex-recommended \
                       texlive-latex-extra \
                       texlive-fonts-recommended \
                       latexmk

WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

CMD python setup.py install
