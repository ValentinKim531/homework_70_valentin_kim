from django.contrib import admin

from .models import Issue, Status, Type, Project


# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "summary",
        "description",
        "status",
        "get_type",
        "project",
    )
    list_filter = ("id", "summary", "description")
    search_fields = ("summary", "description")
    fields = ("summary", "description", "status", "type", "project")
    readonly_fields = ("id", "created_at", "updated_at")

    def get_type(self, instance):
        return [type.name for type in instance.type.all()]


admin.site.register(Issue, IssueAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("id", "name")
    search_fields = ("name",)
    fields = ("name",)
    readonly_fields = ("id", "created_at")


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("id", "name")
    search_fields = ("name",)
    fields = ("name",)
    readonly_fields = ("id", "created_at")


admin.site.register(Status, StatusAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "start_date",
        "end_date",
        "title",
        "description",
    )
    list_filter = ("id", "title",)
    search_fields = ("title",)
    fields = (
        "start_date",
        "end_date",
        "title",
        "description",
    )
    readonly_fields = ("id",)


admin.site.register(Project, ProjectAdmin)