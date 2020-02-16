# flask-uwsgi-nginx
## Setup

`docker run -p 80:80 registry.gitlab.com/sleepless-se/flask-uwsgi-nginx`

## Test
Access 
http://localhost

You can see `Welcome to Flask!`

## Develop

You can focus to develop your flask application. Because this project has already worked at localhost:80 with uwsgi and nginx, You never mind about it.

1. Clone repository `git clone git@gitlab.com:sleepless-se/flask-uwsgi-nginx.git`
1. Edit `flask-uwsgi-nginx/api.py` as you want.

That's it!


## Build Push

1. `docker build -t HUB_USER/REPO_NAME:TAG .`
1. `docker push HUB_USER/REPO_NAME:TAG`

