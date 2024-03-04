from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from .models import Post

@receiver(post_save, sender=Post)
def resize_image(sender, instance, **kwargs):
    if instance.image:
        img = Image.open(instance.image.path)

        # Set the desired size
        desired_size = (400, 400)

        # Resize the image
        img.thumbnail(desired_size)
        img.save(instance.image.path)
