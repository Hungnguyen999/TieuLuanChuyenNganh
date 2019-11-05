# cái này dùng để link sản phẩm - bấm vào sản phẩm sẽ ra chi tiết sản phẩm
from django.conf.urls import url  
# nên nhớ sử dụng đúng định dạng : url-url hoặc path-path
#LƯU Ý: PATH,RE-PATH và URL khác nhau: url có regex còn path thì không . Link doc: https://docs.djangoproject.com/en/2.2/ref/urls/ 
from . import views
app_name="list"  # đối với django 2. > thì phải khai báo app_name
from .views import (
    SearchProductView,
)
urlpatterns = [
    url(r'^$',SearchProductView.as_view(),name="query"),
]
# sau đó chúng ta khai báo view này trong Ecommerce/urls
# sau đó chúng ta chỉ việc sử dụng