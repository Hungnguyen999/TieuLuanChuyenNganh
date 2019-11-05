from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404
from django.utils.text import slugify 
from django.core.exceptions import MultipleObjectsReturned
from .models import Product
# Create your views here.
class ProductListView(ListView):
    template_name = "products/list.html"
    def get_context_data(self, *arg,**kwargs):  #Returns a dictionary representing the template context. 
        context= super(ProductListView,self).get_context_data(*arg,**kwargs)
        print(context)
        return context

    def get_queryset(self,*args, **kwargs):  # Query lấy all 
        request =self.request
        return Product.objects.all()


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    def get_queryset(self,*args, **kwargs):  # Query lấy all 
        request =self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured_detail.html"

class ProductDetailSlugView(DetailView):
    queryset= Product.objects.all()
    template_name="products/detail.html"

    def get_object(self,*args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("404 Not found")
        except Product.MuiltipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except:
            raise Http404("Still 404 errorrrrrr")
        return instance


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs':queryset
    }
    return render(request, "products/list.html",context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name ="products/detail.html"
    def get_context_data(self, *arg,**kwargs):  #Returns a dictionary representing the template context. 
        context= super(ProductDetailView,self).get_context_data(*arg,**kwargs)
        print(context)
        return context

    # def get_object(self,*args, **kwargs):   # đây là cách model manager interact với bất kì object
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance
    
    # def get_queryset(self,*args, **kwargs):  
    #     request =self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

def product_detail_view(request,pk=None,*args, **kwargs):
    # print(args)
    # print(kwargs)
    # instance=get_object_or_404(Product,pk=pk)  #id
    #queryset= Product.objects.all()
    instance = Product.objects.get_by_id(pk)   # lấy data từ model qua . hàm get_by_id ở bên model
    print(instance)
    if instance is None:
        raise Http404("Product doesn't exist")
    # qs = Product.objects.filter(id=pk)   #LOOK UP 
    # print(qs)
    # if qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")
    context= {
        'object':instance   # lấy toàn bộ object của pk tương ứng ra 
    }
    return render(request,"products/detail.html",context)   