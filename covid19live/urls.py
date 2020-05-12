from django.contrib import admin
from django.urls import path
from Main_Page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Main , name="main"),
    path('karnataka/', views.Karnataka),
    path('tamilnadu/', views.Tamilnadu),
    path('kerala/', views.Kerala),
    path('andhrapradesh/', views.AndhraPradesh),
    path('maharashtra/', views.Maharashtra),
    path('telangana/', views.Telangana),

]
