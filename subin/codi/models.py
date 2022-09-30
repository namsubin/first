from django.db import models
from django.urls import reverse
from codi.fields import ThumbnailImageField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner=models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    class Meta:
        ordering=('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('codi:category_detail', args=(self.id,))
    
class Codi(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Codi Description', blank=True)
    image = ThumbnailImageField(upload_to='codi/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)
    url = models.URLField('site_url')
    owner=models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    class Meta:
        ordering=('title',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('codi:codi_detail', args=(self.id,))
    
    