
# matrimony_dj/urls.py
from django.contrib import admin
from django.urls import path
from . import views, settings  
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('', include('matrimony_dj.urls')) # This includes the URLs from the matrimony_dj app
# ]
