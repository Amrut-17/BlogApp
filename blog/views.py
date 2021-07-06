from django.shortcuts import render
from .forms import SignUp, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import BlogPost
from django.contrib.auth.models import Group
# Create your views here.

# Home 
def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# About page
def about(request):
    return render(request, 'blog/about.html')

# Contact Page
def contact(request):
    return render(request, 'blog/contact.html')

# Dashboard page 
def dashboard(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.all();
        return render(request, 'blog/dashboard.html', {'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

# SignUp Page
def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            messages.success(request, "You have successfully Signed up !!!")
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUp()
    return render(request, 'blog/signup.html', {'form':form})

# Login Page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')



# Logout Page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Add Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']

                postSave = BlogPost(title=title, desc=desc)
                postSave.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

#Update Post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = BlogPost.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = BlogPost.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

#Delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = BlogPost.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')