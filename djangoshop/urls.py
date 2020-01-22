from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('login', accounts.views.login, name = 'login' ),
    path('accounts/', include('allauth.urls')),
    
]
