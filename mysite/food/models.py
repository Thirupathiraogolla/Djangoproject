from django.db import models

# Create your models here.
class items(models.Model):
    def __str__(self):
        return self.item_name
    item_name= models.CharField(max_length=40)
    item_desc=models.CharField(max_length=50)
    item_price=models.IntegerField()
    item_image = models.CharField(max_length=600,default='https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png')
