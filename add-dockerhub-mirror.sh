#!/bin/bash
set -e

DOCKER_DAEMON_FILE="/etc/docker/daemon.json"

# Docs: https://mirror.iranserver.com/docker/

echo -e "Updating your Docker registry to docker.iranserver.com mrirror ...\n"

if [ ! -f "$DOCKER_DAEMON_FILE" ]; then
  echo -e "Creating your docker daemon config file ...\n"
  touch /etc/docker/daemon.json
fi

echo -e "Backuping your current /etc/docker/daemon.json file into the /etc/docker/daemon.json.old ...\n"
sudo cp /etc/docker/daemon.json /etc/docker/daemon.json.old


sudo bash -c "cat <<EOT > $DOCKER_DAEMON_FILE
{
  "registry-mirrors": [\"https://docker.iranserver.com\"]
}
EOT"

echo -e "Restarting your docker daemon ...\n"
sudo systemctl daemon-reload
sudo systemctl restart docker

echo -e "Done! for test: 'docker run hello-world'\n"
