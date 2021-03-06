from django.db import models

class Category(models.Model):
    """Model definition for Category."""
    name = models.CharField(max_length=50)
    
    # TODO: Define fields here

    # class Meta:
    #     """Meta definition for Category."""

    #     verbose_name = 'Category'
    #     verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    # def save(self):
    #     """Save method for Category."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Category."""
    #     return ('')

    # TODO: Define custom methods here

class Book(models.Model):
    
    status_book = [
        ("availble","availble" ),
        ("rental","rental" ),
        ("solid","solid")
        ]
    
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_author = models.ImageField(upload_to='photos', blank=True, null=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.title
