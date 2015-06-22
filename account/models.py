from django.contrib.auth.models import models, UserManager,BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class UserMgr(BaseUserManager):
    def create_user(self, username, email, password):
        if not username or not email or not password:
            raise ValueError('Every inputs must be filled')
        user = self.model(
            username=username,
            email=email,
            password=make_password(password,None,'pbkdf2_sha256'),
            date_joined = timezone.now()
        )
        user.save()
        return user

    #https://docs.djangoproject.com/en/1.8/topics/auth/customizing/


class User(AbstractBaseUser):
    username = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField()
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    class Meta:
        db_table = 'users'