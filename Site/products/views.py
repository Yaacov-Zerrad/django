from webbrowser import get
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from products.models import Products
from .form import ProductForm, RowProductForm



def product_list(request, *args, **kwargs):
    """return page html"""
    products = Products.objects.all()
    context = { 'title': 'product_list',
               'products':products }
    return render(request, 'index.html', context)






def product_create(request):
    """create form facile"""
    form = ProductForm(request.POST or None)
    message = "Fill the form"
    if form.is_valid():
        form.save()
        form = ProductForm()
        message = 'We have receive your product !'
    return render(request, 'products/create.html', {'form':form, 'message': message})



def product_update(request, pk):
    """update form"""
    obj = get_object_or_404(Products, id=pk)
    # try:
    #     obj = Products.objects.get(id=pk)    
    # except Products.DoesNotExist:
    #     raise Http404
    form = ProductForm(request.POST or None, instance=obj)
    message = "Update the form"
    if form.is_valid():
        form.save()
        form = ProductForm()
        message = 'your modification was successfully !'
    return render(request, 'products/update.html', {'form':form, 'message': message})


def product_delete(request, myid):
    obj = get_object_or_404(Products, id=myid)
    name = obj.name
    if request.method == "POST":
        obj.delete()
        return redirect('manager')
    
    return render(request, 'products/delete.html', {'name':name})
    




def product_manager(request):
    obj = Products.objects.all()    
    context ={'title': 'table',
              'object': obj }
    return render(request, 'products/manager.html', context)

# def product_create(request):
#     """create form super diff"""
#     message = 'fill  the form'
#     if request.POST:
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         image= request.POST.get('image')
#         slug= request.POST.get('slug')
#         newProduct = Products.objects.create( name=name , description=description , price=price , image=image , slug=slug)
#         newProduct.save()
#         message = "your product was saved successfully"
#     return render(request, 'products/create.html', { 'message': message})

# def product_create(request):
#     """create form  diff"""
#     form = RowProductForm()
#     message = 'fill  the form'
#     if request.method == "POST":
#         form = RowProductForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data) dict des donnees
#             newProduct = Products.objects.create(**form.cleaned_data)
#             newProduct.save()
#             form = RowProductForm()
#             message = "your product was saved successfully"
#     return render(request, 'products/create.html', {'form':form, 'message':message})
  
    
    
    
    
    
    
    
    
#_________________________________________________


def index2(request, *args, **kwargs):
    context = { 'title' : 'index',
               'name': 'yaacov',
               'age' : 25,
               'list' : [13, 24, 35, 42, 56, 67, 71],
               'str' : 'STR'
               }
    return render(request, 'index2.html', context)
    

def contact(request, *args, **kwargs):
    context = { 'title' : 'contact',
               'contact': 'yaacov',
               'age' : 25,
               }
    return render(request, 'contact.html', context)



def blog(request, *args, **kwargs):
    context = { 'title' : 'blog',
               'contact': 'yaacov',
               'age' : 25,
               }
    return render(request, 'blog.html', context)