import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from models import ApiAuth


def auth(request, redirect_url='/'):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)
            print redirect_url
            return redirect('/'+redirect_url)
        return redirect('/login')
    else:
        print request.GET
        context = {'redirect_url': request.GET['next']}
        return render(request, 'login.html', context)


def apiauth(request):
    api_auth = ApiAuth()
    token = api_auth.get_token(username=request.GET['user'], password=request.GET['pass'])
    api_auth.save()
    return HttpResponse(token)