from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views
from . import api_views


router = routers.DefaultRouter()
router.register(r'requests', api_views.RequestViewSet, base_name="request")

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^', include(router.urls)),
    ]
