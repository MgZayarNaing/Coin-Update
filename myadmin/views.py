from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import  messages
from django.db.models import Q
from datetime import datetime

def AdminHome(request):
    return render(request,'admin_base.html')

def AdminRegisterConfirm(request,currentuser_id):
    if request.method == "POST":
        myuser = UserModel.objects.get(id = currentuser_id)
        myuser.status = True
        myuser.save()
        return redirect('/myadmin/user_list/')

def AdminRegisterDestroy(request,currentuser_id):
    if request.method == "POST":
        myuser = UserModel.objects.get(id = currentuser_id)
        myuser.status = False
        myuser.save()
        return redirect('/myadmin/user_list/')

def UserList(request):
    myuser = UserModel.objects.all().order_by('-time','status')
    return render(request,'user_list.html',{"myuser":myuser})

def AdminAddCoin(request):
     if request.method == "GET":
        customer = UserModel.objects.filter(coin_status = False)
        coin_type = CoinTypeModel.objects.all()
        network_type = NetworkModel.objects.all()
        return render(request,'admin_add_coin.html',{"customer":customer,"network_type":network_type,"coin_type":coin_type})
     if request.method == "POST":
        customer = UserModel.objects.get(id=request.POST.get('customer'))
        coin = CoinModel.objects.create(
             quantity = request.POST.get('quantity'),
             customer_id = request.POST.get('customer'),
             coin_type_id = request.POST.get('coin_type'),
             network_type_id = request.POST.get('network_type'),
             time = datetime.now(),
        )
        customer.coin_status = True
        customer.save()
        coin.save()
        return redirect('/myadmin/user_coin/')
     
def AdminEditCoin(request,cn_id):
     if request.method == "GET":
          coin = CoinModel.objects.get(id = cn_id)
          return render(request,'admin_edit_coin.html',{"coin":coin})
     if request.method == "POST":
          coin = CoinModel.objects.get(id = cn_id)
          coin.quantity = request.POST.get('balance')
          coin.save()
          return redirect('/myadmin/user_coin/')
     
def UserCoin(request):
    coin = CoinModel.objects.all()
    return render(request,'user_coin.html',{"coin":coin})

def ViewDeposit(request):
    deposit = DepositModel.objects.all()
    return render(request,'view_deposit.html',{"deposit":deposit})

def ApproveDeposit(request,d_id):
    if request.method == "POST":
        deposit = DepositModel.objects.get(id = d_id)
        deposit.status = True
        deposit.save()
        return redirect('/myadmin/view_deposit/')
    
def ViewWithDraw(request):
    withdraw = WithDrawModel.objects.all()
    return render(request,'view_withdraw.html',{"withdraw":withdraw})

def ApproveWithdraw(request,w_id):
    if request.method == "POST":
        widthdraw = WithDrawModel.objects.get(id = w_id)
        widthdraw.status = True
        widthdraw.save()
        return redirect('/myadmin/view_withdraw/')

def NetworkCreate(request):
    if request.method == "GET":
        return render(request,"network_create.html")
    if request.method == "POST":
        network = NetworkModel.objects.create(
            type = request.POST.get('type'),
            qrcode = request.FILES.get('qrcode'),
            link_name = request.POST.get('link_name'),
            link_address = request.POST.get('link_address'),
            time = datetime.now(),
        )
        network.save()
        return redirect('/myadmin/network_list/')

def NetworkList(request):
    network = NetworkModel.objects.all().order_by('-time')
    return render(request,'network_list.html',{"network":network})

def NetworkUpdate(request,n_id):
    if request.method == "GET":
        network = NetworkModel.objects.get(id = n_id)
        return render(request,"network_update.html",{"network":network})
    if request.method == "POST":
        network = NetworkModel.objects.get(id = n_id)
        network.type = request.POST.get('type')
        if request.FILES.get('qrcode'):
            network.qrcode.delete()
            network.qrcode = request.POST.get('qrcode')
        network.link_name = request.POST.get('link_name')
        network.link_address = request.POST.get('link_address')
        network.save()
        return redirect('/myadmin/network_list/')
    
def NetworkDelete(request,n_id):
    network = NetworkModel.objects.get(id = n_id)
    if request.FILES.get('qrcode'):
        network.qrcode.delete()
    network.delete()
    return redirect('/myadmin/network_list/')