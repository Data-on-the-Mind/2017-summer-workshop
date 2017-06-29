#!/bin/bash

## add default Jetstream user (uid:1000) to docker group so the user does not
## have to type `sudo docker` each time.
## https://www.explainxkcd.com/wiki/index.php/149:_Sandwich
JETSTREAM_USER=$(getent passwd 1000 | cut -d: -f1)
adduser $JETSTREAM_USER docker

## automatically install and enable byobu for the default Jetstream user
apt-get -y install byobu
sudo -u $JETSTREAM_USER -i /usr/bin/byobu-launcher-install

su -c "docker rm -f dotm; docker run --name dotm -d -p 80:8888 -p 1723:1723 -v $JETSTREAM_USER:/home/jovyan aculich/data-on-the-mind-2017-summer-workshop jupyter notebook --ip=* --NotebookApp.password=sha1:9274638cf4a5:6196ebab9550b728900b2de9b06d8ddea7e8b518" $JETSTREAM_USER
