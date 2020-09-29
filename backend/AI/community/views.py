from django.shortcuts import render, get_object_or_404
from .serializers import NoticeSerializer, NoticeListSerializer, SuggestionSerializer, SuggestionListSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notice, Suggestion, Comment
from django.contrib import messages


@api_view(['GET'])
def notice_list(request):
    notices = Notice.objects.all()
    serializer = NoticeListSerializer(notices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def notice_create(request):
    notice = Notice()
    notice.title = request.data['title']
    notice.content = request.data['content']
    notice.user = request.user
    notice.save()
    return Response('성공')


@api_view(['GET'])
def notice_detail(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)
    serializer = NoticeSerializer(notice)
    return Response(serializer.data)


@api_view(['DELETE'])
def notice_delete(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)
    notice.delete()
    return

@api_view(['PATCH'])
def notice_update(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)
    notice.title = request.POST.get('title')
    notice.content = request.POST.get('content')
    notice.save()
    return Response('성공')

@api_view(['GET'])
def suggestion_list(request):
    suggestions = Suggestion.objects.all()
    serializer = SuggestionListSerializer(suggestions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggestion_create(request):
    suggestion = Suggestion()
    suggestion.title = request.data['title']
    suggestion.content = request.data['content']
    suggestion.user = request.user
    suggestion.finish = False
    suggestion.save()
    return Response('성공')


@api_view(['GET'])
def suggestion_detail(request, suggestion_pk):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)
    comments = suggestion.comment_set.all()
    serializer = SuggestionSerializer(suggestion)
    return Response(serializer.data)


@api_view(['DELETE'])
def suggestion_delete(request, suggestion_pk):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)
    suggestion.delete()
    return

@api_view(['PATCH'])
def suggestion_update(request, suggestion_pk):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)
    suggestion.title = request.POST.get('title')
    suggestion.content = request.POST.get('content')
    suggestion.save()
    return Response('성공')
