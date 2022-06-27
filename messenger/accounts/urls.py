from django.urls import path
from . import views
 
app_name='accounts'

urlpatterns = [
    path('register/',views.user_register,name='user_register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name='profile'),
    path('update/',views.update,name='update'),
    path('history/',views.order_history,name='order_history'),
    path('change_password/',views.change_password,name='change'),
]