from django.conf.urls import url
from . import api

urlpatterns = [
    url('room', api.rooms),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say)
]
