from wsgiref.util import request_uri

from django.shortcuts import render,redirect,HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from.models import Blog,Area,Comment
from .forms import (
    Formblog,
    UpdateBlogForm,
    UpdateAreaForm,
    FormArea,
    CreateCommentForm


)
# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs

    }


    return render (request,'blog.html',context)


def blo(request):
    blogs1 = Blog.objects.all()
    context = {
        "blogs1":blogs1
    }
    return render(request,'blogs.html',context)

def createBlog(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(

            title = title,
            body= body

        )
        return redirect('http://127.0.0.1:8000/blog/')




    form = Formblog()
    context = {
        'form':form

    }

    return render(request,'form_blog.html', context)


def updateBlog(request, id):
    blog = Blog.objects.get(pk=id)

    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/blog/')

        return HttpResponse('error')

    form = UpdateBlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'update_blog.html', context)


def deleteBlog(request,id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('http://127.0.0.1:8000/blog/')




def areaView(request):
    areas = Area.objects.all()


    context= {

        'areas':areas
    }
    return render(request,'area.html',context)


def createArea(request):

    if request.method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        Area.objects.create(

            name=name,
            about=about
        )


    form = FormArea()
    context = {
        'form':form
    }
    return render(request,'form_area.html',context)





def updateArea(request, id):
    area = get_object_or_404(Area, pk=id)

    if request.method == 'POST':
        form = UpdateAreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('/area/')

        return HttpResponse('Ошибка при обновлении')

    form = UpdateAreaForm(instance=area)
    context = {'form': form}
    return render(request, 'update_area.html', context)


def deleteArea(request,id):
    area = Area .objects.get(pk=id)
    area.delete()
    return redirect('http://127.0.0.1:8000/area/')





def commentView(request,id):
    if request.method=="POST":
        author = request.POST['author']
        text = request.POST['text']
        blog = Blog.objects.get(id=id)
        Comment.objects.create(

            blog=blog,
            author=author,
            text=text


        )

    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    form = CreateCommentForm

    context = {
        'id':id,
        'form':form,

        'comments':comments
    }
    return render(request, 'comment.html',context)




def deleteComment(request, id):
    comment = Comment.objects.get(id=id)

    blog_id = comment.blog.id
    comment.delete()
    return redirect('comment_view', id=blog_id)