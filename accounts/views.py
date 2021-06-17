from django.shortcuts import render, redirect
from .models import CustomUser
from django.views import View
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.

class SignupView(View):
	def get(self, request, *args, **kwargs):
		form =CustomUserForm()
		return render(request, 'accounts/signup.html', {'form':form})

	def post(self, request, *args, **kwargs):
		form = CustomUserForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			city = form.cleaned_data['city']
			phone_number = form.cleaned_data['phone_number']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			username = email.split('@')[0]

			if password == confirm_password:
				user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name, email=email, password=password, username=username)
				user.phone_number = phone_number
				user.city = city
				user.save()

				current_site = get_current_site(request)
				mail_subject = 'Account Activation'
				message = render_to_string('accounts/email_verification.html', {

					'user':user,
					'domain' : current_site,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					})
				send_mail = EmailMessage(mail_subject, message, to=[email])
				print(send_mail)
				send_mail.send()
				
				messages.success(request,'Account successfully Created')
				return redirect('signup')
			else:
				messages.error(request, 'Password Does not match!')
				return redirect('signup')
		else:
			return redirect('signup')


def EmailVerification(request, uidb64, token):
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = CustomUser.objects.get(pk=uid)

	except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
		user = None

	if user is not None and default_token_generator.check_token(user, token):
		user.is_active = True
		user.save()
		messages.success(request, 'Thank You! Your account is successfully activated.')
		return redirect('login')
	else:
		messages.error(request, 'Sorry something went wrong!')
		return redirect('login')



class LoginView(View):
	def get(self, request, *args, **kargs):
		return render(request, 'accounts/login.html')

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(email=email, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,'User successfully logged in.' )
			return redirect('dashboard')

		else:
			messages.error(request, 'Invalid credentials')
			return redirect('login')

@login_required(login_url='login')
def LogoutView(request):
	logout(request)
	return redirect('login')


class DashboardView(LoginRequiredMixin,View):
	def get(self, request, *args, **kwargs):
		return render(request, 'accounts/dashboard.html')


class PasswordResetView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'accounts/password_reset.html')

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		if CustomUser.objects.filter(email__iexact=email).exists():
			user = CustomUser.objects.get(email=email)
			current_site = get_current_site(request)
			mail_subject = 'Password Reset'
			message = render_to_string('accounts/password_reset_email.html', {

					'user':user,
					'domain' : current_site,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					})
			send_mail = EmailMessage(mail_subject, message, to=[email])
			print(send_mail)
			send_mail.send()
			messages.success(request, 'A reset link sent to your email')
			return redirect('login')
		else:
			messages.error(request, 'Email Does Not Exist')
			return redirect('password_reset')

class PasswordResetEmailView(View):

	def get(self,request, uidb64, token, *args, **kwargs):
		try:
			uid = urlsafe_base64_decode(uidb64).decode()
			user = CustomUser.objects.get(pk=uid)

		except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
			user = None
		if user is not None and default_token_generator.check_token(user, token):
			request.session['uid'] = uid
			messages.success(request, 'Please Reset Your Password')
			return redirect('create_new_password')
		else:
			messages.error(request, 'Something went wrong, please try again later')
			return redirect('login')


class CreateNewPasswordView(View):
	def get (self, request, *args, **kwargs):
		return render(request, 'accounts/create_new_password.html')
		
	def post(self, request, *args, **kwargs):
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')

		if password == confirm_password:
			uid = request.session.get('uid')
			user = CustomUser.objects.get(pk=uid)
			user.set_password(password)
			user.save()
			messages.success(request, 'Password Reset Successfully. Please Login with new password')
			return redirect('login')
		else:
			messages.error(request, 'Password Does Not Match')
			return redirect('create_new_password')
















