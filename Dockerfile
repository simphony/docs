FROM python:3.8-buster

RUN apt-get update
RUN apt-get install -y default-jre
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-latex-recommended \
                       texlive-latex-extra \
                       texlive-fonts-recommended \
                       latexmk

WORKDIR /app
ADD . .

RUN pip install -r requirements.txt

EXPOSE 5500

CMD python setup.py install && sphinx-reload --host 0.0.0.0 docs/
