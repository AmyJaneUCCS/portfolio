from .views import StudentListView, StudentDetailView, PortfolioListView, PortfolioDetailView, ProjectListView, ProjectDetailView
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
    path('projects/', ProjectListView.as_view(), name= 'projects'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
    path('portfolio/<int:portfolio_id>/delete_project/<int:project_id>', views.deleteProject, name='delete_project'),
    path('portfolio/<int:portfolio_id>/update_portfolio/', views.updatePortfolio, name='update_portfolio'),
]
