## Week 2 - Orchestration with Kestra

### Quick way to install Kestra
$ docker run --pull=always --rm -it -p 8080:8080 --user=root \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp:/tmp kestra/kestra:latest server local

After that you can wite on your browser: **localhost:8080** and you are redirected
to a new instance of Kestra.  
With the quick installation, if you kill the container you loose the flows. Therefore if
you restart the container your jobs are not saved.

### Install Kestra using docker compose

1. Download the docker-compose.yaml file
```
curl -o docker-compose.yaml \
https://raw.githubusercontent.com/kestra-io/kestra/develop/docker-compose.yml
```
2. In bash execute ```docker compose build```in the same folder where you have the docker-compose.yaml
3. Run in bash ```docker compose up```
4. In browser: ```localhost:8080```

###  Different images of kestra in docker
visit: ```hub.docker.com/kestra/kestra/tags```
The recommended tag (version) is **latest**, that is the tag we used in our docker-compose.yaml