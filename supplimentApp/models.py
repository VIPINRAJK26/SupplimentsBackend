from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Orders(models.Model):

    STATUS_CHOICES = (
        ('credit', 'Credit'),
        ('paid', 'Paid'),
    )

    QUANTITY_STATUS_CHOICES = (
        ('bottle', 'Bottle'),
        ('loose', 'Loose'),
    )

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='credit'
    )

    # Remaining unpaid amount
    credit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Total order price
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity_status = models.CharField(
        max_length=20,
        choices=QUANTITY_STATUS_CHOICES,
        default='bottle'
    )

    loose_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    bottle_quantity = models.IntegerField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def clean(self):

        # CREDIT → credit amount required
        if self.status == 'credit':
            if self.credit_price is None:
                raise ValidationError({
                    'credit_price': 'Credit amount is required when status is credit.'
                })

            if self.credit_price > self.price:
                raise ValidationError({
                    'credit_price': 'Credit amount cannot exceed total price.'
                })

        # PAID → remove credit amount
        if self.status == 'paid':
            self.credit_price = None

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.order_id}"