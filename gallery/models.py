from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_path = models.ImageField(upload_to = 'gallery/')
    

    def __str__(self):
        return self.image_name


    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item;