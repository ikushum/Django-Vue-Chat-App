from django.conf.urls import url

from . import groupChatConsumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', groupChatConsumers.GroupChatConsumer),
]
