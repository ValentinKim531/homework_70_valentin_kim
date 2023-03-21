from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from webapp.forms import IssueForm
from webapp.models import Issue, Project


class GroupPermissionMixin(UserPassesTestMixin):
    pass
    # def test_func(self):
    #     return self.request.user.groups.filter(name__in=['manager', 'lead', 'dev']).exists()


class IssueCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "issue_create.html"
    model = Issue
    form_class = IssueForm
    success_message = 'Issue is added.'

    def get_success_url(self):
        return reverse("webapp:issue_detail", kwargs={"pk": self.object.pk})


class IssueUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "issue_update.html"
    form_class = IssueForm
    model = Issue
    success_message = 'Issue is updated'

    def get_success_url(self):
        return reverse("webapp:issue_detail", kwargs={"pk": self.object.pk})


class IssueDetail(DetailView):
    template_name = "issue_view.html"
    model = Issue


class IssueDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = "issue_confirm_delete.html"
    model = Issue
    success_url = reverse_lazy("webapp:index")
    success_message = 'Issue is deleted.'


class ProjectIssueCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Issue
    template_name = 'issue_create.html'
    form_class = IssueForm
    success_message = 'Issue in Project is created.'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:issue_detail", kwargs={"pk": self.object.pk})

