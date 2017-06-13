FROM jupyter/datascience-notebook

RUN conda install --yes r-psych r-afex r-lsmeans r-lme4 r-car r-broom r-purrr beautifulsoup4 selenium lxml rpy2 nose
RUN pip2 install dallinger==3.0.0
