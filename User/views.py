from django.shortcuts import render, redirect
from Admin.models import Category, Watch,Payment
from User.models import UserInfo, MyCard,OrderMaster ,Review, CheckoutDetail,Order,Contact
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    category = Category.objects.all()
    watch = Watch.objects.all()
    return render(request, "master.html", {"watches": watch, "categorys": category})


def women(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=2)
    return render(request, "women.html", {"watches": watch, "categorys": category})

def men(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=1)
    return render(request, "men.html", {"watches": watch, "categorys": category})

def about(request):
    category = Category.objects.all()
    return render(request, "about.html", { "categorys": category})

def forHerCASULE(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=2,Type=4)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHerINVOGUE(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=2,Type=1)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHerFITNESS(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=2,Type=2)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHerCLASSY(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=2,Type=3)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHerADVENTUROUS(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=2,Type=5)
    return render(request, "master.html", {"watches": watch, "categorys": category})


def forHimCASULE(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=1,Type=4)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHimINVOGUE(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=1,Type=1)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHimFITNESS(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=1,Type=2)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHimCLASSY(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=1,Type=3)
    return render(request, "master.html", {"watches": watch, "categorys": category})

def forHimADVENTUROUS(request):
    category = Category.objects.all()
    watch = Watch.objects.filter(gender=1,Type=5)
    return render(request, "master.html", {"watches": watch, "categorys": category})


def ShowCategory(request, id):
    category = Category.objects.all()
    watch = Watch.objects.filter(category=id)
    return render(request, "master.html", {"watches": watch, "categorys": category})


def ViewDetails(request, id):    
    category = Category.objects.all()
    watch = Watch.objects.get(id=id)
    reviews = Review.objects.filter(Watch=watch)
    if request.method=="POST":
        content = request.POST['content']
        if (content != ""):
            if ("email" in request.session):
                review = Review(user=UserInfo.objects.get(email=request.session["email"]), content=content, Watch=watch )
                review.save()
                return redirect(f"/ViewDetails/{id}")
            else:
                return redirect(Login)
    return render(request, "ViewDetails.html", {"watch": watch, "categorys": category,"reviews" : reviews})

def search(request):
    category = Category.objects.all()
    watch = Watch.objects.all()
        
    if request.method == "POST":
        category = Category.objects.all()
        search=request.POST['search']
        watch = Watch.objects.filter(watch_model=search)
        return render(request, "master.html", {"watches": watch, "categorys": category})
    else:
        return redirect(home)

    
def SignUp(request):
    category = Category.objects.all()
    if (request.method == "GET"):
        return render(request, "signup.html", {"categorys": category})

    else:
        name =request.POST["name"]
        phone_number=request.POST["PhoneNo"]
        email = request.POST["email"]
        password = request.POST["pwd"]
        password2 = request.POST["pwd2"]
        if password != password2:        
            messages.success(request, "Passwords do not match each other")
            return render(request, "signup.html", {"categorys": category})
        try:
            # is user allready exsist
            user = UserInfo.objects.get(username=email)

        except:
            # is user not exsist,create new user
            user = UserInfo(name, email, password, phone_number)
            user.save()
            return redirect(Login)
        else:
            message = "Thes user Alreday Exsist"
            return render(request, "signup.html", {"message": message , "categorys": category})


def Login(request):
    category = Category.objects.all()
    if (request.method == "GET"):
        return render(request, "login.html", {"categorys": category})
    else:
        email = request.POST['email']
        pwd = request.POST['pwd']

        try:
            u = UserInfo.objects.get(email=email, password=pwd)
        except:
            msg = "Invalid User , Plz Try Again"
            return render(request, "login.html", {'msg': msg , "categorys": category})

        else:
            user = UserInfo.objects.get(email=email, password=pwd)
            name = user.name
            request.session["name"] = name
            request.session["email"] = email
            return redirect(home)


def SignOut(request):
    
    request.session.clear()
    return redirect(home)


