from django.urls import path
from .views import views_roles

urlpatterns = [
    path('api/roles', views_roles.roles_list),
    path('api/roles/<int:pk>/', views_roles.roles_detail),
]