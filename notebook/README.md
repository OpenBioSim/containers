# notebook container

This container is used by try.openbiosim.org jupyterhub service
to allow people to easily start a jupyter lab session with 
sire, BioSimSpace and all associated tools pre-loaded.

$ docker build --platform linux/x86-64 -t openbiosim/notebook:latest -t openbiosim/notebook:2023.1.0beta .

$ docker push openbiosim/notebook:latest

