from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from webapp.forms import IssueForm
from webapp.models import Issue, Project


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issue_create.html"
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse("issue_detail", kwargs={"pk": self.object.pk})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "issue_update.html"
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse("issue_detail", kwargs={"pk": self.object.pk})


class IssueDetail(DetailView):
    template_name = "issue_view.html"
    model = Issue


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "issue_confirm_delete.html"
    model = Issue
    success_url = reverse_lazy("index")


class ProjectIssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issue_create.html'
    form_class = IssueForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return redirect('issue_detail', pk=issue.pk)