from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import IssueSerializer, ProjectSerializer
from webapp.models import Issue, Project


class IssueListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all()
        serializer = IssueSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueDetailView(APIView):
    def get(self, request, pk):
        try:
            object = Issue.objects.get(pk=pk)
            serializer = IssueSerializer(object)
            return Response(serializer.data)
        except Issue.DoesNotExist:
            raise Http404


class ProjectDetailView(APIView):
    def get(self, request, pk):
        try:
            object = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(object)
            return Response(serializer.data)
        except Project.DoesNotExist:
            raise Http404


class UpdateIssue(APIView):
    def put(self, request, pk):
        object = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProject(APIView):
    def put(self, request, pk):
        object = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteIssue(APIView):
    def delete(self, request, pk):
        try:
            object = Issue.objects.get(pk=pk)
            id = object.pk
            object.delete()
            return Response(
                {"Задача была успешно удалена, со следующим ID:": id},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Issue.DoesNotExist:
            raise Http404


class DeleteProject(APIView):
    def delete(self, request, pk):
        try:
            object = Project.objects.get(pk=pk)
            id = object.pk
            object.delete()
            print(object.pk)
            return Response(
                {"Проект был успешно удален, со следующим ID:": id},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Project.DoesNotExist:
            raise Http404
