from django.core.exceptions import ValidationError
from django.db import models
import uuid


def validate_positive(value):
    if value <= 0:
        raise ValidationError("This value must be positive.")


def validate_non_negative(value):
    if value < 0:
        raise ValidationError("This value must be non-negative.")


class Product(models.Model):
    CATEGORY_CHOICES = (
        ("Electronics", "Electronics"),
        ("Clothing", "Clothing"),
        ("Food", "Food"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[validate_positive]
    )
    quantity = models.IntegerField(validators=[validate_non_negative])
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ["name"]
