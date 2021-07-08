from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from .models import Post

@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/home/')
			else:
				messages.success(request, 'Incorrect Password')
				return redirect('/')
		else:
			messages.success(request, 'User Does Not Exists')
			return redirect('/')
	if request.user.is_authenticated:
		return redirect('/home/')
	else:
		return render(request, 'login.html')

@csrf_exempt
def home(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			title = request.POST.get('title')
			body = request.POST.get('body')
			if Post.objects.filter(title = title).exists():
				messages.success(request, 'Post Already Exists')
				return redirect('/home/')
			else:
				Post.objects.create(title=title, body=body, user=request.user)
				messages.success(request, 'Blog Posted!')
				return redirect('/home/')
		dic = {'posts':reversed(Post.objects.all())}
		return render(request, 'post.html', dic)
	else:
		return redirect('/')

@csrf_exempt
def register(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
			messages.success(request, 'Username/Email Already Exists')
			return redirect('/register/')
		else:
			user = User.objects.create_user(
				username = username,
				first_name = fname,
				last_name = lname,
				email = email,
				password = password
			)
			messages.success(request, 'Registration Success!')
			return redirect('/')
	if request.user.is_authenticated:
		return redirect('/home/')
	else:
		return render(request, 'register.html')

def logout_view(request):
	logout(request)
	return redirect('/')