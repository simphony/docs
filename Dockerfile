FROM python:3.8-buster

RUN apt-get update
RUN apt-get install -y pandoc default-jre graphviz
RUN apt-get install -y texlive-latex-recommended \
                       texlive-latex-extra \
                       texlive-fonts-recommended \
                       latexmk

WORKDIR /app
ADD . .

RUN pip install -r requirements.txt

CMD sphinx-autobuild --host 0.0.0.0 docs/source docs/build/html

# Build:
# $ docker build -t simphony-docs .

# Run:
# $ docker run --rm -v $PWD:/app -p 8000:8000 simphony-docs
