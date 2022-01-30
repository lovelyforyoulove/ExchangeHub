from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DetailView,View
from base.models import  Product      
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.messages.views import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
from backend.settings import BASE_URL
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="/admin/")
def admin_home(request):
    return render(request,"admin_templates/home.html")


class ProductView(View):
    def get(self,request,*args,**kwargs):

     return render(request,"admin_templates/product_create.html")
    def post(self,request,*args,**kwargs):
        user = request.user
        name=request.POST.get("name")
        brand=request.POST.get("brand")
        countInStock=request.POST.get("countInStock")
        
        price=request.POST.get("price")
        
        description=request.POST.get("description")
        
        image=request.FILES.getlist("image")
        product=Product(name=name,countInStock=countInStock,price=price,brand=brand,description=description,user=user,image=request.FILES['image'])
        product.save()
        # return HttpResponse("OK")

@csrf_exempt
def file_upload(request):
    file=request.FILES["file"]
    fs=FileSystemStorage()
    filename=fs.save(file.name,file)
    file_url=fs.url(filename)
    return HttpResponse('{"location":"'+BASE_URL+''+file_url+'"}')


class ProductListView(ListView):
    model=Product
    template_name="admin_templates/product_list.html"
    paginate_by=3

    def get_queryset(self):
        filter_val=self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val!="":
            products=Product.objects.filter(Q(name__contains=filter_val) | Q(product_description__contains=filter_val)).order_by(order_by)
        else:
            products=Product.objects.all().order_by(order_by)   
        product_list=[]
        return product_list

    def get_context_data(self,**kwargs):
        context=super(ProductListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","id")
        context["all_table_fields"]=Product._meta.get_fields()
        return context


class ProductEdit(View):

    def get(self,request,*args,**kwargs):
        product_id=kwargs["product_id"]
        product=Product.objects.get(id=product_id)
        return render(request,"admin_templates/product_edit.html")

    
class ProductAddStocks(View):
    def get(self,request,*args,**kwargs):
        product_id=kwargs["product_id"]
        product=Product.objects.get(id=product_id)
        return render(request,"admin_templates/product_add_stocks.html",{"product":product})
