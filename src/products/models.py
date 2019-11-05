from django.db.models import Q
from django.db import models
import random
import os


from django.db.models.signals import pre_save,post_save
from django.urls import reverse

from .utils import unique_slug_generator

# Create your models here.
def get_filename_ext(filepath):   
    base_name = os  .path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext
def upload_image_path(instance,filename):   # dùng để dịnh dạng lại đường dẫn của hình ảnh được lưu vao2o 1 folder trong project
    # print(instance)
    # print(filename)
    new_filename = random.randint(1,10000)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename = new_filename,
        final_filename = final_filename
    )

#class ProductQuerySet
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)
    
    def search(self,query):
        lookups = (Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query)|
                Q(tag__title__icontains=query)) #biến xác định những giá trị nào bằng với keyword trong query 
        
        #Q(tag__name__icontains=query)
        #tshirt,t-shirt,t shirt
        return self.filter(lookups).distinct() #trả về các giá trị đó

#class model manager
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)
    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self,id):
        qs = self.get_queryset.filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:   # nếu query ra dữ liệu 
            return qs.first()
        return None
    
    def all(self):
        return self.get_queryset().active()

    def search(self,query):
        return self.get_queryset().search(query).active()  #active là hàm trên productqueryset. Tìm ra những thằng nào đang được active
        #cái này đem qua views.py gọi như thế này  
        # eturn Product.objects.search(query)


class Product(models.Model): #Product category
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True,unique=True)
    description = models.TextField()  # mỗi lần như vậy đều chạy python manage.py makemigrations -> python manage.py migrate
    price = models.DecimalField(decimal_places=2,max_digits=20,null=True,default=39.99)
    #null = true có nghĩa là database thuộc tính này có thể null
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)  # uppload vào file ở đường dẫn MEDIA_ROOT
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self): # Hàm để get link và chuyển trang
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail",kwargs={"slug": self.slug })

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    
def product_pre_save_receiver(sender,instance,*args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)  # Hàm này dùng để tạo slug nếu như slug rỗng sẽ tự động tạo
            #còn nếu như tự điền slug sẽ không ảnh hưởng, đồng thời hàm này còn tự động tạo slug không trùng với bất kì slug nào có trong objects                                
pre_save.connect(product_pre_save_receiver,sender=Product)