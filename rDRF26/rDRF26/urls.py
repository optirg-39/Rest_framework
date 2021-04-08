from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken


# '''Creating router object'''
router = DefaultRouter()

# '''Register StudentsViewSet with Router '''
# router.register('pyth',views.StudentsViewSet, basename='student')

router.register(r'studentapi', views.StudentModelViewSet, basename='StudentsViewSet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/',CustomAuthToken.as_view()),
]
