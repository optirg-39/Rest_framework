from django.contrib import admin
from django.urls import path
from api.views import StudentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', StudentListView.as_view()),
]
