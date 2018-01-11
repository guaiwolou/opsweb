#coding:utf8
from django.http.response import HttpResponse, JsonResponse
import json
from django.template import Context, loader, RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return HttpResponse("世界你好!")

#httpresponse
def test1(request):
    data = {"name": "zero", "age": 30}
    return HttpResponse(json.dumps(data), content_type="application/json", status=200)


def test2(request):
    data = {"name": "zero", "age": 30}
    return JsonResponse(data, safe=True)


def test3(request):
    data = ["a", "b", "c"]
    return JsonResponse(data, safe=False)

#context/requestcontext
def context1(request):
    template = loader.get_template("logintest1.html")
    context = Context({"name": "zero"})
    return HttpResponse(template.render(context))


def context2(request):
    template = loader.get_template("logintest2.html")
    context = RequestContext(request, {"name": "zero"})
    return HttpResponse(template.render(context))


def context3(request):
    return render(request, "logintest2.html", {"name": "zero"})


#GET/POST
def login_view(request):
    if request.method == "GET":
        return render(request, "user/login.html", {"title": "Guaiwolo.com"})
    elif request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Login Success!")
            else:
                return HttpResponse("User is not Active!")
        else:
            return HttpResponse("User Login Failed!")

def logout_view(request):
    logout(request)
    return HttpResponse("logout!")

