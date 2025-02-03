from django.contrib import admin
from django.urls import path
from .views import blog,blo,createBlog,updateBlog,deleteBlog,areaView,createArea,updateArea,deleteArea
urlpatterns = [
    path('blog/',blog),
    path('blo/',blo),
    path('create/',createBlog),
    path('update/<int:id>/',updateBlog ),
    path('delete/<int:id>/',deleteBlog),
    path('area/', areaView),
    path('createarea/',createArea),
    path('update_area/<int:id>/', updateArea),
    path('delete_area/<int:id>/',deleteArea)

 ]