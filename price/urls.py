from django.urls import path

from . import views

urlpatterns = [
	path('', views.default, name = "default"),
	path('home/', views.home, name = "home"),
	path('price/', views.getPrice, name="get_price"),
	]
