from tabnanny import verbose
from typing import Any
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=50)
    code =models.CharField(max_length=2)
    class Meta:
        verbose_name_plural ="Countries"
    def __str__(self):
        return f"{self.name}"
    


class Adress(models.Model):
    street=models.CharField(max_length=50)
    postal_code=models.CharField(max_length=50)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}{self.postal_code},{self.city}"
    class Meta:
        verbose_name_plural ="Address entity"

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    adress=models.OneToOneField(Adress, on_delete=models.CASCADE,null=True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title= models.CharField(max_length=50)
    rating= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author= models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling=models.BooleanField(default=False)
    slug= models.SlugField(default="",null=False,db_index=True)
    published_country=models.ManyToManyField(Country)
    def get_absolute_url(self):
        return reverse("detail-page", args=[self.slug])
    def __str__(self):
        return f"{self.title}"
