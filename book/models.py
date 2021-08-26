from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    cover_image = models.ImageField(upload_to="images", default = None, null=True)
    ebook_pdf = models.FileField(upload_to="ebook-pdf",default = None, null=True)
    publish_date = models.DateField(blank=True, null=True)
    author_full_name = models.CharField(max_length=50, null=False)
    abstract = models.TextField()


    def get_absolute_url(self):
        return reverse("book-detail-page", kwargs={"pk": self.pk})
    
