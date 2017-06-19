FROM jupyter/datascience-notebook

RUN conda install --yes r-psych r-afex r-lsmeans r-lme4 r-car r-broom r-purrr beautifulsoup4 selenium lxml nose rpy2
RUN pip2 install dallinger==3.0.0 psiturk==2.2.1

ENTRYPOINT ["/bin/bash"]
