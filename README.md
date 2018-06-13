# Django-Vue Live Chat

A Live Chat application build using Django and Vue.js. It uses Django's Channels which allows us to handle WebSocket protocol. It thr frontend layer Vue.js uses WebSocket API to establish two-sided connection with the server.

### Installation

Make sure to have python3, pip3 and redis installed properely on your machine.

Install dependencies using
```sh
$ pip3 install -r requirements.txt
```
Start a redis server on port 6379
```sh
$ echo "port 6379" | redis-server -
```
For starting local dev server
```sh
$ python3 manage.py runserver-
```

License
----
MIT
**Free Software, Hell Yeah!**


