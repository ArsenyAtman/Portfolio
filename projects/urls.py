from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProjectList.as_view(), name='home'),
    path('about/', views.AboutDetail.as_view(), name='about'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
]
