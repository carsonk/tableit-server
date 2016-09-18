from django.db import models

# Menu

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.SmallIntegerField(default=0)

# Orders

class Order(models.Model):
    time_submitted = models.DateTimeField(auto_now_add=True)
    menu_items = models.ManyToManyField(MenuItem)
