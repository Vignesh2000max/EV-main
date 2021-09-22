from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser,PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    station_name = models.CharField(max_length=100, default='no', blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(max_length=300)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pin = models.CharField(max_length=50)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class bookedSlotLogDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    station = models.CharField(max_length=100)
    charge_point_number = models.CharField(max_length=100)
    booked_date = models.DateField(auto_now_add=True)
    slot_booked_time = models.TimeField()
    booked_at = models.TimeField(auto_now_add=True)