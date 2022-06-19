from django.urls import path
from products.views import product_list, index2, blog, contact, product_create, product_manager, product_update, product_delete
from products.views import register, connexion, deconnection
from django.contrib.auth import views

urlpatterns = [
    path('', product_list, name='index'),
    path('manager/', product_manager, name='manager'),
    path('create/', product_create, name='create'),
    path('update/<int:pk>', product_update, name='update'),
    path('delete/<int:myid>', product_delete, name='delete'),
    # user url
    path('register/', register, name='register'),
    path('login/', connexion, name='login'),
    path('logout/', deconnection, name='logout'),
    
    path('reset_password', views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name='user/password_reset_send.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='user/password_reset_from.html'), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='user/password_reset_done.html'), name='password_reset_complete')
]




