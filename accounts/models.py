from django.db import models
from main.models import *
import uuid
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class Profiles(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    photo = VersatileImageField(upload_to="chiefuser/",blank=True,null=True)

    class Meta:
        db_table = 'accounts_profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class ProfileCoins(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey('accounts.Profiles',on_delete=models.CASCADE)
    points = models.PositiveBigIntegerField(default=50,blank=True,null=True)

    class Meta:
        db_table = 'accounts_profilecoins'
        verbose_name = 'profilecoin'
        verbose_name_plural = 'profilecoins'
        ordering = ('date_added',)

    def __str__(self):
        return self.profile.name