from django.urls import path
from praisy.views import *

urlpatterns=[
   path('books/getall/',getall_books,name="get_books"),
   path("user/getall/",getall_users,name='getall_users'),
   path("product/get/",get_products,name='get_products'),
   path("student/get/",get_students,name='get_students'),
   path("blog/get/",get_blogs,name='get_blogs'),
   path('customers/getall/',Customer_view,name="customer_view"),
   path("customers/post",customer_post,name="customer_post"),
   path("customers/",CustomerAPIView.as_view(),name="customer_class_view"),
   path("customers/create",CustomerAPIView.as_view(),name="customer_create"),
   path("customers/getbyid/<int:cus_id>/",Customer_Single.as_view(),name="customer_getbyid"),
   path("student/",Student_det.as_view(),name='student_details'),
   path("student/post",Student_det.as_view(),name='student_post_det'),
   path("student/getbyid/<int:std_id>/",student_edit.as_view(),name="student_getbyid"),
   path('category/getall/',category_det.as_view(),name="get_cate"),
   path("category/post",category_det.as_view(),name='category_post_det'),
   path("product/getbyid/<int:pro_id>/",product_get.as_view(),name="product_getbyid"),
   path('product/getall/',product_det.as_view(),name="get_prod"),
   path("product/post",product_det.as_view(),name='product_post_det'),
   path('stdcourse/get/',stud_det.as_view(),name="get_prod"),
   path("course/getbyid/<int:st_id>/",course_edit.as_view(),name="course_getbyid"),

] 