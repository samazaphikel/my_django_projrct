from phantomapp import views
from django.urls import re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
	re_path(r'^$',views.index,name="index"),
	re_path(r'^login/$',LoginView.as_view(template_name="login.html"),name="login"),
	re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
	]
