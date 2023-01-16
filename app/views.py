from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import uploder,Category
from app.form import img

# Create your views here.
def home(request):
    ob=Category.objects.all()
    image=uploder.objects.all()
    data={"image":image,"ob":ob}
    return render(request,"home.html",data)

def category(request,id):
    ob=Category.objects.all()
    oo=Category.objects.get(pk=id)
    image=uploder.objects.filter(category=oo)
    data={"image":image,"ob":ob}
    return render(request,"home.html",data)
    

def trending(request):
    return render(request,"trending.html")


# def join(request):
#     return render(request,"join.html")



#----------#
# this code for login logout
#----------#
# code for loging file ------join.html

@login_required(login_url='signin')
def log(request):
    if 'username' in request.session:
        crnt_usr=request.session['username']
        print(crnt_usr)
    return render(request,"join.html")

def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Password doesn't match")
        else:
            user=User.objects.create_user(username=name,email=email,password=pass1)
            user.save()
            return redirect('signin')
    return render(request,"signup.html")


def signin(request):
    if request.method=='POST':
        name=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=name,password=pass1)  
        if user is not None:
            login(request,user)
            return redirect("upload")
        else:
            return HttpResponse("<h1>Username or password is incorrect</h1>")
    return render(request,"login.html")





#----------#
# this code for upload a photo
#----------#

def upload(request):
    if request.method == "POST":
        form=img(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form =img()
    ab=uploder.objects.all()
    return render(request,"upload.html",{ "ab":ab,"form":form})

def remove(request,id):
    uploder.objects.filter(id=id).delete()
    return redirect("/upload")
    
    
    
    
    
    
    
    
    
    
    
    
