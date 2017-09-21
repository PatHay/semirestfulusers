from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import Register
from .models import User
# Create your views here.

def root(request):
    return redirect('/users')

def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "users/index.html", context)

def new(request):
    form = Register()
    return render(request, "users/new.html", {'form': form})

def create(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            create = User.objects.create(first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'], email = form.cleaned_data['email'])
            create.save()
            return redirect('/')
        else:
            print form.errors
            return redirect('/')
    else:
        return HttpResponse("Error")

def show(request, number):
    context = {
        'number': number,
        'first_name': User.objects.get(id=number).first_name,
        'last_name': User.objects.get(id=number).last_name,
        'email': User.objects.get(id=number).email,
        'created_at': User.objects.get(id=number).created_at,
    }
    return render(request, "users/show.html", context)

def edit(request, number):
    context = {
        'form': Register(),
        'number': number,
    }
    
    return render(request, "users/edit.html", context)

def edit_user(request, number):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            e = User.objects.get(id=number)
            e.first_name = form.cleaned_data['first_name']
            e.last_name = form.cleaned_data['last_name']
            e.email = form.cleaned_data['email']
            e.save()
            return redirect('/')
    else:
        return HttpResponse("Error")

def destroy(request, number):
    d = User.objects.get(id=number)
    d.delete()
    return redirect('/users')