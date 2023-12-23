from django.db.models import Q, Subquery
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import signupForm
from .models import signup, cart, ContactMessage
from django.conf import settings
import math
from django.core.mail import send_mail
import random
k1=''
def signincheck(request):
    username=request.POST["username"]
    password=request.POST["password1"]
    print(username,password)
    flag=signup.objects.filter(username=username,password=password)
    print(flag)
    if flag:
        user = signup.objects.get(username=username)
        request.session["email"]=user.email
        request.session["uname"] = user.username
        return render(request,"index.html",{"uname":user.username})
    else:
         msg="Signin Failed"
         return render(request,"login.html",{"msg":msg})


def signupcheck(request):
    if request.method=='POST':
        x=signupForm(request.POST or None)
        if x is not None:
            x.save()
        return render(request,'index.html',{})






def loginpage(request):
    return render(request,"login.html")
def aboutpage(request):
    if "uname" in request.session:
        return render(request,"about.html")
    else:
        return render(request,"sessiontimeout.html")
def contactpage(request):
    return render(request,"contact.html")
def indexpage(request):
    return render(request,"index.html")
def menupage(request):
    return render(request,"menu.html")
def hotelpage(request):
    return render(request,"Hotel.html")
def newsdetailpage(request):
    return render(request,"news-detail.html")
def forgotpass(request):
    return render(request,"forgotpass.html")
def newpassfun(request):
    return render(request,"newpass.html")
def success(request):
    return render(request, "passsuccess.html")
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(5):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
def forgotpassword(request):
    global k1
    if request.method=='POST':
        email=request.POST['email1']
        subject = 'welcome to BudgetBoss'
        k1=(generateOTP())
        print(k1)
        message = 'Hi, thank you for registering in BudgetBoss.Your otp is ' + k1
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email
        send_mail(subject, message, email_from, [recipient_list], fail_silently=False)
        return render(request,'verifyotp.html')
def otp_verify(request):
    x=request.POST['otp']
    print(x,k1)
    if x==k1:
        return render(request,"newpass.html")
    else:
        return render(request,'menu.html')


def empchangepwd(request):
    ename=request.session["uname"]
    return render(request,"userchangepwd.html",{"ename":ename})



def empupdatepwd(request):
    uname=request.session["uname"]


    npwd=request.POST["pass2"]
    flag = signup.objects.filter(Q(username=uname))

    if flag:

        signup.objects.filter(username=uname).update(password=npwd)

        return render(request, "index.html", {"uname": uname})
    else:

        return render(request, "menu.html", {"uname": uname})
def change_password(request):
    x=request.POST.get('uname')
    x1=signup.objects.filter(email=x)
    print(x1)
    if x1:
        xx = signup.objects.get(email=x)
        y=request.POST.get('pass1')
        z=request.POST.get('pass2')
        print(y,z)
        if y==z:
            xx.password=y
            xx.save()
            return render(request,'login.html')
        else:
            return render(request,'newpass.html',{'msg':'Passwords Not Match'})
    else:
        return render(request, 'newpass.html', {'msg': '1st register with that mails'})
def signout(request):
    request.session.flush()
    return render(request,"login.html")

def add_cart(request):
    user=request.session["email"]
    prid=request.POST["pid"]
    print(prid)
    cartobj=cart(mail=user,pid=prid)
    cart.save(cartobj)
    return redirect('/cart')

def get_cart(request):
    Product = [
        {'id': 1, 'name': 'Product 1', 'price': '12.50', 'image_url': 'https://i.postimg.cc/T1LrR1js/Hydrabad-Chicken-Biryani.jpg'},
        {'id': 2, 'name': 'Product 2', 'price': '24.50', 'image_url': 'https://i.postimg.cc/dVjnNWqS/dhokhla.jpg'},
        {'id': 3, 'name': 'Product 3', 'price': '45', 'image_url': 'https://i.postimg.cc/hPP9PSgM/alooparatha.jpg'},
        {'id': 4, 'name': 'Product 4', 'price': '86', 'image_url': 'https://i.postimg.cc/wBKyJHKC/sambar.jpg'},
        {'id': 5, 'name': 'Product 5', 'price':'20.50', 'image_url': 'https://i.postimg.cc/3xL75F1n/louis-hansel-dph-M2-U1xq0-U-unsplash.jpg'},
        {'id': 6, 'name': 'Product 6', 'price': '34.60', 'image_url': 'https://i.postimg.cc/zvPSYMLq/farhad-ibrahimzade-D5c9-Zci-Qy-I-unsplash.jpg'},
    ]
    user = request.session["email"]
    pro = cart.objects.filter(mail=user)
    product_ids = [p['pid'] for p in pro.values('pid')]
    products = []
    total_price = 0  # initialize total price to zero
    for product in Product:
        try:
            if product['id'] in product_ids:
                products.append(product)
                total_price += float(product['price'])  # add product price to total price
        except KeyError:
            pass
    return render(request, "cart.html", {"pro": products, "total_price": total_price})

def deletecartproduct(request,uid):
    cart.objects.filter(pid=uid).delete()
    return redirect("getcart")
def clearcartafterpayment(request):
    user = request.session["email"]
    cart.objects.filter(mail=user).delete()
    return redirect("index")

def leave_message(request):
    if request.method == 'POST':
        name = request.POST.get('contact-name')
        phone_number = request.POST.get('contact-phone')
        email = request.POST.get('contact-email')
        message = request.POST.get('contact-message')

        # Create a new ContactMessage object
        contact_message = ContactMessage(name=name, phone_number=phone_number, email=email, message=message)
        contact_message.save()

        return render(request,'index.html')

    return render(request, 'contact.html')
#
# def logined(request):
#     if request.method=='POST':
#         uname=request.POST["username"]
#         pass=request.POST["password1"]
#         request.session['id']=username
# def signout(request):
#     request.session.flush()
# def home(request):




