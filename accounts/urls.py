from django.urls import path
from .views import SignupView, LoginView, EmailVerification,LogoutView,DashboardView,PasswordResetView,PasswordResetEmailView,CreateNewPasswordView

urlpatterns = [

path('signup/', SignupView.as_view(), name='signup'),
path('login/', LoginView.as_view(), name = 'login'),
path('logout/', LogoutView, name='logout'),
path('dashboard/', DashboardView.as_view(),name='dashboard'),
path('email_verification/<uidb64>/<token>/', EmailVerification, name = 'email_verification'),
path('password_reset/', PasswordResetView.as_view(),name='password_reset'),
path('password_reset_email/<uidb64>/<token>/', PasswordResetEmailView.as_view(), name='password_reset_email'),
path('create_new_password/', CreateNewPasswordView.as_view(),name='create_new_password'),


]