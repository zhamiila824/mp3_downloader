from django.db import models

class Request(models.Model):
    url = models.URLField(max_length=400)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.url == None:
            return "URL IS NULL"
        return self.url