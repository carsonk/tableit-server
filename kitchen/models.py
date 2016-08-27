from django.db import models


# Menu models.

class MenuCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


# Customer, sessions, and orders.
# Separating out customers from tables, since we might
# want to be able to split checks. 

class Table(models.Model):
    location = models.CharField(max_length=255)

class Customer(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    active = models.BooleanField()

class Order(models.Model):
    STATUS_OPTS = (
        ('s', 'Submitted'),
        ('c', 'Cooking'),
        ('d', 'Delivered')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_OPTS)
    time_submitted = models.DateTimeField(auto_now_add=True)

    menu_items = models.ManyToManyField(MenuItem)
