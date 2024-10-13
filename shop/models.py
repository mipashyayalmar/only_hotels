from django.db import models
from django.utils import timezone


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class Orders(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('online', 'Online'),
        ('other', 'Other'),
    ]

    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    userId = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Updated to DecimalField for better precision
    name = models.CharField(max_length=90, null=True, blank=True)  # Updated
    email = models.CharField(max_length=111, null=True, blank=True)  # Updated
    address = models.CharField(max_length=111, null=True, blank=True)  # Updated
    city = models.CharField(max_length=111, null=True, blank=True)  # Updated
    state = models.CharField(max_length=111, null=True, blank=True)  # Updated
    zip_code = models.CharField(max_length=111, null=True, blank=True)  # Updated
    phone = models.CharField(max_length=111, default="", null=True, blank=True)  # Updated
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cash')  # New field for payment method
    payment_comments = models.CharField(max_length=255, null=True, blank=True)  # New field for comments if payment method is 'Other'
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.order_id}"

    def save(self, *args, **kwargs):
        # Ensure payment_comments is filled if payment method is 'Other'
        if self.payment_method == 'other' and not self.payment_comments:
            raise ValueError("Payment comments are required for 'Other' payment method.")
        super().save(*args, **kwargs)



class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.update_desc


from django.db import models

class Advertise(models.Model):
    name = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to="shop/advertise/", default="")
    
    def __str__(self):
        return self.name


# models.py
from django.db import models

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)  # Unique table number
    status = models.CharField(max_length=20, default='Blank')  # Example statuses: 'Blank', 'Running', 'Printed', 'Paid'
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Amount associated with the table

    def __str__(self):
        return f'Table {self.number}'
