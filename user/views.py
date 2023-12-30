from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    
    if request.method == 'POST':
        forms=RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('user-login')
    else:
        forms=RegisterForm()
    context={
        'forms':forms
    }
    return render(request,'user/register.html',context)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST or None,instance=request.user)
        p_form=ProfileUpdateForm(request.POST or None,request.FILES or None,instance=request.user.profilemodel)
        if u_form.is_valid()  and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profilemodel )
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'user/profile.html',context)