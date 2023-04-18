from django.urls import path

from api.views import IssueListView, ProjectListView, IssueDetailView, ProjectDetailView

urlpatterns = [
    path("issues/", IssueListView.as_view(), name='issues'),
    path("issue/<int:pk>", IssueDetailView.as_view(), name='issue_detail'),
    path("projects/", ProjectListView.as_view(), name='projects'),
    path("project/<int:pk>", ProjectDetailView.as_view(), name='project_detail'),
]