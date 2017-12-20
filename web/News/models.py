from django.db import models

# Create your models here.

class News (models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    created_date = models.DateField(auto_now_add = True)
    modify_date = models.DateField(auto_now = True)
    content = models.TextField()
    #image = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length = 100)
    is_show = models.BooleanField()

    class Meta:
        db_table = "News"

    def _str_(self):
        return self.title

