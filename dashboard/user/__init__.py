from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User


class UserListView(TemplateView):
    template_name = "user/userlist.html"  #template name

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['userlist'] = User.objects.all()
        return context


    def get(self, request, *args, **kwargs):
        return super(UserListView, self).get(request, *args, **kwargs)