def ShowCard(request):
    category = Category.objects.all()
    if (request.method == "GET"):
        items = MyCard.objects.filter(user_id=request.session["email"])
        total = 0
        for item in items:
            total += item.qty * item.Watch.price
        request.session["total"] = total
        return render(request, "ShowCard.html", {"items": items , "categorys": category})

    else:
        card_id = request.POST["wid"]
        item = MyCard.objects.get(id=card_id)
        action = request.POST["action"]
        if (action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(ShowCard)


def AddToCard(request):                  
    if ("email" in request.session):
        # get user info
        user = UserInfo.objects.get(email=request.session["email"])
        Watch_id = request.POST["wid"]
        watch = Watch.objects.get(id=Watch_id)
        qty = request.POST["qty"]
        

        try:
            card=MyCard.objects.get(user = user, Watch = watch)
        except:
            card = MyCard()
            card.user = user
            card.Watch = watch
            card.qty = qty
           
            card.save()
            
            return redirect(ShowCard)
        else:
            
            return redirect(ShowCard)
    else:
        return redirect(Login)

def MakePayment(request):
    if (request.method=="GET"):
        return render(request,"makepayment.html")
    else:
        CardNo=request.POST["cardno"]
        Cvv=request.POST["cvv"]
        Expiry=request.POST["expiry"]
        try:
            buyer=Payment.objects.get(card_no=CardNo,cvv=Cvv,expiry=Expiry)
        except:
            return redirect(MakePayment)
        else:
            owner=Payment.objects.get(card_no="222",cvv="222",expiry="12/2026")
            buyer.balance-=request.session["total"]
            owner.balance+=request.session["total"]
            buyer.save()
            owner.save()
            
            OM=OrderMaster()
            OM.user=UserInfo.objects.get(email=request.session["email"])
            OM.amount=request.session["total"]
            items = MyCard.objects.filter(user_id=request.session["email"])
            details = ""
            count=0
            for item in items:
                count+=1
                details+= str(count)+"."+item.Watch.watch_model+" -->"+ str(item.qty)+"/n"
                item.delete()
            
            OM.details=details
            OM.save()

            return redirect(OrderView)
            
def checkout(request):
    category = Category.objects.all()    
    if ("email" in request.session):
        # get user info
        user=UserInfo.objects.get(email=request.session["email"])
        items = MyCard.objects.filter(user_id = request.session["email"])        
        total = request.session["total"]
        if (request.method=="GET"):
            return render(request, "checkout.html", {'items':items , "categorys": category})
        
        else:
            try:
                city = request.POST['city']
            except MultiValueDictKeyError:
                city = False

            try:
                state = request.POST['state']
            except MultiValueDictKeyError:
                state = False

            
            try:
                zipcode = request.POST['zipcode']
            except MultiValueDictKeyError:
                zipcode = False

            try:
                address = request.POST['address']
            except MultiValueDictKeyError:
                address = False 

            try:
                phone_number = request.POST['phone_number']
            except MultiValueDictKeyError:
                phone_number = False

            try:
                payment_method = request.POST['payment_method']
            except MultiValueDictKeyError:
                payment_method  = False    
            
            shipping_adress = CheckoutDetail.objects.create(address=address, city=city, phone_number=phone_number,orderdate=datetime.now(), state=state, zipcode=zipcode, total_amount=total)
            shipping_adress.save()            
            user=UserInfo.objects.get(email=request.session["email"])            
            items = MyCard.objects.filter(user_id=request.session["email"])
            
            for item in items:                               
                order=Order.objects.create(user=user, checkoutdetail=shipping_adress,watch=item.Watch,qty = item.qty,amount=(item.Watch.price*item.qty),payment_method=payment_method)
                order.save()
            return redirect(MakePayment)
        
    else:
        return redirect(Login)

def OrderView(request):
    if ("email" in request.session):        
        order = Order.objects.filter(user_id=request.session["email"], delivery_date__gte= datetime.now()).order_by('-delivery_date')
           
        category = Category.objects.all()
    
        if(request.method=="GET"):
            return render(request, "orderview.html", {"orders": order, "categorys": category})
        
        else:
            order_id = request.POST["oid"]
            order = Order.objects.get(id=order_id)
            amount=request.POST["amount"]
            action = request.POST["action"]
            if (action == "remove"):
                owner=Payment.objects.get(card_no="222",cvv="222",expiry="12/2026")
                buyer=Payment.objects.get(card_no="111",cvv="111",expiry="12/2026")
               
                buyer.balance = float(buyer.balance) + float(amount)
                owner.balance = float(owner.balance) - float(amount)
                buyer.save()
                owner.save()
                order.delete()
                return redirect(OrderView)

    else:
        return redirect(Login)


def contact(request):
    category = Category.objects.all()
    if request.method=="POST":       
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        alert = True
        return render(request, 'contactUs.html', {"categorys": category,'alert':alert})
    return render(request, "contactUs.html",{"categorys": category})
