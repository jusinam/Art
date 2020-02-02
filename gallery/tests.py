from django.test import TestCase
from .models import Image

# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_image = Image(id=1,image_name='Evans', image_description='Evans is a code enthusiast',image_path='media/gallery/evans.jpg')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

     # Testing Save Method
    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # def tearDown(self):
    #     Image.objects.all().delete()