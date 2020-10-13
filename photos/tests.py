from django.test import TestCase
from .models import Image, Location, Category

class ImageTestClass(TestCase):

  def setUp(self):
    self.category = Category(cat_name='food')
    self.category.save()

    self.location = Location(city='Nairobi', country='Kenya', locale='Kileleshwa')
    self.location.save()

    self.image = Image(photo='test.jpeg', img_name='test trip', description='a trip to see the nothern lights', location=self.location, category=self.category)
    self.image.save()
  
  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))

  def test_save(self):
    self.image.save_image()
  
  def test_get_img_by_id(self):
    img = Image.get_image_by_id(self.image.pk)
    self.assertEqual(img, self.image)
  
  def test_search(self):
    img_cat = Image.search_cat('food')
    self.assertIn(self.image, img_cat)
    
  def test_delete_image(self):
    image2 = Image(photo='test2.jpeg', img_name='another test trip', description='a trip to watch the olympics', location=self.location, category=self.category)
    image2.save_image()
    image2.delete_image()
    result=Image.get_image_by_id(pk=image2.id)
    self.assertEqual(result,"Image does not exist")
  
  def test_update_image(self):
    new_img = 'test3.jpeg'
    Image.update_image(self.image.id,new_img)
    updated_img = Image.get_image_by_id(self.image.id)
    self.assertEqual(updated_img.photo,"test3.jpeg")
  