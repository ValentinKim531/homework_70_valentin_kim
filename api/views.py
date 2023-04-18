from django.http import JsonResponse, Http404
from django.views import View
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