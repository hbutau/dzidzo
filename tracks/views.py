from django.shortcuts import render
from django.views.generic import  ListView
from braces import views
from .models import Track

# Create your views here.


class Track_View(views.LoginRequiredMixin, ListView):
	model = 'Track'
	queryset = Track.objects.all()
	context_object_name = "tracks"
	template_name = 'tracks.html'


