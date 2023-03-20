from django.urls import path

from webapp.views.base import IndexView, IndexRedirectView, ProjectRedirectView, ProjectView
from webapp.views.issues import (
    IssueDetail,
    IssueCreateView,
    IssueUpdateView,
    IssueDeleteView, ProjectIssueCreateView,
)
from webapp.views.projects_view import ProjectDetail, ProjectCreateView

app_name = 'webapp'


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "issue/",
        IndexRedirectView.as_view(),
        name="issue_index_redirect",
    ),
    path("issue/add", IssueCreateView.as_view(), name="issue_add"),
    path(
        "issue/<int:pk>",
        IssueDetail.as_view(),
        name="issue_detail",
    ),
    path(
        "issue/<int:pk>/delete/",
        IssueDeleteView.as_view(),
        name="issue_delete",
    ),
    path(
        "issue/<int:pk>/confirm_delete/",
        IssueDeleteView.as_view(),
        name="confirm_delete",
    ),
    path(
        "issue/<int:pk>/update/",
        IssueUpdateView.as_view(),
        name="issue_update",
    ),
    path("projects/", ProjectView.as_view(), name="index_projects"),
    path(
        "projects/list/",
        ProjectRedirectView.as_view(),
        name="project_index_redirect",
    ),
    path(
        "project/<int:pk>",
        ProjectDetail.as_view(),
        name="project_detail",
    ),
    path(
        "project/add",
        ProjectCreateView.as_view(),
        name="project_add",
    ),
    path(
        'project/<int:pk>/issues/add/',
        ProjectIssueCreateView.as_view(),
        name='project_issue_add'
    ),
]
