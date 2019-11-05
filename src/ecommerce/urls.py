"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from .views import home_page,home_page_old,about_page,contact_page,login_page,register_page
from django.views.generic import TemplateView
from carts.views import cart_home
app_name="list"  # đối với django 2. > thì phải khai báo app_name

# from products.views import (
#     ProductListView,
#     product_list_view,
#     ProductDetailView,
#     product_detail_view,
#     ProductFeaturedDetailView,
#     ProductFeaturedListView,
#     ProductDetailSlugView
#     ) 
from django.conf.urls.static import static  # IMPORT 2 THƯ VIỆN STATIC VÀ SETTING VÀO
from django.conf import settings
urlpatterns = [
    url(r'^$',home_page,name="home"),
    url(r'^login/',login_page,name="login"),
    url(r'^about/',about_page,name="about"),
    url(r'^homepage/',home_page,name="home"),
    url(r'^contact/',contact_page,name='contact'),
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^register/',register_page,name="register"),
    url(r'^products/',include('products.urls',namespace='products')),
    url(r'^bootstrap/',TemplateView.as_view(template_name="bootstrap/example.html")),
    url(r'^search/',include("search.urls",namespace="search")),
    url(r'cart/',cart_home,name="cart"),
    # url('products/',ProductListView.as_view()),
    # url('products-fbv/',product_list_view),
    # url('products/<int:pk>/',ProductDetailView.as_view()),
    # url('products/<slug:slug>',ProductDetailSlugView.as_view()),
    # url('products-fbv/<int:pk>/',product_detail_view),
    # url('featured/<int:pk>/',ProductFeaturedDetailView.as_view()),
    # url('featured/',ProductFeaturedListView.as_view()),
    
    
    #GHI CHÚ : 
    # URL trang web ví dụ : www.example.com/article/The 46 Year Old Virgin
    #Slug là 1 phần của url, Tất cả các chữ cái được rút gọn và 
    #dấu cách được thay thế bằng dấu gạch nối -. Xem URL của trang web này để biết ví dụ!
    #www.example.com/article/the-46-year-old-virgin
    #Nếu không có slug thì sẽ như thế này : www.example.com/article/The%2046%20Year%20Old%20Virgin  Rất xấu
    # ĐỪNG ĐỂ CÁC SLUG TRÙNG NHAU . NẾU TRÙNG NHAU SẼ BỊ LỖI HIỂN THỊ VỀ MultipleObjectsReturned
]
if settings.DEBUG:   #THÊM CÁI DÒNG NÀY VÀO 
    urlpatterns=urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)   # SAU ĐÓ CHẠY SERVER LINK ADMIN
    #THÌ SẼ THẤY SỰ THAY ĐỔI SẼ XUẤT HIỆN 1 SỐ FILE CSS ĐƯỢC TÌM THẤY
    #TIẾP TÚC CHẠY LỆNH python manage.py collectstatic
    # => các file đó sẽ tự động được add vào trong file static_cdn
    urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)