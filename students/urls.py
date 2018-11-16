from django.urls import path, reverse, reverse_lazy
from django.conf.urls import url
from . import views

app_name = "students"

urlpatterns = [
	path('assignments/', views.student_asmt, name='assignments'),
]