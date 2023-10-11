from .views import StudentListView, StudentDetailView, PortfolioListView, PortfolioDetailView
from django.urls import path
from . import views

urlpatterns = [
    # path function defines a url pattern
    # '' is empty to represent based path to app
    path('', views.index, name='index'),
    path('students/', StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('portfolios/', PortfolioListView.as_view(), name= 'portfolios'),
    path('portfolio/<int:pk>', PortfolioDetailView.as_view(), name='portfolio-detail'),
]
