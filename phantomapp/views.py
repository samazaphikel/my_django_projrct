from phantomapp import forms
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect

def error404(request,exception):
	return render(request,"404.html")

def error500(request,*args):
	return render(request,"505.html")

def index(request):
	return render(request,"index.html")



def login(request):
	if request.method == "POST":
		form_login = forms.LoginForm(data=request.POST)
		if form_login.is_valid():
			username = form_login.cleaned_data['username']
			password = form_login.cleaned_data['password']
			authentication = authenticate(username=username,password=password)
			if authenticate is not None:
				return redirect('/')
			else:
				return render(request,"login.html",{'form_login':form_login})

	else:
		form_login = forms.LoginForm()

	return render(request,"login.html",{'form_login':form_login})





