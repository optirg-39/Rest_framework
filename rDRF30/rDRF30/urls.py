from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# '''Creating router object'''
router = DefaultRouter()

# '''Register StudentsViewSet with Router '''
# router.register('pyth',views.StudentsViewSet, basename='student')

router.register(r'studentapi', views.StudentModelViewSet, basename='StudentsViewSet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("gettoken/", TokenObtainPairView.as_view(), name="Access_Token"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="Refresh_Token"),
    path("verifytoken/", TokenVerifyView.as_view(), name="Verify_Token"),

]
