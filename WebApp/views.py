from django.contrib.auth import login
from django.shortcuts import render, redirect,get_object_or_404
from LibApp.models import ProductDb, CategoryDb
from WebApp.models import ContactDb, Product, Register_db, CartDb, WishlList, Review_Db, CheckoutDb
from django.contrib import messages
from .form import SignUpForm
import razorpay
# Create your views here.
def home_page(request):
    cat=CategoryDb.objects.all()
    return render(request,"home.html",{'category':cat})
def about_page(request):
   return render(request,"about.html")
def contact_page(request):
    return render(request,"contact.html")
def our_products(request):
    pro = ProductDb.objects.filter(status="approved")

    return render(request, 'OurProducts.html',{'products':pro})

def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em= request.POST.get('email')
        message=request.POST.get('msg')
        obj=ContactDb(Name=na,Email=em,Message=message)
        obj.save()
        return redirect(contact_page)
def filtered_products(request,cat_name):
    data=ProductDb.objects.filter(Category=cat_name)
    return render(request, "Products_Filtered.html",{'data':data})
def Add_products(request):
    cat = CategoryDb.objects.all()
    return render(request,"Add_NewProducts.html",{'cat':cat})
def save_productdetails(request):
    if request.method == "POST":
        s_category = request.POST.get("cat_name")
        stat=request.POST.get("status")
        pro_name = request.POST.get("p_name")
        autr = request.POST.get("auth")
        lan = request.POST.get("lang")

        publish = request.POST.get("pub")
        PUB_date = request.POST.get("pub_date")
        pg = request.POST.get("pg")

        decsri = request.POST.get("desc")
        pric = request.POST.get("pri")

        image = request.FILES['p_image']
        obj = ProductDb(Category=s_category, ProductName=pro_name, Description=decsri, Price=pric,
                        ProductImage =image, Author=autr, Language=lan,status=stat,
                        Publisher=publish, Publication_date=PUB_date, Pages=pg)
        obj.save()
        return redirect(Add_products)


from django.shortcuts import render, get_object_or_404
from .models import Product

def single_product_view(request, product_id):
    data = ProductDb.objects.get(id=product_id)
    review = Review_Db.objects.filter(Product_Id=product_id)
    # c_data = CartDb.objects.all()

    return render(request, 'single_product.html', {'data':data,'review':review})
def register_page(request):
    return render(request,"register.html")
def save_register(request):
    if request.method == "POST":
        name = request.POST.get('na')
        email = request.POST.get('em')
        paswd= request.POST.get('pwd1')
        cofirm_pwd=request.POST.get('pwd2')
        obj=Register_db(Username=name,Email=email,Password=paswd,Confirm_password=cofirm_pwd)
        if Register_db.objects.filter(Username=name).exists():
            messages.warning(request,"Username already exist...!")
            return redirect(register_page)
        elif Register_db.objects.filter(Email=email).exists():
            messages.warning(request, "Email already exist...!")
            return redirect(register_page)
        else:
            obj.save()
            messages.success(request, "Registered successfully...!")
        return redirect(register_page)
def UserLogin(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        pswd=request.POST.get("password")
        if Register_db.objects.filter(Username=un,Password=pswd).exists():
            request.session['Username']=un
            request.session['Password']=pswd
            messages.success(request, "successfully Login....")
            return redirect(home_page)
        else:
            return redirect(register_page)
    else:
        return redirect(register_page)

def UserLogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "successfully Logout....")
    return redirect(home_page)
def save_cart(request,p_id):
    if request.method=="POST":
        name=request.POST.get("u_name")
        print("hai",name)
        P_Name=request.POST.get("p_name")
        qty=request.POST.get("quantity")
        total=request.POST.get("t_price")
        data = ProductDb.objects.get(id=p_id)

        if data.stock > 0:
            data.stock=data.stock-int(qty)
            data.save()

        obj=CartDb(Username=name,ProductName=P_Name,Quantity=qty,TotalPrice=total,Product_Id=data.id)
        obj.save()
        messages.success(request, "successfully added products....")
        return redirect(home_page)
def cart_page(request):
    data=CartDb.objects.filter(Username=request.session['Username'])

    subtotal=0
    shipping_charge=0
    total=0
    for d in data:
        subtotal=subtotal+d.TotalPrice
        if subtotal>=500:
            shipping_charge=50
        else:
            shipping_charge = 100
        total = subtotal + shipping_charge
    return render(request,"cart.html",{'data':data,'subtotal':subtotal,'shipping_charge':shipping_charge,'total':total})
def delete_item(request,p_id):
    # x=CartDb.objects.filter(id=p_id)
    x = CartDb.objects.get(id=p_id)
    pro=x.Product_Id
    data = ProductDb.objects.get(id=pro)
    data.stock = data.stock + int(1)
    data.save()
    x.delete()
    return redirect(cart_page)
def UserLogin_page(request):
    return render(request,"UserLogin.html")


def frontpage(request):
    return render(request, 'frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:

        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
def add_wishlist(request,wishlist_id):
    data = ProductDb.objects.get(id=wishlist_id)
    # x=data.ProductName
    # y=data.Price
    obj=WishlList(Product_Id=data.id,Username=request.session['Username'])
    # obj.ProductImage.save(data.ProductImage.name,data.ProductImage.file)

    # obj=WishlList(ProductName=x,Price=y,ProductImage=z)
    obj.save()
    return redirect(wishlist_view)

def wishlist_view(request):
    data = WishlList.objects.filter(Username=request.session['Username']).values_list("Product_Id", flat=True)

    product_data=ProductDb.objects.filter(id__in=data)

    return render(request, "wishlist.html", {'data': data,'product_data':product_data})
def delete_wishlist(request,w_id):
    x=WishlList.objects.filter(id=w_id)
    x.delete()
    return redirect(wishlist_view)
def save_review(request,r_id):
    if request.method == "POST":
        rev = request.POST.get("review")
        nme = request.POST.get("name")
        email_id = request.POST.get("email")
        rate= request.POST.get("rating")
        data = ProductDb.objects.get(id=r_id)
        obj=Review_Db(Comment=rev,Username=nme,Email=email_id,Rating=rate,Product_Id=data.id)
        obj.save()
        return redirect(home_page)
def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get("u_name")
        email=request.POST.get("em")
        address = request.POST.get("adrs")
        phone=request.POST.get("mob")
        Price=request.POST.get("total")
        # data=CartDb.objects.filter(id=p_id)
        obj=CheckoutDb(Name=name,Email=email,Address=address,Phone=phone,Totalprice=Price)
        # if data.stock > 0:
        #     data.stock=data.stock-data.Quantity
        #     data.save()
        obj.save()
        return redirect(payment_page)

def payment_page(request):

    #Retrive the CheckoutDb object with the specified id
    customer=CheckoutDb.objects.order_by('-id').first()


    #Get the payment amount of the specified customer
    payy=customer.Totalprice

    #convert amount to Paisa(smallest currency unit)
    amount=int(payy*100)


    #convert amount to string for printing
    payy_str=str(amount)


    #printing each character of the payment amount
    for i in payy_str:
        print(i)


    if request.method=="POST":
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_TrXkR4gsjBY3MC','oQQRbVSlhL3MlOi0ZveUSrxl'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})







