"""sismgca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from equipamentos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexListView.as_view(), name='listar_disponibilidade'),
    path('mudar/par2000t/<pk>', Par2000TUpdate.as_view(), name='mudar_par2000t'),
    path('mudar/consoles/<pk>', ConsolesUpdate.as_view(), name='mudar_consoles'),
    path('mudar/radios/<pk>', RadiosUpdate.as_view(), name='mudar_radios'),
    path('mudar/centralaudio/<pk>', CentralAudioUpdate.as_view(), name='mudar_centralaudio'),
    path('mudar/diversos/<pk>', DiversosUpdate.as_view(), name='mudar_diversos'),
    path('mudar/ems/<pk>', EmsUpdate.as_view(), name='mudar_ems'),
    path('mudar/telefonia/<pk>', TelefoniaUpdate.as_view(), name='mudar_telefonia'),
]
