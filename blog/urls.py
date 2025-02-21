from django.contrib import admin
from django.urls import path
from .views import blog,blo,createBlog,updateBlog,deleteBlog,areaView,createArea,updateArea,deleteArea,commentView,deleteComment

urlpatterns = [
    path('',blog),
    path('blo/',blo),
    path('create/',createBlog),
    path('update/<int:id>/',updateBlog, name='updateBlog' ),
    path('delete/<int:id>/',deleteBlog),
    path('area/', areaView),
    path('createarea/',createArea),
    path('update_area/<int:id>/', updateArea),
    path('delete_area/<int:id>/',deleteArea),
    path('comment/<int:id>/',commentView, name='comment_view'),
    path('delete_comment/<int:id>/', deleteComment, name='delete_comment'),

 ]