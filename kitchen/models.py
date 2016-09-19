from django.db import models
import datetime

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Order(models.Model):
    time_submitted = models.DateTimeField(auto_now_add=True)
    menu_items = models.ManyToManyField(MenuItem)
    
    def __str__(self):
        return self.time_submitted.isoformat()

