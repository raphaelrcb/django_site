from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.
# BB030210


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField()
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])















