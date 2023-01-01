#!/bin/bash

# Docs: https://mirror.iranserver.com/docker/

echo -e "Updating your Docker registry to docker.iranserver.com mrirror ...\n"

echo -e "Backuping your current /etc/docker/daemon.json file into the /etc/docker/daemon.json.old ...\n"
sudo cp /etc/docker/daemon.json /etc/docker/daemon.json.old

sudo cat <<EOT > /etc/docker/daemon.json
{
  "registry-mirrors": ["https://docker.iranserver.com"]
}
EOT

echo -e "Restarting your docker daemon ...\n"
sudo systemctl restart docker

echo -e "Done! for test: 'docker run hello-world'\n"
