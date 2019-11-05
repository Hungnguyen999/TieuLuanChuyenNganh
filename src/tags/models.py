from django.db import models
from django.db.models.signals import pre_save,post_save
from django.urls import reverse

from products.models import Product    # Bước 1 của tạo quan hệ cơ sở dữ liệu giữa 2 bảng product và tags
from products.utils import unique_slug_generator 
# Create your models here.
class Tag(models.Model):
    title =  models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product,blank=True) #Bước 2 của tạo quan hệ csdl
    #blank=true có nghĩa là định nghĩa đây là foreign-key . 
    #Khi khóa chính này rỗng thì sẽ bị lỗi toàn vẹn IntergrityError
    def __str__(self):
        return self.title
        
def tag_pre_save_receiver(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(tag_pre_save_receiver,sender=Tag)
#Ở video 7 sẽ hướng dẫn về cách làm sao để lấy được product thông qua tag và ngược lại thông qua reverse lookup