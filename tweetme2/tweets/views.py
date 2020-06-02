from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request,"pages/home.html",context={},status=200)
	# return HttpResponse("<h1>Hellow world</h1>")


def tweet_list_view(request, *args, **kwargs):
	"""
	Rest Api VIEW
	consume by javascript
	"""
	querry_set = Tweet.objects.all()
	tweets_list = [{"id":x.id, "title":x.title, "content": x.content} for x in querry_set]
	data ={
		"isUser": False,
		"response":tweets_list,
	}
	return JsonResponse(data)



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

	return render(request,"pages/tweets.html",context=data)

	# return JsonResponse(data, status=status)