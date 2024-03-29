from django.db.models import Q  #Lookup là dùng truy vấn nhiều field dữ liệu
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.
class SearchProductView(ListView):
    template_name="search/views.html"

    def get_context_data(self,*args, **kwargs):
        context = super(SearchProductView,self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context   #Query lấy dữ liệu : qua bên views.html chỉ cần ghi query là sẽ hiểu

    def get_queryset(self,*args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q',None); #method_dict['q']
        print(query)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()  # nếu ko có gì sẽ trả về những product dc tích fearture
