from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome,{username}.You are now able to login!")
            return redirect('login')
            #当新用户产生后 最好是redirect 到login page 上
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required 
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Cograts! Your Profile is updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    } # context 是字典
    return render(request,'users/profile.html',context)




# 因为原有的代码 在注册之后是不会添加新的用户，因为只是单纯的post
# Simply create a blank form ....render to the template

# method is post,, put in a condition ,,get post request will contain the data into body
#Specify to get a post request, 会获得 request.POST data
# 如果不是 post request 的话，则直接create blank form ,则不会像数据库添加新的数据

# message.debug//.info//.warning//.error//.sucess

#decorator  add function to the existing function 