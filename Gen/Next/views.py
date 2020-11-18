from django.shortcuts import render, redirect
from django.http import HttpResponse
from Next.functions.functions import handle_uploaded_file  
from Next.forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'index.html',{'banner_images' : Banners}) 
    #return render(request,'index.html')


def log(request):
    return render(request,'user_log_in1.html')


def about(request):
    return render(request,'about.html')

def admin(request):
    return render(request,'admin.html')


def banner_upload(request): 
  
    if request.method == 'POST': 
        form = BannerForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
            #messages.success(request,'apurba')
            #return render(request, 'banner_up.html', {'form' : form})
    else: 
        form = BannerForm() 
    return render(request, 'banner_up.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('<center><h1>successfully uploaded <br><a href="admin">back</a></h1></center>') 

def display_images(request): 
  
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'di.html',{'banner_images' : Banners}) 

def delete(request, id):
    Banners = Banner.objects.get(id=id)
    Banners.delete()
    return redirect("/display")


