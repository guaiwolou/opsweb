# coding:utf8
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage

class UserListView(TemplateView):
    template_name = "user/userlist.html"  #template name
    before_index = 5
    after_index = 5

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        userlist = User.objects.all()    #获取所有的用户列表对象
        paginator = Paginator(userlist, 10)   #实例化Paginator
        page = self.request.GET.get("page", 1)  #获取当前页码
        try:
            page_obj = paginator.page(page)    #获取当前页的数据
        except EmptyPage:
            page_obj = paginator.page(1)
        context['page_obj'] = page_obj
        start_index = page_obj.number-self.before_index
        if start_index < 0:
            start_index = 0
        end_index = page_obj.number+self.after_index
        context['page_range'] = page_obj.paginator.page_range[start_index:end_index]
        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UserListView, self).get(request, *args, **kwargs)


class ModifyUserStatusView(View):
    def post(self, request):
        ret = {"status": 0}
        user_id = request.POST.get("user_id", None)
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            ret["status"] = 1
            ret["errmsg"] = "User does not exists."
        return JsonResponse(ret, safe=True)
