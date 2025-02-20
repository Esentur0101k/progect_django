from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Менеджер для модели пользователя
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True  # Исправлено: `superadmin` на `is_superadmin`
        user.save(using=self._db)
        return user

# Кастомная модель пользователя
class User(AbstractUser):
    RESTAURANT = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer'),
    )

    first_name = models.CharField(max_length=50)  # Исправлено: `firs_name` на `first_name`
    last_name = models.CharField(max_length=50)  # Исправлено: `Last_name` на `last_name`
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # Поля для управления доступом
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Исправлено: `data_joined` на `date_joined`
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Исправлено: `created_data`
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)  # Исправлено: `modified_data`
    is_admin = models.BooleanField(default=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=False, blank=True, null=True)
    is_superadmin = models.BooleanField(default=False, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
