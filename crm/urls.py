from . import views
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views


app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('student_list', views.student_list, name='student_list'),
    path('event_list', views.event_list, name='event_list'),
    path('club_list', views.club_list, name='club_list'),
    path('meal_list', views.meal_list, name='meal_list'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('club/<int:pk>/edit/', views.club_edit, name='club_edit'),
    path('club/<int:pk>/delete/', views.club_delete, name='club_delete'),
    path('meal/<int:pk>/edit/', views.meal_edit, name='meal_edit'),
    path('meal/<int:pk>/delete/', views.meal_delete, name='meal_delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls'))
]


