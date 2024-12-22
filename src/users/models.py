import typing

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from utils.models import BaseModel, uuid_generator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields) -> "User":
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = typing.cast(User, self.model(email=email, **extra_fields))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):  # type: ignore
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    id = models.UUIDField(
        default=uuid_generator, primary_key=True, null=False, blank=False
    )

    email = models.EmailField(
        verbose_name="email address",
        unique=True,
        error_messages={
            "unique": "A user is already registered with this email address",
        },
    )
    username = models.CharField(null=True, max_length=255)

    name = models.CharField(max_length=200, null=True)

    is_staff = models.BooleanField(
        verbose_name="staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        verbose_name="active",
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    requires_activation = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name=("date joined"),
        default=timezone.now,
    )

    objects = UserManager()


class MagicToken(BaseModel):
    user = models.ForeignKey(
        "users.User", related_name="magic_tokens", on_delete=models.CASCADE
    )
    token = models.UUIDField(default=uuid_generator)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)
