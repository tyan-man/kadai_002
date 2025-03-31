from django.db import models
from django.conf import settings
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django import forms
from .managers import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(verbose_name="カテゴリー", max_length=255)
    created_at = models.DateTimeField('登録日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)


class Shop(models.Model):
    shop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, verbose_name="カテゴリー", on_delete=models.CASCADE)
    shop_name = models.CharField(verbose_name="店舗名", max_length=255)
    img = models.ImageField(verbose_name="画像", upload_to='images/', null=True, blank=True)
    detail = models.TextField(verbose_name="詳細", max_length=255)
    business_day = models.CharField(verbose_name="営業日", max_length=255)
    business_hour = models.CharField(verbose_name="営業時間", max_length=255)
    p_code = models.CharField(verbose_name="郵便番号", max_length=7)
    address = models.CharField(verbose_name="住所", max_length=255)
    tel = models.CharField(verbose_name="電話番号", max_length=15)
    created_at = models.DateTimeField('登録日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.shop_name
    
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, verbose_name="店舗", on_delete=models.CASCADE)
    review = models.TextField(verbose_name="コメント", max_length=255)
    created_at = models.DateTimeField('登録日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.review

class FavoriteShop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID を使用
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FavoriteShop {self.id}"

class Reservation(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, verbose_name="店舗", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="日付")
    start_time = models.TimeField(verbose_name="開始時間")
    end_time = models.TimeField(verbose_name="終了時間")
    created_at = models.DateTimeField('登録日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['shop', 'date', 'start_time'], name='unique_reservation')
        ]

    def __str__(self):
        return self.date
    
class ShopImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, verbose_name="店舗", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name="画像", upload_to='images/')
    created_at = models.DateTimeField('登録日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.img


