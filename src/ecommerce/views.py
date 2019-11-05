from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.models import User
from .forms import ContactForm,LoginForm,RegisterForm

def home_page(request):
    print(request.session.get("first_name","Unknown"))  # khi mà log out ra thì session sẽ là unknown . CÁI NÀY LÀ GETTER
    context={
        "title":"Home Page",
        "content":"Welcome to Home page",
        "premium_content":"Nguyễn Duy Hưnggggg"
    }
    return render(request,"home_page.html",context)  #context là tryền dictionary vào trong home_page.html

def about_page(request):
    context={
        "title":"About Page",
        "content":"Welcome to about page"
    }
    return render(request,"about.html")
def contact_page(request):
    contact_form =ContactForm(request.POST or None)
    context={
        "title":"Contact",
        "contact":"Welcome to the contact page",
        "form":contact_form,
        "brandname":"Cái này truyển từ context ở trong def contact_page qua base.html"
    }
    if request.user.is_authenticated:
        context.update({"premium_content":"Nguyễn Duy Hưng đẹp trai"})
    # if contact_form.is_valid():
    #     print(contact_form.cleaned_data)      
    # if request.method == "POST":
    #     #nếu như method trong form view.html được post 
    #     #thì Get sẽ lấy data từ form truyền về server
    #     print(request.POST.get('fullname'))     #fullname,email,content là name của thẻ trong form bên views.html
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,"contact/views.html",context)

def login_page(request):   #LoginForm là 1 class trong forms.py
    form=LoginForm(request.POST or None)  #Biến chứa form LoginForm, kế thừa từ class LoginForm tại forms.LoginForm
    context={
        "form":form     #Nhận LoginForm 
    }
    
    print("User logged in status")
    if request.user.is_authenticated:  #is_authenticated đã không còn là function nữa : nó đã trở thành hàm boolean trong django 3.0
        print("true")
    else:
        print("false")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")  
        #2 cái này kiểu giống getParameter bên java:
        # get data từ đối tượng username và password
        user=authenticate(request,username=username,password=password) 
        #Check điều kiện đăng nhập
        print("User logged in status")
        if user is not None:
            login(request,user)
            if request.user.is_authenticated:  #is_authenticated đã không còn là function nữa : nó đã trở thành hàm boolean trong django 3.0
                    print("true")
            else:
                    print("false")
            #Redirect to a success page if user != null
            #context['form']=LoginForm()
            return redirect("/login")
        else:
            #Return an error notification if user == null
            print("Lỗi này c ác mày ơi hahahahaha")
    return render(request,"auth/login.html",context) 
    #response Form có chứa nội dung của class LoginForm đã kết hợp với File auth/login.html


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user=User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,"auth/register.html",context)
#Home page cũ 
def home_page_old(request):
    html_="""
    <!doctype html>
        <html lang="en">
        <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <div class='text-center'>
            <h1>Hello, world!</h1>
            </div>
        </head>
        <body>
            <h1>Hello, world!</h1>

            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        </body>
        </html>
    """
    context={
        "title":"About Page",
        "content":"Welcome to Home page"
    }
    return HttpResponse(html_)