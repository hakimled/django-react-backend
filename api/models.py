from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
import os
from django.utils import timezone
from random import sample
from PIL import Image


def upload_location(instance, filename):
	today = timezone.now()
	base , ext = os.path.splitext(filename)

	randomList = [
		'1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f',
		'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'w','x','y','z']
	rando = sample(randomList, 10)
	new_random = ''.join(rando).upper() 

	file_path = 'images/{date}-{basename}{filename}'.format(date=today, basename=new_random,  filename=ext)
	return file_path






class Post(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    post_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.id} has {self.likes} likes' 
    
    
    
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.width > 300 or img.height > 300:
    #         output_size = (300, 300)
    #         img.resize(output_size)
            
    #        # b = img.filter(ImageFilter.GaussianBlur(14))
    #         img.save(self.image.path)
    
    
@receiver(pre_delete, sender=Post)
def delete_image(sender, instance, **kwargs):
    # Delete the image file from the media folder
    if instance.image:
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.image))
        if os.path.exists(image_path):
            os.remove(image_path)


pre_delete.connect(delete_image, sender=Post)

