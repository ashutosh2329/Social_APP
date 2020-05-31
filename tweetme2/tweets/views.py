from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hellow world</h1>")

def tweet_detail_view(request,tweet_id, *args, **kwargs):
	"""
	Rest Api VIEW
	consume by javascript


	"""
	data ={
	     "id": tweet_id,
	}
	status = 200
	try:
		obj = Tweet.objects.get(id=tweet_id)
		data['title'] = obj.title
		data['content'] = obj.content

	except:
		data['message'] = "Not Found"
		status = 400

	return JsonResponse(data, status=status)