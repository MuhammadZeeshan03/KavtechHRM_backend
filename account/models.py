from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet
#  Custom User Manager
from django.db.models import options


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        """
      Creates and saves a User with the given email, name, tc and password.
      """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            password=password,

        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
      Creates and saves a superuser with the given email, name, tc and password.
      """
        user = self.create_user(
            email,
            password=make_password(password),
            name=name,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


#  Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def verify_password(self, raw_password):
        return pbkdf2_sha256.varify(raw_password, self.password)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserProfile(models.Model):
    user_fk = models.ForeignKey('User', on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    experience = models.TextField(max_length=500, blank=True)
                 # 'b_degree', 'b_institute','m_degree', 'm_institute', 'phd_degree', 'phd_institute',
    b_degree = models.TextField(max_length=10, blank=True)
    b_institute = models.TextField(max_length=50, blank=True)
    m_degree = models.TextField(max_length=10, blank=True)
    m_institute = models.TextField(max_length=50, blank=True)
    phd_degree = models.TextField(max_length=10, blank=True)
    phd_institute = models.TextField(max_length=50, blank=True)
    job_openings = models.CharField(max_length=500, blank=True)
    birth_date = models.DateField(blank=True),
    sched_test = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "account_kavprof"

    def __self__(self):
       return "self.first_name"