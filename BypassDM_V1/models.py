import uuid
from django.db import models
from autho.models import TwitterUser
from cryptography.fernet import Fernet

class Tweet(models.Model):
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    twitter_user_fullname = models.CharField(max_length=150)
    username = models.CharField(max_length=255)
    message = models.ForeignKey('EncryptedMessage', on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    twitter_userid = models.CharField(max_length=100, default='')
    key = models.TextField(null=True)

    def __str__(self):
        return '{}: {}'.format(self.username, self.timestamp)


class EncryptedMessage(models.Model):
    encrypted_text = models.TextField()
    encrypted_message = models.BinaryField(null=True)


    def __str__(self):
        return self.encrypted_text
