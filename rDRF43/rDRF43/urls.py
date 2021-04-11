from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

"""Creating Router Object"""
router =DefaultRouter()

"""Register SingerModelViewSet and SongModelViweSet with router"""
router.register('singer',views.SingerModelViewSet, basename='singer')
router.register('song',views.SongModelViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]
