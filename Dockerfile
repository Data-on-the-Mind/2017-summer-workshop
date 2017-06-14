FROM jupyter/datascience-notebook

RUN conda install --yes r-psych r-afex r-lsmeans r-lme4 r-car r-broom r-purrr beautifulsoup4 selenium lxml nose
## FIXME: temporarily disable installation of rpy2 due to more complex build requirements
#RUN conda install --yes rpy2
RUN pip2 install dallinger==3.0.0
