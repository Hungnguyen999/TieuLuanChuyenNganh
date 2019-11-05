# $ python manage.py shell
# >>> from tags.models import Tag
# >>> Tag.objects.all()
# <QuerySet [<Tag: T shirt>, <Tag: Sieunhan>, <Tag: Nón>, <Tag: Red>, <Tag: Black>, <Tag: Blue>]>
# >>> Tag.objects.last()
# <Tag: Blue>
# >>> Blue = Tag.objects.last()
# >>> Blue.title
# 'Blue'
# >>> Blue.slug
# 'blue'
# >>> blue.active
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'blue' is not defined
# >>> Blue.active 
# True
# >>> Blue.products
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000002A1D2AB64E0>
# >>> Blue.products.all()
# <ProductQuerySet [<Product: T-Shirt>, <Product: Hat>, <Product: Super man>]>
# >>> Blue.objects.all().first()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\hung\AppData\Local\Programs\Python\Python36\lib\site-packages\django\db\models\manager.py", line 176, in __get__
#     raise AttributeError("Manager isn't accessible via %s instances" % cls.__name__)
# AttributeError: Manager isn't accessible via Tag instances
# >>> Blue.products.all().first() 
# <Product: T-Shirt>
# >>> 
# KeyboardInterrupt
# >>> exit()                     

# hung@DESKTOP-PPO9I2T MINGW64 /d/Django/Ecommerce/ecommerce/src
# $ python manage.py shell
# Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.     
# (InteractiveConsole)
# >>> from products.models import Product 
# >>> qs = Product.objects.all()
# >>> qs
# <ProductQuerySet [<Product: T-Shirt>, <Product: Hat>, <Product: Siêu nhân đồ chơi>, <Product: Super man>, <Product: Super computer>, <Product: Super computer>]>
# >>> tshirt = qs.first()
# >>> tshirt.tag
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Product' object has no attribute 'tag'
# >>> tshirt.title
# 'T-Shirt'
# >>> tshirt.description
# 'Thi is a T-Shirt from Gucci'
# >>> tshirt.tag_set
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000173F7DDA438>
# >>> tshirt.tag_set.all()
# <QuerySet [<Tag: T shirt>, <Tag: Blue>]>
# >>> tshirt.tag_set.filter(title__iexact='Blue')
# <QuerySet [<Tag: Blue>]