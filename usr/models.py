from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    display_pic= models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.display_pic.path)

        if(img.height>300 or img.width>300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.display_pic.path, *args, **kwargs)