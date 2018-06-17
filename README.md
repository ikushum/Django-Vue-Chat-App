# Django-Vue Live Chat

A Live Chat application built using Django and Vue.js. It uses Django's Channels which allows us to handle WebSocket protocol. In the frontend layer Vue.js uses WebSocket API to establish two-sided connection with the server. Users can create a chat room and invite multiple users to the chat room by sharing the room's URL.


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
Apply migrations
```sh
$ python3 manage.py migrate
```
For starting local dev server
```sh
$ python3 manage.py runserver
```
Navigate to ``` /chat ``` to create a new chat room

License
----
MIT
**Free Software, Hell Yeah!**


