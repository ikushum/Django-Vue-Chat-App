from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User
from django.core import serializers

@login_required
def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })    

@login_required
def messages(request):
    return render(request, 'chat/messages.html', {  
    	'users':   mark_safe( serializers.serialize('json', User.objects.all() ) ),
    	'current_user': mark_safe( serializers.serialize('json', [ request.user ] ) )
    })