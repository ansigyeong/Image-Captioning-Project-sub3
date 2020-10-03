from django.shortcuts import render, get_object_or_404
from .serializers import NoticeSerializer, NoticeListSerializer, SuggestionSerializer, SuggestionListSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notice, Suggestion, Comment
from django.contrib import messages
from accounts.models import User

@api_view(['GET'])
def notice_list(request):
    notices = Notice.objects.all()
    serializer = NoticeListSerializer(notices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def noticecheck(request):
    user = get_object_or_404(User, username = request.user)
    if user.username == 'admin':
        return Response('통과')
    else:
        return Response('실패')


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

@api_view(['POST'])
def notice_update(request, notice_pk):
    # 수정시에는 해당 article 인스턴스를 넘겨줘야한다!
    notice = get_object_or_404(Notice, pk=notice_pk)
    if request.user == notice.user:
        if request.data['title']:
            notice.title = request.data['title']
            notice.content = request.data['content']
            notice.save()
            return Response('성공')
        else:
            form = notice(instance=notice)
        context = {
            'title': notice.title,
            'content': notice.content,
        }
        return Response(context)
    else:
        # 1. 메시지프레임워크를 사용하여, 메인페이지로 이동.
        return Response('본인이 작성한 글만 수정할 수 있습니다.')
        # 2. 403 status code를 반환.
        # return HttpResponseForbidden()

@api_view(['POST'])
def suggestion_list(request):
    print(request.user)
    user = get_object_or_404(User, username = request.user)
    if user.username == 'admin':
        suggestions = Suggestion.objects.all()
    else:
        suggestions = Suggestion.objects.filter(user=request.user)
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
    comment_serializer = CommentSerializer(comments, many=True)
    data = {
        'suggestion': serializer.data,
        'comments': comment_serializer.data
    }
    return Response(data)


@api_view(['DELETE'])
def suggestion_delete(request, suggestion_pk):
    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)
    suggestion.delete()
    return

@api_view(['POST'])
def suggestion_update(request, suggestion_pk):
    # 수정시에는 해당 article 인스턴스를 넘겨줘야한다!
    suggestion = get_object_or_404(Suggestion, pk=suggestion_pk)
    if request.user == suggestion.user:
        if request.data['title']:
            suggestion.title = request.data['title']
            suggestion.content = request.data['content']
            suggestion.save()
            return Response('성공')
        else:
            form = Suggestion(instance=suggestion)
        context = {
            'title': suggestion.title,
            'content': suggestion.content,
        }
        return Response(context)
    else:
        # 1. 메시지프레임워크를 사용하여, 메인페이지로 이동.
        return Response('본인이 작성한 글만 수정할 수 있습니다.')
        # 2. 403 status code를 반환.
        # return HttpResponseForbidden()

@api_view(['POST'])
def commentcreate(request, suggestion_pk):
    comment = Comment()
    comment.user = request.user
    suggestion = get_object_or_404(Suggestion, pk = suggestion_pk)
    comment.suggestion = suggestion
    comment.content = request.data['content']
    comment.save()
    return Response('성공')