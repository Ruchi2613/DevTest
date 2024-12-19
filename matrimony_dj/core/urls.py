
# matrimony_dj/urls.py
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'), 
]



# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('', include('matrimony_dj.urls')) # This includes the URLs from the matrimony_dj app
# ]
