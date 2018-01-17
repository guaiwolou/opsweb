#coding:utf8
from django.http import HttpResponse, JsonResponse, QueryDict
import json
from django.template import Context, loader, RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


# Create your views here.


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
        return render(request, "user/login.html")
    elif request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        print user
        res = {"status": 0}
        if user is not None:
            if user.is_active:
                login(request, user)
                res["next_url"] = "/"
            else:
                res['status'] = 1
                res['errmsg'] = "User is not Active!"
        else:
            res['status'] = 2
            res['errmsg'] = "User Login Failed!"
        print res
        return JsonResponse(res, safe=True)



def logout_view(request):
    logout(request)
    return HttpResponse("logout!")


def test_form(request):
    if request.method == "GET":
        return render(request, "test/test_from.html")
    else:
        fav = QueryDict(request.body).getlist("fav[]", "")
        print fav
        return HttpResponse("")

class IndexView(View):
    def get(self, request):
        return render(request, "public/index.html")

