from django.contrib.auth import views as auth_views
from django.urls import path
from WebApp import views

urlpatterns=[
            path('',views.home_page,name="home"),
path('about/',views.about_page,name="about"),
path('contact/',views.contact_page,name="contact"),
path('our_products/',views.our_products,name="our_products"),
path('save_contact/',views.save_contact,name="save_contact"),
path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
path('Add_products/',views.Add_products,name="Add_products"),
path('save_productdetails/',views.save_productdetails,name="save_productdetails"),
path('single_product_view/<int:product_id>/', views.single_product_view, name='single_product_view'),
path('register_page/',views.register_page,name="register_page"),
path('save_register/',views.save_register,name="save_register"),
path('UserLogin/',views.UserLogin,name="UserLogin"),
path('UserLogout/',views.UserLogout,name="UserLogout"),
path('save_cart/<int:p_id>/',views.save_cart,name="save_cart"),
path('cart_page/',views.cart_page,name="cart_page"),
path('delete_item/<int:p_id>/',views.delete_item,name="delete_item"),
path('UserLogin_page/',views.UserLogin_page,name="UserLogin_page"),
# path('frontpage/',views.frontpage,name="frontpage"),
# path('wishlist/',views.wishlist,name="wishlist"),
path('wishlist_view/',views.wishlist_view,name="wishlist_view"),

path('add_wishlist/<int:wishlist_id>/', views.add_wishlist, name='add_wishlist'),
path('delete_wishlist/<int:w_id>/',views.delete_wishlist,name="delete_wishlist"),
path('save_review/<int:r_id>/',views.save_review,name="save_review"),
path('save_checkout/',views.save_checkout,name="save_checkout"),
path('payment_page/',views.payment_page,name="payment_page"),



    ]