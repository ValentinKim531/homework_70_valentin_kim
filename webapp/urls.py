from django.urls import path

from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.issues import (
    IssueDetail, IssueCreateView, IssueUpdateView, IssueDeleteView,
)

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
]
