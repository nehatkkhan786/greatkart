from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
	def create_user(self, first_name, last_name, username, email, password=None, *args, **kwargs):
		if not email:
			raise ValueError('User must have an email')

		if not username:
			raise ValueError('user must have an username')

		user= self.model(
			email = self.normalize_email(email),
			username = username,
			first_name = first_name,
			last_name = last_name,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, first_name, last_name, email, username, password=None, **other_fields):
		user = self.create_user(
			email=self.normalize_email(email),
			username = username,
			password = password,
			first_name=first_name,
			last_name=last_name,
			)

		user.is_admin = True
		user.is_active = True
		user.is_staff = True
		user.is_superadmin = True
		user.save(using=self._db)
		return user
		#self.create_user(email, username, first_name, last_name, password, **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)
	phone_number = models.CharField(max_length=50)
	city = models.CharField(max_length=200, blank=True, null= True)

	#required Fields
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login= models.DateTimeField(auto_now_add=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superadmin= models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	objects = CustomUserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, add_label):
		return True

	# @property
	# def is_staff(self):
	# 	return self.is_admin








