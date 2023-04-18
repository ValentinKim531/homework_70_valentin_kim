from rest_framework import serializers
from webapp.models import Issue, Project


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'type', 'status', 'project')
        read_only_fields = ('id',)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'start_date', 'end_date', 'title', 'description', 'users')
        read_only_fields = ('id',)