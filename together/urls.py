from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views 
 
from django.conf import settings 
from django.conf.urls.static import static 
from users import views as u_views 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('register/', u_views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), 
    path('delete/<int:id>/', u_views.user_delete,  name='delete-user'), 
    path('profile/', u_views.profile, name='profile'), 
 
 
    path('', include('blog.urls')), 
 
] 
 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)