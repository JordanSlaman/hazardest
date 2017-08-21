from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

# from views import index, play
import viewsets as CoreViewSets

router = routers.DefaultRouter()

router.register(r'session', CoreViewSets.SessionViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]