from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, Hello {username}!')
            return redirect('usr-login')
    else:
        form=UserRegisterForm()
    return render(request, 'usr/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if(userForm.is_valid() and profileForm.is_valid()):
            userForm.save()
            profileForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('usr-profile')

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'userForm': userForm,
        'profileForm': profileForm
    }

    return render(request, 'usr/profile.html', context)
