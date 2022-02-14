from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import  BaseUserManager
from django.conf import settings
# Create your models here.

# We use models to decribe the data we need for our application.
# Django then uses these models to setup and configure our Database to store our data effectively.
# Each model in django maps to the specific table within our database.
# Django handles the relationship between our models and database for us. No need to write separate code.

# Custom user model
class  UserProfileManager(BaseUserManager):
    """Manager for User Profile"""
    # Specify some functions within the manager that can be used to manipulate objects within the model it is manager for.

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        #If no email is passed
        if not email:
            raise ValueError("User must have an email address")
        #normalize the email
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff  = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # django needs custom model manager for the usermodel to know how to create users and control users from django commandline tool.
    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #Username will be email address
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # contains text of the feed
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
