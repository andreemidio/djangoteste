from django.db import models


class Products(models.Model):
    product_url = models.CharField(max_length=255)
    consult_date = models.DateTimeField(default=False)
    product_url_created_at = models.DateTimeField(max_length=255)
    product_url_image = models.CharField(max_length=255)
    store_url = models.CharField(max_length=255)
    c = models.IntegerField(null=True)

    def __str__(self):
        return self.store_url

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'
        ordering = ['pk']
