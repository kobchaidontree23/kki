from django.shortcuts import render
from .models import Post
from .models import Review
from django.contrib import messages
from django.contrib.auth.models import User

def hello(request):
    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html',
                  {'a': 'dfdf'}
                  )


def rate(request):
    return render(request, 'rate_us.html')


def addBlock(request):
    name = request.POST['name']
    desc = request.POST['desc']
    pos = request.POST['pos']
    post_info = Post(name=name, desc=desc,pos = pos)
    post_info.save()
    return render(request, 'rate_us.html', 
    {'name': name, 
    'desc': desc,
    'pos': pos})


def reviews(request):
    
    #reviews = request.POST['reviews']
    
    # review_info = Review(reviews=reviews)
    # review_info.save()
    context = {}
    if request.method == 'POST':
        
        reviews = request.POST['reviews']
        if reviews != '':
            review_info = Review(reviews=reviews)
            review_info.save()
            context['status'] = 'success'
            return render(request, 'rate_us.html', context)
        else:
            context['status'] = 'alert'
            return render(request, 'rate_us.html', context)
# Create your views here.

def addNew(request):
     username = request.POST['username']
     firstname = request.POST['firstname']
     lastname = request.POST['lastname']
     password = request.POST['password']
     repassword  = request.POST['repassword']
     email = request.POST['email']
     user = User.objects.create_user(
         username = username,
         first_name = firstname,
         last_name = lastname,
         email = email,
         password = password,
         )
     user.save()
     return render(request,'register_form.html')

def register(request):
    return render(request,'register_form.html')