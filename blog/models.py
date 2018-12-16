from django.db import models

from taggit.managers import TaggableManager

from django_boto.s3.storage import S3Storage

s3 = S3Storage()


class Thought(models.Model):
    title = models.CharField(max_length=200)
    tags = TaggableManager(blank=True)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True, storage=s3)

    def __unicode__(self):
        return self.title


class StaticFiles(models.Model):
    '''
    A model to be able to quickly change static images in some of the pages
    using django admin (f. ex. main image in Blog post list page and etc.).
    Only one model instance can exist!
    '''
    landing_image = models.ImageField(null=True, blank=True, storage=s3)
    code_image = models.ImageField(null=True, blank=True, storage=s3)
    thoughts_image = models.ImageField(null=True, blank=True, storage=s3)
    sounds_image = models.ImageField(null=True, blank=True, storage=s3)
    pics_image = models.ImageField(null=True, blank=True, storage=s3)
    resume = models.FileField(null=True, blank=True, storage=s3)
