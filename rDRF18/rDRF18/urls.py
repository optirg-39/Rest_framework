from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# '''Creating router object'''
router = DefaultRouter()

# '''Register StudentsViewSet with Router '''
# router.register('pyth',views.StudentsViewSet, basename='student')

router.register(r'studentapi', views.StudentModelViewSet, basename='StudentsViewSet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
