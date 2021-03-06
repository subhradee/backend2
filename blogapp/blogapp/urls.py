"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
router = DefaultRouter()
router.register('blogs', views.BlogPostApi, basename="api")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserView.as_view()),
    path('userget/', views.UserGet.as_view()),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
    path('', include(router.urls)),
]
