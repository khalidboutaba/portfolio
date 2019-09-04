from django.db import models

class Blog(models.Model):
    title = models.TextField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%A %d %Y')

    def summary(self):
        return self.body[:100]