from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Adds Additional Fields for the django default user model and use email as a unqiue
    Identifier.
    """

    def create_user(self,email,password,**extra_fields):
        """
        Create a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email)
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        """
        Create an Admin user.
        """
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )