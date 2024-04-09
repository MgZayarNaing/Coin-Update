from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import  messages
from django.db.models import Q
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import JsonResponse
import random


# Create your views here.
def HomePage(request):
     return redirect('/home/')

def HeroSection(request):
        hero = HeroModel.objects.all().order_by('-time')
        return render(request, 'index.html',{"hero":hero})

def Register(request):
        if request.method == "GET":
                return render(request,'register.html')
        elif request.method == "POST":
                username = request.POST.get('username')
                email = request.POST.get('email')

                if User.objects.filter(email = email).exists():
                        messages.error(request,'Email already exists!')
                        return redirect('/register/')
                elif User.objects.filter(username = username).exists():
                        messages.error(request,'Username already exists!')
                        return redirect('/register/')
                else:
                    password = request.POST.get('password')
                    password_confirm = request.POST.get('passwordconfirm')
                    if password == password_confirm:
                        phone = request.POST.get('phone')
                        user1 = User.objects.create_user(
                            username = username,
                            password = password,
                            email = email,
                        )
                        user1.save()

                        user2 = UserModel.objects.create(
                            username = username,
                            email = email,
                            password = password,
                            phone = phone,
                        )
                        user2.save()
                        messages.success(request,"Account was created for "+username)
                        return redirect('/login/')
                    else:
                        messages.error(request,"Password does not match! Please check your password again!")
                        return redirect('/register/')
        else:
            messages.error(request,"Invalid request method!")

def LogIn(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user_name_or_email_check = User.objects.filter(
            Q(username = username_or_email) |
            Q(email = username_or_email)
        ).exists()

        if not user_name_or_email_check:
            messages.error(request,"Invalid username or email!")
            return redirect('/login/')
        else:
            user1 = User.objects.get(
                Q(username = username_or_email) |
                Q(email = username_or_email)
            )
            user2 = UserModel.objects.get(
                Q(username = username_or_email) |
                Q(email = username_or_email)
            )
            if user2.password == password:
                if user2.status == True:
                    login(request,user1)
                    if user1.username == "admin":
                        return redirect('/myadmin/dashboard/')
                    elif user1.email == "admin@gmail.com":
                        return redirect('/myadmin/dashboard/')
                    else:
                        messages.success(request,"Login Success")
                        return redirect('/home/')
                else:
                    messages.error(request,"Please Wait!")
                    return redirect('/login/')
            else:
                messages.error(request,"Invalid password! Please fill your password again correctly!")
                return redirect('/login/')
            
def LogOut(request):
     logout(request)
     return redirect('/home/')
     
     
def RoomChoice(request):
    if request.user.is_authenticated:
        try:
            myuser = UserModel.objects.get(email=request.user.email)
            coin = CoinModel.objects.get(customer_id=myuser.id)
        except Exception:
             coin = CoinModel.objects.all()
             coin.quantity = 0
        return render(request, 'room_choice.html', {"myuser": myuser, "coin": coin})
        
# def Balance(request):
#     if request.user.is_authenticated:
#         try:
#             myuser = UserModel.objects.get(email=request.user.email)
#             coin = CoinModel.objects.get(customer_id= myuser.id)
#             qr = QRModel.objects.all()
#         except Exception:
#             coin = None
#         return render(request, 'balance.html', {"myuser": myuser, "coin": coin,"qr":qr})
        # try:
        #     myuser = UserModel.objects.get(email=request.user.email)
        # except UserModel.MultipleObjectsReturned:
        #     myuser = UserModel.objects.filter(email=request.user.email).first()
        # except UserModel.DoesNotExist:
        #     messages.error(request, "User not found")
        #     return redirect('/home/')
        # try:
        #     coin = CoinModel.objects.get(customer_id=myuser.id)
        # except CoinModel.DoesNotExist:
        #     messages.error(request, "Coin not found")
        #     return redirect('/home/') 
        # return render(request, 'balance.html', {"myuser": myuser, "coin": coin})
    
def Balance(request):
    myuser = None
    coin = None

    if request.user.is_authenticated:
        try:
            myuser = UserModel.objects.get(email=request.user.email)
            coin = CoinModel.objects.get(customer_id=myuser.id)
        except (UserModel.DoesNotExist, CoinModel.DoesNotExist):
            pass
        except Exception as e:
            print(e)
    else:
        pass
    return render(request, 'balance.html', {"myuser": myuser, "coin": coin})


    
# def Deposit(request):
#      if request.method == "GET":
#           coin_type = CoinTypeModel.objects.all()
#           network_type = NetworkModel.objects.all()
#           current_user = UserModel.objects.get(email = request.user.email)
#           return render(request,'deposit.html',{"current_user":current_user,"coin_type":coin_type,"network_type":network_type})
#      if request.method == "POST":
#           current_user = UserModel.objects.get(email = request.user.email)
#           deposit = DepositModel.objects.create(
#                customer_id = current_user.id,
#                coin_type_id = request.POST.get('coin_type'),
#                network_type_id = request.POST.get('network_type'),
#                quantity = request.POST.get('quantity'),
#                screenshot = request.FILES.get('screenshot'),
#                time = datetime.now(),
#           )
#           deposit.save()
#           return redirect('/app/balance/')

def Deposit(request):
    if request.method == "GET":
        coin_type = CoinTypeModel.objects.all()
        network_type = NetworkModel.objects.all()
        # Use filter instead of get to handle potential multiple objects
        current_users = UserModel.objects.filter(email=request.user.email)
        if current_users.count() == 1:
            current_user = current_users.first()
            return render(request, 'deposit.html', {"current_user": current_user, "coin_type": coin_type, "network_type": network_type})
        elif current_users.count() > 1:
            # Handle multiple users with the same email
            # For example, raise an error or redirect to an error page
            raise Http404("Multiple users found with the same email.")
        else:
            # Handle the case where no user is found
            # For example, redirect to login page or show an error message
            raise Http404("User not found.")

    if request.method == "POST":
        current_users = UserModel.objects.filter(email=request.user.email)
        if current_users.count() == 1:
            current_user = current_users.first()
            deposit = DepositModel.objects.create(
                customer_id=current_user.id,
                coin_type_id=request.POST.get('coin_type'),
                network_type_id=request.POST.get('network_type'),
                quantity=request.POST.get('quantity'),
                screenshot=request.FILES.get('screenshot'),
                time=datetime.now(),
            )
            deposit.save()
            return redirect('/app/balance/')
        elif current_users.count() > 1:
            # Handle multiple users with the same email
            # For example, raise an error or redirect to an error page
            raise Http404("Multiple users found with the same email.")
        else:
            # Handle the case where no user is found
            # For example, redirect to login page or show an error message
            raise Http404("User not found.")
        
def GetQRLink(request):
    option_id = request.GET.get('option_id')
    option = NetworkModel.objects.get(pk=option_id)
    image_url = option.qrcode.url
    return JsonResponse({'image_url': image_url,'link_name': option.link_name,'link_address':option.link_address})
     
def Withdraw(request):
     if request.method == "GET":
          coin_type = CoinTypeModel.objects.all()
          network_type = NetworkModel.objects.all()
          current_user = UserModel.objects.get(email = request.user.email)
          return render(request,'withdraw.html',{"current_user":current_user,"coin_type":coin_type,"network_type":network_type})
     if request.method == "POST":
          current_user = UserModel.objects.get(email = request.user.email)
          withdraw = WithDrawModel.objects.create(
               customer_id = current_user.id,
               coin_type_id = request.POST.get('coin_type'),
               network_type_id = request.POST.get('network_type'),
               quantity = request.POST.get('quantity'),
               address = request.POST.get('address'),
               time = datetime.now(),
          )
          withdraw.save()
          return redirect('/app/balance/')

def NewMember(request):
     return render(request,"new_member.html")

def Intermediate(request):
     return render(request,"intermediate.html")

def Advanced(request):
     return render(request,"advanced.html")

def VIPRoom(request):
     return render(request,"vip_room.html")

     
def randomcreate(request):
    a = random.randint(1,20)
    b = random.randint(1,20)
    c = random.randint(1,20)
    ran = RandomModel.objects.create(
        a = a,
        b = b,
        c = c,
        room = 1,
        status = "free",
        roundno = random.randint(12345,99999)
        )
    ran.save()
    return render(request,"new_member.html")

def randomshow(request):
    ran2 = RandomModel.objects.filter(status="free",room=1)
    ran = ran2[0];
    result = int(ran.a) + int(ran.b) + int(ran.c)
    ran.status = "used"
    ran.save()
    return render(request,"new_member2.html",{"ran":ran,"result":result})




                

                        

