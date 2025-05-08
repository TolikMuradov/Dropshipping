from django.db import models
from .validators import validate_image

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_cny = models.DecimalField(max_digits=10, decimal_places=2)
    price_local = models.DecimalField(max_digits=10, decimal_places=2)
    source_url = models.URLField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
