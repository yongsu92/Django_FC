from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from .models import Fcuser
from .forms import LoginForm


def home(request):
    user_id = request.session.get('user')
    if user_id:

        fcuser = get_object_or_404(Fcuser, pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('home')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request,'fcuser/register.html')
    elif request.method == 'POST':

        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password =request.POST.get('password',None)
        re_password =request.POST.get('re-password',None)
        
        res_data= {}
        
        if not (username  and useremail and password and re_password): # 입력값이 없는 결우
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif re_password != password: # 비밀번호가 입력된 비밀번호와 다른 경우
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            fcuser.save()

        return render(request,'fcuser/register.html',res_data)



# def login(request):
#     if request.method == 'GET':
#         return render(request,'fcuser/login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username',None)
#         password = request.POST.get('password',None)

#         res_data = {}
#         if not (username and password):
#             res_data['error'] = '모든 값을 입력해야 합니다.'
#         else:
#             # fcuser = Fcuser.objects.get(username = username)
#             fcuser = get_object_or_404(Fcuser,username = username)
#             if check_password(password,fcuser.password):
#                 # session
#                 request.session['user'] = fcuser.id


#                 return redirect('/')
#             else:
#                 res_data['error'] = '비밀번호가 틀렸습니다.'
                

#         return render(request,'fcuser/login.html',res_data)

def login(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form =LoginForm()

    return render(request,'fcuser/login.html',{'form':form})
