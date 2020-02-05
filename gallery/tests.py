from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_category = Category(category_name='Tech-Field')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'Moringa')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='Evans', image_description='Evans is a code enthusiast',image_path='media/gallery/evans.jpg',image_category=self.new_category,image_location=self.new_location)

    


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

     # Testing  instance
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing  saveinf
    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)
    # Testing  deletind
    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='Evans')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    # Testing  category searching
    def test_search_by_category_method(self):
        self.new_image.save_image()
        fetch_specific = Category.objects.get(category_name='Tech-Field')
        self.assertTrue(fetch_specific.category_name=='Tech-Field')

    # Testing  image object retrieval
    def test_retrieve_all_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.image_name,'Evans')

    # Testing  image retrieval
    def test_get_image_by_id_method(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    # Testing  image updation
    def test_update_image_method(self):
        self.new_image.save_image()
        obtained_object =Image.update_image('Evans','Evans')
        fetched = Image.objects.get(image_name='Evans')
        self.assertEqual(fetched.image_name,'Evans')    

    # Testing  location
    def test_obtain_by_location_method(self):
        self.new_image.save_image()
        fetch_specific = Location.objects.get(location_name='Moringa')
        self.assertTrue(fetch_specific.location_name=='Moringa')