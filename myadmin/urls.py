from django.shortcuts import redirect
from django.urls import path, include
from myadmin import views

urlpatterns = [
    path('dashboard/',views.AdminHome),
    path('user_list/',views.UserList),
    path('user_coin/',views.UserCoin),
    path('admin_register_confirm/<int:currentuser_id>/',views.AdminRegisterConfirm),
    path('admin_register_destroy/<int:currentuser_id>/',views.AdminRegisterDestroy),
    path('admin_add_coin/',views.AdminAddCoin),
    path('admin_edit_coin/<int:cn_id>/',views.AdminEditCoin),
    path('view_deposit/',views.ViewDeposit),
    path('approve_deposit/<int:d_id>/',views.ApproveDeposit),
    path('view_withdraw/',views.ViewWithDraw),
    path('approve_withdraw/<int:w_id>/',views.ApproveWithdraw),
    path('network_create/',views.NetworkCreate),
    path('network_list/',views.NetworkList),
    path('network_update/<int:n_id>/',views.NetworkUpdate),
    path('network_delete/<int:n_id>/',views.NetworkDelete),
]