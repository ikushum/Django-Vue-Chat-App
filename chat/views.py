import json
from django.core import serializers
from django.shortcuts import render
from chat.models import Message
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'chat/chatRoomIndex.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/chatRoom.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'current_user': mark_safe( serializers.serialize('json', [ request.user ] ) ),
    })    

@login_required
def messages(request):
    return render(request, 'chat/messages.html', {  
    	'users':   mark_safe( serializers.serialize('json', User.objects.all() ) ),
    	'current_user': mark_safe( serializers.serialize('json', [ request.user ] ) ),
    	'messages': mark_safe( serializers.serialize('json', [] ) ),    	
    })

def message(request, selected_user):
	user1 = User.objects.get(pk=selected_user)
	user2 = User.objects.get(pk=request.user.pk)
	messages = Message.objects.filter(sender=user1, receiver=user2) | Message.objects.filter(sender=user2, receiver=user1)
	return render(request, 'chat/messages.html', {  
    	'users':   mark_safe( serializers.serialize('json', User.objects.all() ) ),
    	'current_user': mark_safe( serializers.serialize('json', [ request.user ] ) ),
    	'selected_user': mark_safe( serializers.serialize('json', [ User.objects.get(pk=selected_user) ] ) ),
    	'messages': mark_safe( serializers.serialize('json', messages.order_by('created_at') ) ),
		})   