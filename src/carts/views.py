from django.shortcuts import render
from .models import Cart
# Create your views here.

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('new cart created')
    return cart_obj

def cart_home(request):
    request.session['cart_id'] = "12"
    cart_id = request.session.get("cart_id",None)
    # if cart_id is None and isinstance(cart_id,int): #isinstance dùng để check integer
    #     print('create new cart step')
    #     cart_obj = Cart.objects.create(user=None)
    #     request.session['card_id'] = cart_obj.id
 
    # print(request.session)
    # print(dir(request.session))
    # request.session.set_expiry(300)
    # key = request.session.session_key
    # print(key)
    #request.session['cart_id'] = '12' # cái này truyền first_name: chúng ta qua ecommerce/views.py lấy data GỌI CÁI NÀY LÀ SETTER BÊN KIA LÀ GETTER
    #else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count()==1:
        print('Cart ID exists')
        cart_obj = qs.first()
    else:
        print('Check cart ID exists step')
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    return render(request,"carts/home.html",{})