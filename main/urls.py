from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.about, name='about'),
	url(r'^links/', views.links, name='links'),
	url(r'^books/', views.books, name='books'),
	url(r'^dump/', views.dump, name='dump'),
]
