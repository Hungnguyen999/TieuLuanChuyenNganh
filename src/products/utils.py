import random   # Hàm tự động sinh ra slug , kiểm tra slug có rỗng hay không nếu rỗng sẽ tự tạo
# bên cạnh đó kiểm tra xem có slug nào trùng không nếu trùng thì tự động sinh ra slug không trùng
import string
from django.utils.text import slugify
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug     #Kiểm tra slug có rỗng hay không 
    else:
        slug = slugify(instance.title)
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()  # nhớ là exists chứ không phải exist
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug