from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('사이트 URL')

    def __str__(self):
        return "URL"+self.site_name + " : " + self.url
    
    def get_absolute_url(self):
        # return reverse("detail", kwargs={"pk": self.pk})
        return reverse('detail', args=[str(self.id)])


    
