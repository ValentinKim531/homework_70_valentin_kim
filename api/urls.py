from django.urls import path

from api.views import (
    IssueListView,
    ProjectListView,
    IssueDetailView,
    ProjectDetailView,
    UpdateIssue,
    UpdateProject,
    DeleteIssue,
    DeleteProject,
)

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="issues"),
    path("issue/<int:pk>", IssueDetailView.as_view(), name="issue_detail"),
    path("issue-update/<int:pk>", UpdateIssue.as_view(), name="issue_update"),
    path("issue-delete/<int:pk>", DeleteIssue.as_view(), name="issue_delete"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path(
        "project/<int:pk>", ProjectDetailView.as_view(), name="project_detail"
    ),
    path(
        "project-update/<int:pk>",
        UpdateProject.as_view(),
        name="project_update",
    ),
    path(
        "project-delete/<int:pk>",
        DeleteProject.as_view(),
        name="project_update",
    ),
]
