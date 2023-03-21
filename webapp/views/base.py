from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import RedirectView, ListView
from webapp.forms import SimpleSearchForm
from webapp.models import Issue, Project
from webapp.views.issues import GroupPermissionMixin


class IndexView(ListView):
    context_object_name = "issues"
    model = Issue
    template_name = "index.html"
    ordering = ["-created_at"]
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.object_list = self.get_queryset()
        self.allow_empty = self.get_allow_empty()

        if self.allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                context = super().get_context_data(
                    object_list=self.object_list, **kwargs
                )
                context["form"] = self.form
                context["text"] = "Задачи не найдены"
                print("test")
                return self.render_to_response(context)
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form

        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(
                description__icontains=self.search_value
            )
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None


class IndexRedirectView(RedirectView):
    pattern_name = "index"


class ProjectView(ListView):
    context_object_name = "projects"
    model = Project
    template_name = "index_projects.html"
    ordering = ["-start_date"]


class ProjectRedirectView(RedirectView):
    pattern_name = "index_projects"


