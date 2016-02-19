from os import listdir, path
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def about(request):
	return render(request, 'main/about.html')

def links(request):
	return render(request, 'main/links.html')

def books(request):
	template = loader.get_template('main/list.html')
	return HttpResponse(template.render(prepare_list_files('books/', 'books'), request))

def dump(request):
	template = loader.get_template('main/list.html')
	return HttpResponse(template.render(prepare_list_files('dump/'), request))

def prepare_list_files(folder, header = None):
	files = listdir(path.join(settings.STATIC_ROOT, folder))
	context = { 'folder' : folder, 'files' : files }
	if header:
		context['header'] = header
	return context
