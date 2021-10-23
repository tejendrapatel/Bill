from django.contrib import admin
from django.urls import path
from patelbill.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name= 'home'),
    path('', LOGIN, name='Login'),
    path('forgot/', Forgot, name='forgot'),
    path('signup', Signup, name='signup'),
    path('Logout/', LOGOUT, name='Logout'),
    path('main/', Main, name='Mainn'),
    path('deleteblog/<int:pid>/', delete_blog, name='deleteblog'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

