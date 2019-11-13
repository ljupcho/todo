# todo

First you would create a dir for this project and in it:
1). clone the repo https://github.com/ljupcho/docker-nginx-python2-db-redis
2). clone your project https://github.com/ljupcho/todo
3). cd todo && ./scripts/startup.sh 
This should create all the docker containers and set up everything, including insallation of the packages in requirements.txt files for both the web and consumers. they are set up with uwsgi with nginx proxy. using redis to store jobs/tasks for a the celery queue. docker-compose.yml file is the main file for building the docker services/containers.

The consumers are kept alive using supervisor that runs the celery worker commands.
Upon creating a task from the app a job/task is being dispached in redis and a consumer picks it up through the celery queue system. if change is made only restarting the consumer's docker container is enough with: `docker-compose restart consumers`