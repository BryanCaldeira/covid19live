from django.contrib import admin
from django.urls import path
from Main_Page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Main , name="main"),
    path('andhrapradesh/', views.Main),
    path('karnataka/', views.Main),
    path('tamilnadu/', views.Main),
    path('kerala/', views.Main),
    path('maharashtra/', views.Main),
    path('telangana/', views.Main),
    path('delhi/', views.Main),
    path('uttarpradesh/', views.Main),
    path('punjab/', views.Main),
    path('westbengal/', views.Main),

]
