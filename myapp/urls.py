from django.urls import path
from myapp import views

urlpatterns = [
    path('room_choice/',views.RoomChoice),
    path('balance/',views.Balance),
    path('deposit/',views.Deposit),
    path('get_qr_link/', views.GetQRLink),
    path('withdraw/',views.Withdraw),
    path('new_member/',views.NewMember),
    path('intermediate/',views.Intermediate),
    path('advanced/',views.Advanced),
    path('vip_room/',views.VIPRoom),
    path('randomc/',views.randomcreate,name="randomc"),
    path('randoms/',views.randomshow,name="randoms"),

]