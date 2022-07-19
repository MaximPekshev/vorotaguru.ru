from django.db import models
import uuid
from uuslug import slugify

def get_image_name(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.cpu_slug
	return new_name

def get_image_title_name(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.title
	return new_name

class Category(models.Model):
    
    title 				= models.CharField(max_length = 150, verbose_name='Наименование')
    description 		= models.TextField(max_length=10240, verbose_name='Описание', blank=True, null=True)
    meta_name 			= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
    meta_keywords 		= models.CharField(max_length=150, verbose_name='meta keywords', blank=True, null=True, default="")
    meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
    cpu_slug			= models.SlugField(max_length=70, verbose_name='ЧПУ_Url', blank=True, db_index=True)
    picture				= models.ImageField(upload_to=get_image_name, verbose_name='Изображение 800x530', default=None, null=True, blank=True)
    parent_category 	= models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_DEFAULT,null=True, blank=True, default=None)
    
    def __str__(self):
        
        return self.title
        
    def save(self, *args, **kwargs):
        
        self.cpu_slug = '{}'.format(slugify(self.title))	
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Portfolio(models.Model):
    
    title 				= models.CharField(max_length = 150, verbose_name='Наименование')
    picture				= models.ImageField(upload_to=get_image_title_name, verbose_name='Изображение 800x530', default=None, null=True, blank=True)
    parent_category 	= models.ForeignKey('Portfolio_category', verbose_name='Категория', on_delete=models.SET_DEFAULT,null=True, blank=True, default=None)

    def __str__(self):
        
        return self.title
        
    def save(self, *args, **kwargs):	
        super(Portfolio, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

class Portfolio_category(models.Model):
    
    title = models.CharField(max_length = 150, verbose_name='Наименование')
    cpu_slug = models.SlugField(max_length=150, verbose_name='Наименование eng', blank=True, db_index=True)


    def __str__(self):
        
        return self.title
        
    def save(self, *args, **kwargs):
        self.cpu_slug = '{}'.format(slugify(self.title))	
        super(Portfolio_category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Категория портфолио'
        verbose_name_plural = 'Категории портфолио'



class Page(models.Model):

	title 				= models.CharField(max_length=150, verbose_name="Заголовок", null=True)
	meta_title 			= models.CharField(max_length=150, verbose_name='meta title', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
	meta_keywords 		= models.TextField(max_length=1024, verbose_name='meta keywords', blank=True, null=True)
		
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Страница'
		verbose_name_plural = 'Страницы'