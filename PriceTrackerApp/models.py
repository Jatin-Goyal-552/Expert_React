from django.db import models
from .price import get_link_data_amazon,get_link_data_flipkart
from django.contrib.auth.models import User
from urllib import request

class Link(models.Model):
    l_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    url = models.URLField()
    name = models.CharField(max_length=1000, blank=True)
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('price_difference', '-created')

    def save(self, *args, **kwargs):
        try:
            name, price = get_link_data_amazon(self.url)
        except:
            name, price = get_link_data_flipkart(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0
        
        self.name = name
        self.current_price = price
        # self.user=request.user.id
        super().save(*args, **kwargs)