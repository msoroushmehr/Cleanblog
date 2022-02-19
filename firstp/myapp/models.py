from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html
from extensions.utils import jalali_convertor
from django.urls import reverse
class CategoryManager(models.Manager):
        def active(self):
            return self.filter(status=True)

class ArticleManager(models.Manager):
        def published(self):
            return self.filter(status="p")
        
        
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name="زیردسته")
    title = models.CharField(max_length=100, verbose_name=" عنوان دسته بندی")
    slug = models.SlugField(unique=True, null=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(verbose_name="آیا نمایش داده شود؟", default=True)
    position = models.IntegerField(verbose_name="پوزیشن")
    image = models.ImageField(upload_to="images", verbose_name="تصویر")
 
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = (["parent__id","position"])
    def __str__(self):
            return self.title

    objects = CategoryManager()      
class Articles(models.Model):
    STATUS_CHOICES = [('d', 'پیش‌نویس'), ('p', 'چاپ‌شده')]
    title = models.CharField(max_length=100, verbose_name="عنوان")
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles", verbose_name="نویسنده")
    description = models.TextField(verbose_name="محتوا")
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار" )
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی ها", related_name="articles")
    image = models.ImageField(upload_to="images", verbose_name="تصویر")
    status = models.CharField(max_length =1, choices = STATUS_CHOICES, verbose_name="وضعیت مقاله")
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
    def __str__(self):
        return self.title
    def jpublish(self):
        return jalali_convertor(self.published)
    def category_publish(self):
        return self.category.filter(status=True)
    def images_tags(self):
        return format_html("<img src='{}'  width=100 height=75>".format(self.image.url))
    def category_to_str(self):
        return ", ".join([categori.title for categori in self.category_publish()])
    def get_absolute_url(self):
        return reverse("account:home")
    
    objects = ArticleManager()
    images_tags.short_description = "تصویر"
myhome = Articles(image='books-584.jpg', slug='')
    