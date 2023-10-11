from .views import StudentListView, StudentDetailView
from django.urls import path
from . import views

urlpatterns = [
    # path function defines a url pattern
    # '' is empty to represent based path to app
    path('', views.index, name='index'),
    path('students/', StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student-detail')
]
