from django.contrib import admin
from django.urls import path
from api.views import studentapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/<int:pk>',studentapi ),
    path('studentapi/',studentapi ),
]
