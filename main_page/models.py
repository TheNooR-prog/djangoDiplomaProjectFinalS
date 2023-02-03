from django.core.validators import RegexValidator, ValidationError
from django.db import models
import uuid
import os

import djangoDiplomaProject.settings


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )


class UserReservation(models.Model):
    email_re = RegexValidator(regex=r'^[0-9a-zA-z]+([-\.]?[0-9a-zA-z_])*@[0-9a-zA-z]+(\.?[0-9a-zA-z])*$',
                              message='Email could include "0-9,a-z,A-Z,_,-,." only')
    mobile_re = RegexValidator(regex=r'^(\d{3}[- ]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, validators=[email_re])
    phone = models.CharField(max_length=15, validators=[mobile_re])
    date = models.DateField()
    time = models.TimeField()
    number_people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=250, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-time', '-is_processed', )

    def __str__(self):
        return f'{self.date} {self.time} | {self.name} {self.phone}: {self.message[:50]}'


class About(models.Model):

    header = models.TextField(max_length=400)
    first_fact = models.TextField(max_length=200)
    second_fact = models.TextField(max_length=200)
    third_fact = models.TextField(max_length=200)
    footer = models.TextField(max_length=400)
    video_link = models.URLField()

    def __str__(self):
        return f'Click here to change About part. Adding new About parts is forbidden.'

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValidationError('Only one About instance allowed')
        return super(About, self).save(*args, **kwargs)


class WhyUs(models.Model):
    header = models.TextField(max_length=400)
    first_fact_header = models.CharField(max_length=50)
    first_fact_text = models.TextField(max_length=200)
    second_fact_header = models.CharField(max_length=50)
    second_fact_text = models.TextField(max_length=200)
    third_fact_header = models.CharField(max_length=50)
    third_fact_text = models.TextField(max_length=200)

    def __str__(self):
        return f'Click here to change Why Us. Adding new Why Us parts is forbidden.'

    def save(self, *args, **kwargs):
        if not self.pk and WhyUs.objects.exists():
            raise ValidationError('Only one Why Us instance allowed')
        return super(WhyUs, self).save(*args, **kwargs)

class StatsCounter(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    number = models.PositiveSmallIntegerField()
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}:{self.number}'

    class Meta:
        ordering = ('position', )

class Testimonials(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('testimonials/', new_filename)

    stars_amount_re = RegexValidator(regex=r'^[1-5]$',
                              message='1 to 5 stars only')
    text = models.TextField(max_length=200)
    name = models.CharField(max_length=25)
    occupation = models.CharField(max_length=25)
    stars_amount = models.PositiveSmallIntegerField(validators=[stars_amount_re])
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.text[:50]}'
    class Meta:
        ordering = ('position', )


class Event(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('events/', new_filename)

    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    text = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.text[:50]}'
    class Meta:
        ordering = ('position', )


class Chef(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('chefs/', new_filename)

    name = models.CharField(max_length=25)
    occupation = models.CharField(max_length=25)
    text = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.occupation}'
    class Meta:
        ordering = ('position', )

class Gallery(models.Model):
    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split(".")[-1]
        new_filename = f"{uuid.uuid4()}.{ext_file}"
        return os.path.join('gallery/', new_filename)

    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        ordering = ('position', )

class UserContact(models.Model):
    email_re = RegexValidator(regex=r'^[0-9a-zA-z]+([-\.]?[0-9a-zA-z_])*@[0-9a-zA-z]+(\.?[0-9a-zA-z])*$',
                              message='Email could include "0-9,a-z,A-Z,_,-,." only')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, validators=[email_re])
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed', )

    def __str__(self):
        return f'{self.date[:11]} | {self.subject}: {self.message[:50]}'
