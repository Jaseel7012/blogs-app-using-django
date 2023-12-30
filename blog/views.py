from django.shortcuts import render,redirect
from .models import PostModel
from .form import PostModelForm,PostUpdateForm,CommentForm
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    posts=PostModel.objects.all()
    if request.method == 'POST':

        form=PostModelForm(request.POST,request.user) 
        if form.is_valid():
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('index')
            
    else:
        form=PostModelForm()
    context={
        'posts' : posts,
        'forms':form
    }
    return render(request,'blog/index.html',context)
@login_required
def post_detail(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            instance=comment_form.save(commit=False)
            instance.user=request.user
            instance.post=post
            instance.save()
            return redirect('post-detail',pk=post.id)
    else:
        comment_form=CommentForm()
         
    context={
        'post':post,
        'c_form':comment_form
        
    }
    return render(request,'blog/post_detail.html',context)
@login_required
def post_edit(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form=PostUpdateForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail',pk=post.id)
    else:
        form=PostUpdateForm(instance=post)
    context={
        'post':post,
        'form':form
    }
    return render(request,'blog/post_edit.html',context)
@login_required
def post_delete(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')

    return render(request,'blog/post_delete.html',{'post':post})

