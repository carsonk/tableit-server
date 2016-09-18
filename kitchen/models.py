from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.SmallIntegerField(default=0)

class Order(models.Model):
    time_submitted = models.DateTimeField(auto_now_add=True)
    menu_items = models.ManyToManyField(MenuItem)
