from django.conf.urls import url, include
from . import views
from . import user


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^test1/$', views.test1),
    url(r'^test2/$', views.test2),
    url(r'^test3/$', views.test3),
    url(r'^context1/$', views.context1),
    url(r'^context2/$', views.context2),
    url(r'^context3/$', views.context3),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^test_form/$', views.test_form),
    #url(r'^user/userlist/$', user.UserListView.as_view()),
    url(r'^user/', include([
        url(r'^userlist/$', user.UserListView.as_view()),
        url(r'^userlist1/$', user.UserListView1.as_view(), name="userlistView"),
        url(r'^modifystatus/$', user.ModifyUserStatusView.as_view()),
    ]))
]