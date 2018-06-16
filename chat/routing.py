from django.conf.urls import url

from . import groupChatConsumers, privateChatConsumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', groupChatConsumers.GroupChatConsumer),
    url(r'^ws/chat/(?P<chat_token>[^/]+)/$', privateChatConsumers.PrivateChatConsumer),    
]
