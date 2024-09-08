from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Base.urls')),
    path('administrativo/', include('Adm.urls')),
    path('controle/', include('Controle.urls')),
]
