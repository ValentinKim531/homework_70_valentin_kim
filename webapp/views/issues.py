from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from webapp.forms import IssueForm
from webapp.models import Issue
from webapp.views.base import IndexView


class IssueCreateView(CreateView):
    template_name = 'issue_create.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDetail(DetailView):
    template_name = 'issue_view.html'
    model = Issue


class IssueDeleteView(DeleteView):
    template_name = 'issue_confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('index')
