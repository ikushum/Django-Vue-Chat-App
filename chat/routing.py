from django.conf.urls import url

from . import groupChatConsumers, privateChatConsumers

websocket_urlpatterns = [
    url(r'^group_chat/ws/(?P<room_name>[^/]+)/$', groupChatConsumers.GroupChatConsumer),
    url(r'^private_chat/ws/(?P<chat_token>[^/]+)/$', privateChatConsumers.PrivateChatConsumer),
]
