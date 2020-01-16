from django.db import models

# Create your models here.


class Carousel(models.Model):
    c_img = models.ImageField(upload_to='c_pics')
    c_label = models.CharField(max_length=100)
    c_desc = models.TextField()


class Destination(models.Model):
    name = models.CharField(max_length=100)
    sub_text = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    detail_desc = models.TextField()
    todo_img1 = models.ImageField(upload_to='pics')
    todo_title1 = models.CharField(max_length=100)
    todo_desc1 = models.TextField()
    todo_img2 = models.ImageField(upload_to='pics')
    todo_title2 = models.CharField(max_length=100)
    todo_desc2 = models.TextField()
    todo_img3 = models.ImageField(upload_to='pics')
    todo_title3 = models.CharField(max_length=100)
    todo_desc3 = models.TextField()
    todo_img4 = models.ImageField(upload_to='pics')
    todo_title4 = models.CharField(max_length=100)
    todo_desc4 = models.TextField()
    dest_map = models.CharField(max_length=500)
    hotel_img1 = models.ImageField(upload_to='pics')
    hotel_name1 = models.CharField(max_length=100)
    hotel_url1 = models.CharField(max_length=300)
    hotel_price1 = models.IntegerField()
    hotel_img2 = models.ImageField(upload_to='pics')
    hotel_name2 = models.CharField(max_length=100)
    hotel_price2 = models.IntegerField()
    hotel_img3 = models.ImageField(upload_to='pics')
    hotel_name3 = models.CharField(max_length=100)
    hotel_price3 = models.IntegerField()
    when_to_visit = models.TextField()


    def __str__(self):
        return self.name
