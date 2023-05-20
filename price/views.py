import json

import requests
from bs4 import BeautifulSoup
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response


@api_view(('GET',))
def getPrice(self):
	# Making a GET request
	r = requests.get('https://www.metal.com/Lithium-ion-Battery/202303240001')
	# check status code for response; r.status_code == 200 Success:
	soup = BeautifulSoup(r.content, 'html.parser')
	s = soup.find("span", {"class": "strong___1JlBD priceDown___2TbRQ"})
	ans = float(s.contents[0])
	return JsonResponse({'ans': ans})

def home(self):
	return HttpResponse("Home Page")
def default(self):
	return HttpResponse("Default Home Page")
