from django.urls import path
from LibApp import views
urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('category_page/',views.category_page,name="category_page"),
    path('save_category/',views.save_category,name="save_category"),
    path('Display_category_page/',views.Display_category_page,name="Display_category_page"),
    path('category_edit_page/<int:cat_id>/',views.category_edit_page,name="category_edit_page"),
    path('update_category/<int:cat_id>/',views.update_category,name="update_category"),
    path('delete_page/<int:del_id>/', views.delete_page, name="delete_page"),
path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
path('adminLogin/',views.adminLogin,name="adminLogin"),
path('AdminLogout/',views.AdminLogout,name="AdminLogout"),
path('product_page/',views.product_page,name="product_page"),
path('save_product/',views.save_product,name="save_product"),
path('product_display_page/',views.product_display_page,name="product_display_page"),
path('Edit_product_page/<int:pro_id>/',views.Edit_product_page,name="Edit_product_page"),
path('delete_page/<int:del_id>/', views.delete_page, name="delete_page"),
path('update_product/<int:pro_id>/',views.update_product,name="update_product"),
path('contact_details/',views.contact_details,name="contact_details"),
path('Add_User_product/',views.Add_User_product,name="Add_User_product"),
path('approve_product/<int:product_id>/', views.approve_product, name='approve_product'),
    path('reject_product/<int:product_id>/', views.reject_product, name='reject_product'),


]