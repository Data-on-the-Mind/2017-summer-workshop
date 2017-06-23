FROM aculich/rockyter

RUN conda install --yes r-psych r-afex r-lsmeans r-lme4 r-car r-broom r-purrr

RUN conda install --yes            beautifulsoup4 selenium lxml nose rpy2
RUN conda install --yes -n python2 beautifulsoup4 selenium lxml nose rpy2

RUN pip2 install dallinger==3.0.0 psiturk==2.2.1
RUN ln -s $CONDA_DIR/envs/python2/bin/psiturk $CONDA_DIR/bin/psiturk && \
    ln -s $CONDA_DIR/envs/python2/bin/dallinger $CONDA_DIR/bin/dallinger

RUN wget https://github.com/DaveVinson/cmscu-tutorial/raw/master/cmscu.tar.gz && \
    R CMD INSTALL cmscu.tar.gz

RUN pip  install twitter && \
    pip2 install twitter

USER root
RUN apt-get update && apt-get install --yes xvfb
USER $NB_USER

RUN conda install --yes            pyvirtualdisplay xvfbwrapper
RUN conda install --yes -n python2 pyvirtualdisplay xvfbwrapper
RUN conda install --yes r-rjson r-formatr
