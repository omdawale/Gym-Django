from django.shortcuts import render
from .models import HomeFields


def Index(request):
	data = HomeFields.objects.all()
	return render(request, 'index.html',{'data':data})

def About(request):
	return render(request,'about-us.html')

def gallery(request):
	return render(request,'gallery.html')

def contact(request):
	return render(request,'contact.html')

def blog(request):
	return render(request,'blog.html')

def schedule(request):
	return render(request,'schedule.html')

def blogdetails(request):
	return render(request,'blog-details.html')
