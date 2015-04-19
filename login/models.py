import uuid
from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import User
import time

class ApiAuth(models.Model):
    user = models.ForeignKey(User)
    token = models.TextField()
    created = models.FloatField(default=time.time)

    def get_token(self, **kwargs):
        self.user = authenticate(**kwargs)
        if self.user is None:
            self.user = User.objects.create_user(**kwargs)

        if self.user.is_active:
            for t in self.user.apiauth_set.all(): t.delete()
            token = str(uuid.uuid1())
            self.token = token
            return token

    def __str__(self):
        return self.user.username+': '+self.token