from django.db import models

class Upload(models.Model):
   user = models.Foreignkey(UserProfile)
   image = models.ImageField(upload_to='user_images')
