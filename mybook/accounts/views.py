from accounts.forms import EmailOrMobileLoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def register_request(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your account has been created successfully. You can log in now.")
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = EmailOrMobileLoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {user.username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = EmailOrMobileLoginForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect('/')