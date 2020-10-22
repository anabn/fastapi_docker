#!/bin/zsh

# number_of_worker=1
# host=0.0.0.0
# port=8000
# if [ $# -eq 0 ]; then
#     uvicorn app.main:app --reload --workers number_of_worker --host host --port post
# else
#     echo "error try again $@" 
# fi

# set -e
# sed -i "s|{{NGINX_HOST}}|$NGINX_HOST|;" \ 
#     /etc/nginx/conf.d/default.conf
# cat /etc/nginx/conf.d/default.conf
# exec "$@"