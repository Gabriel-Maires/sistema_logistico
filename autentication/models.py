from django.db import models


class Email_Whitelist(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
