from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.home, name="home"),
    path('guntur/', views.guntur, name="guntur"),
    path('EastGodavari/', views.EG, name="eg"),
    path('admin/', admin.site.urls),

]
