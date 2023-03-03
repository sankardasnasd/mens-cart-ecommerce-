from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES =(
    ('pant','pant'),
    ('shirt','shirt'),
    ('tshirt','tshirt'),
    ('inner','innerwear'),

)

STATE_CHOICES = (
    ('kerala','kerala'),
    ('tamilnad','tamilnad'),
    ('karnataka','karnataka'),
    ('andhra pradesh','andhra pradesh'),
    ('gujarat','gujarat'),
    ('assam','assam'),
    ('goa','goa'),
    ('delhi','delhi'),
    ('haryana','haryana'),
    ('jammu & kashmir','jammu & kashmir'),

)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    discription =models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=20)
    product_image = models.ImageField(upload_to="product")
    def __str__(self):
        return self.title
    


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices= STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity + self.product.discount_price
    