from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from LibApp.models import CategoryDb, ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib import messages
from WebApp.models import ContactDb, Product


# Create your views here.
def index_page(request):
    return render(request,"index.html")
def category_page(request):
    return render(request,"category.html")
def save_category(request):
    if request.method=="POST":
        cat_name=request.POST.get("c_name")
        decsription = request.POST.get("desc")
        image=request.FILES['c_image']
        obj=CategoryDb(category_name=cat_name,Description=decsription,Category_image=image)
        obj.save()
        messages.success(request,"category saved successfully...!")
        return redirect(category_page)

def Display_category_page(request):
    data=CategoryDb.objects.all()
    return render(request,"Display_category.html",{'data':data})
def category_edit_page(request,cat_id):
    data=CategoryDb.objects.get(id=cat_id)
    return render(request,"Edit_category.html",{'data':data})
def update_category(request,cat_id):
    if request.method=="POST":
        cat_name = request.POST.get("c_name")
        decsription = request.POST.get("desc")
        try:
            img=request.FILES['c_image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=cat_id).Category_image
        CategoryDb.objects.filter(id=cat_id).update(category_name=cat_name,Description=decsription,Category_image=file)
        return redirect(Display_category_page)
def delete_page(request,del_id):
    data=CategoryDb.objects.filter(id=del_id)
    data.delete()
    return redirect(Display_category_page)
def admin_login_page(request):
    return render(request,"Admi_Login.html")
def adminLogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome....")
                return redirect(index_page)
            else:
                messages.error(request,"invalid password.......")
                return redirect(admin_login_page)
        else:
            messages.warning(request,"User not found...!")
            return redirect(admin_login_page)

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)
def product_page(request):
    cat=CategoryDb.objects.all()
    return render(request,"Products.html",{'cat':cat})
def save_product(request):
    if request.method=="POST":
        s_category=request.POST.get("cat_name")
        pro_name = request.POST.get("p_name")
        author= request.POST.get("auth")
        language = request.POST.get("lang")

        publish = request.POST.get("pub")
        PUB_date = request.POST.get("pub_date")
        page = request.POST.get("pg")

        decsription = request.POST.get("desc")
        pric=request.POST.get("pri")
        image=request.FILES['p_image']
        obj = ProductDb(Category=s_category,ProductName=pro_name,Description=decsription,Price=pric,
                        ProductImage=image,Author=author,Language=language,
                        Publisher= publish,Publication_date=PUB_date,Pages=page)
        obj.save()
        return redirect(product_page)
def product_display_page(request):
    data = ProductDb.objects.all()
    return render(request,"display_product.html",{'data':data})
def Edit_product_page(request,pro_id):
    data = ProductDb.objects.get(id=pro_id)
    cat=CategoryDb.objects.all()
    return render(request, "Edit_product.html", {'data': data,'cat':cat})
def delete_page(request,del_id):
    data=ProductDb.objects.filter(id=del_id)
    data.delete()
    messages.error(request,"Deleted....!!!!")
    return redirect(product_display_page)
def update_product(request,pro_id):
    if request.method=="POST":
        s_category=request.POST.get("cat_name")
        pro_name = request.POST.get("p_name")
        author= request.POST.get("auth")
        language = request.POST.get("lang")

        publish = request.POST.get("pub")
        PUB_date = request.POST.get("pub_date")
        page = request.POST.get("pg")

        decsription = request.POST.get("desc")
        pric=request.POST.get("pri")
        try:
            image=request.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=pro_id).ProductImage
        ProductDb.objects.filter(id=pro_id).update(Category=s_category,ProductName=pro_name,Description=decsription,Price=pric,
                        ProductImage=file,Author=author,Language=language,Publisher= publish,Publication_date=PUB_date,Pages=page)
        return redirect(product_display_page)

def contact_details(request):
    data=ContactDb.objects.all()
    return render(request,"ContactData.html",{'data':data})
def Add_User_product(request):
    data=Product.objects.all()
    return render(request,"User_product_Accept.html",{'data':data})





def approve_product(request, product_id):
    product = get_object_or_404(ProductDb, id=product_id)
    product.status = 'approved'
    product.save()
    messages.success(request, 'Product has been approved successfully.')
    return redirect('Add_products')  # Assuming 'product_list' is the name of the URL where the list of products is displayed

def reject_product(request, product_id):
    product = get_object_or_404(ProductDb, id=product_id)
    product.status = 'rejected'
    product.save()
    messages.error(request, 'Product has been rejected.')
    return redirect('Add_products')



