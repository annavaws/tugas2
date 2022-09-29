from collections import UserList
from re import L
from django.shortcuts import get_object_or_404, render
from requests import request
from todolist.forms import TaskForm
from todolist.models import Task

from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# agar halaman todokist hanya dapat diakses oleh pengguna yang sudah login
@login_required(login_url='/todolist/login/')

def show_todolist(request):
    # untuk tampilin sesuai user yang login
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'data_todolist': data_todolist,
        'nama': request.user.username,
        'last_login': request.COOKIES['last_login']
    }
    # return todolist.html sebagai tampilan
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


def create_task(request):

    context = {
        'data_todolist': Task.objects.all,
        'nama': request.user.username,
    }
    print("request method", request.method)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.user = request.user
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.is_finished = form.cleaned_data['is_finished']
            # validate
            task.save()
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
    else:
        form = TaskForm()
    context['form'] = form
    return render(request, 'todolist_form.html', context)

# def update_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     is_finished = request.POST.get('is_finished', False)
#     print("is_finished", is_finished)

#     # is_finished = not is_finished
#     if is_finished == "on":
#         is_finished = True

#     task.is_finished = is_finished

#     task.save()

#     return redirect('todolist:show_todolist')