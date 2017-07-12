FROM aculich/rockyter

MAINTAINER Aaron Culich / Berkeley Research Computing <brc+aculich@berkeley.edu>

## Please feel free to contact Berkeley Research Computing (BRC) if you have
## questions or if you want dedicated computational infrastructure if
## http://beta.mybinder.org/ does not provide enough power or if you need a
## dedicated resource for your own research or workshop.
##
## - http://research-it.berkeley.edu/brc
## - http://research-it.berkeley.edu/services/cloud-computing-support
##
## Contact: Aaron Culich <brc+aculich@berkeley.edu>

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
RUN conda install --yes r-data.table r-dt
RUN Rscript -e "install.packages('ggthemes', dependencies = TRUE, repos='http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('sjstats', dependencies = TRUE, repos='http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('xaringan', dependencies = TRUE, repos='http://cran.us.r-project.org')"

RUN conda install --yes r-afex==0.17_8
RUN pip2 install dallinger[data]==3.2.0

## installing r-mysql as a dependency for wordbankr triggers a long-standing bug
## with the Anaconda libreadline library which does not link against ncurses, so
## we will implement a crude workaround by copying the system libreadline over
## the conda one. ugly, but it is a workaround. See:
##   https://github.com/ContinuumIO/anaconda-issues/issues/152#
##   https://github.com/IRkernel/IRkernel/issues/204#issuecomment-148991153
#RUN conda install --yes r-rmysql
#RUN cp -p /lib/x86_64-linux-gnu/libreadline.so.6 /opt/conda/lib/libreadline.so.6 && \
#RUN Rscript -e "install.packages('wordbankr', dependencies = TRUE, repos='http://cran.us.r-project.org')"
RUN touch /tmp/testing
RUN conda install --yes            setuptools
RUN conda install --yes -n python2 setuptools
RUN ln -s $CONDA_DIR/envs/python2/bin/psiturk-install $CONDA_DIR/bin/psiturk-install && \
    ln -s $CONDA_DIR/envs/python2/bin/psiturk-server $CONDA_DIR/bin/psiturk-server && \
    ln -s $CONDA_DIR/envs/python2/bin/psiturk-setup-example $CONDA_DIR/bin/psiturk-setup-example && \
    ln -s $CONDA_DIR/envs/python2/bin/psiturk-shell $CONDA_DIR/bin/psiturk-shell

