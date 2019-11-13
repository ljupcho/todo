# todo app with docker
<br/>
First you would create a dir for this project and in it:</br>
1). clone the repo https://github.com/ljupcho/docker-nginx-python2-db-redis<br/>
2). clone your project https://github.com/ljupcho/todo<br/>
3). `cd ocker-nginx-python2-db-redis` && `./scripts/startup.sh` <br/>
This should create all the docker containers and set up everything, including insallation of the packages in requirements.txt files for both the web and consumers. they are set up with uwsgi with nginx proxy. using redis to store jobs/tasks for a the celery queue. docker-compose.yml file is the main file for building the docker services/containers.
<br/><br/>
The consumers are kept alive using supervisor that runs the celery worker commands.
Upon creating a task from the app a job/task is being dispached in redis and a consumer picks it up through the celery queue system. if change is made only restarting the consumer's docker container is enough with: `docker-compose restart consumers`
<br/>
You would access the app in browser with `http://localhost:8081/todolist/` and ports are exposed to mysql docker if case you would prefer to connect it manually on 3306. The uwsgi containers are exposed to 9000 port and redis on stardard 6379 port, make sure those are not taken as well. In the docker app there is .env file if you prefer to adjust the ports, version of some packages or database credentials.