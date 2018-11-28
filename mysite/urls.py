from django.contrib import admin
from django.urls import path
from rest_framework import routers
from blog.models import Perro
from blog import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register( r'perro', views.PerroViewSet )

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    url( r'^', include( router.urls ) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
