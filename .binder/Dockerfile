FROM python:3.10-bullseye


ENV DEBIAN_FRONTEND=noninteractive


# Install required packages: Jupyter and packages required to run notebooks.
RUN apt-get -qq update && \
    apt-get install --yes --no-install-recommends \
    jupyter-notebook python3-jupyterlab-server \
    wget \
    graphviz ffmpeg python3-lammps && \
    apt-get -qq purge && \
    apt-get -qq clean && \
    rm -rf /var/lib/apt/lists/*


# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

# Add ~/.local/bin to PATH
ENV PATH="${HOME}/.local/bin:${PATH}"


# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install simlammps ontology
RUN wget https://raw.githubusercontent.com/simphony/simlammps/main/simphony_osp_simlammps/simlammps.ttl
RUN wget https://raw.githubusercontent.com/simphony/simlammps/main/simphony_osp_simlammps/simlammps.yml
RUN pico install simlammps.yml

# Install city and emmo ontologies
RUN pico install city emmo
