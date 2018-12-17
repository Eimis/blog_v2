from django.db import models


class Thought(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True)

    def __unicode__(self):
        return self.title


class StaticFiles(models.Model):
    '''
    A model to be able to quickly change static images in some of the pages
    using django admin (f. ex. main image in Blog post list page and etc.).
    Only one model instance can exist!
    '''
    landing_image = models.ImageField(null=True, blank=True)
    code_image = models.ImageField(null=True, blank=True)
    thoughts_image = models.ImageField(null=True, blank=True)
    sounds_image = models.ImageField(null=True, blank=True)
    pics_image = models.ImageField(null=True, blank=True)
    resume = models.FileField(null=True, blank=True)
