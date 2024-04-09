from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import Register,LogIn,HomePage,HeroSection,LogOut
urlpatterns = [
    # path('', lambda request: redirect('/app/blog/')),
    path("admin/", admin.site.urls),
    path(("app/"), include("myapp.urls")),
    path(("myadmin/"),include("myadmin.urls")),
    path('register/',Register),
    path('login/',LogIn),
    path('',HomePage),
    path('home/',HeroSection),
    path('logout/',LogOut),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
