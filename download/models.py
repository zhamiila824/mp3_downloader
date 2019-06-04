from django.db import models


class Request(models.Model):
    email = models.EmailField(verbose_name='email_to')
    url = models.URLField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url