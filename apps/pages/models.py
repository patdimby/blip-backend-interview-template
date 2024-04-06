from django.db import models
from django.utils.text import slugify


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=20, default='', blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    hasChild = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['-title']), ]
        ordering = ('-title',)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class MenuItem(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=20, default='', blank=True)
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['-title']), ]
        ordering = ('-title',)

    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, blank=True)
    resume = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    url = models.CharField(max_length=20, default='', blank=True)
    icon = models.CharField(max_length=20,default='fa', blank=True)
    delay = models.CharField(max_length=4,default='0.2s', blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Link(models.Model):
    title = models.CharField(max_length=20, default='', blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    resume = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    url = models.CharField(max_length=20, default='', blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Address(models.Model):
    street = models.CharField(max_length=200)
    email = models.EmailField()
    daily = models.CharField(max_length=200)
    sitename = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=20)
    facebook = models.CharField(max_length=200, default='', blank=True)
    linkedin = models.CharField(max_length=200, default='', blank=True)
    twitter = models.CharField(max_length=200, default='', blank=True)
    instagram = models.CharField(max_length=200, default='', blank=True)
    youtube = models.CharField(max_length=200, default='', blank=True)
    github = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.sitename
