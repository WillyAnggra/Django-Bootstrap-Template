from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog , name="blog"),
    path('tambah/', views.createBlog , name="tambah"),
    path('store/', views.storeBlog , name="store"),
    path('delete/<int:id>', views.deleteBlog , name="delete"),
    path('edit/<int:id>', views.editBlog , name="edit"),
    path('update/<int:id>', views.updateBlog , name="update"),
]