from django.shortcuts import render, get_object_or_404
from .serializers import VocabularySerializer, SpeakingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Vocabulary, Speaking, Listening
from datetime import datetime
from django.utils.dateformat import DateFormat
from captioning import main as caption
from sound import gspeech as speech
from sound import testspeech2 as STT

# 출석부에 기능 이용 횟수를 저장하기 위해 accounts에서 DateCount를 가져옴
# 이 때, from [패키지명].models import [모델명(테이블명)] 의 형태로 가져온다
# ..[패키지명].models import [모델명] 의 형태인 경우
# ValueError: attempted relative import beyond top-level package 에러 발생
from accounts.models import DateCount

@api_view(['POST'])
def vocabulary(request):

    # 선택한 필드가 'True'인 단어 중에서 랜덤으로 20개 선정
    if 'Toeic' in request.data:
        vocas = Vocabulary.objects.filter(Toeic=True).order_by('?')[0:20]
    elif 'Opic' in request.data:
        vocas = Vocabulary.objects.filter(Opic=True).order_by('?')[0:20]
    elif 'korean_SAT' in request.data:
        vocas = Vocabulary.objects.filter(korean_SAT=True).order_by('?')[0:20]

    # 오늘 날짜를 함께 기록
    today = DateFormat(datetime.now()).format('Y-m-d')

    serializer = VocabularySerializer(vocas, many=True)

    # 날짜와 단어장을 함께 전송
    data = {
        "today": today,
        "vocabulary": serializer.data
    }

    # 기능 이용 카운트를 추가
    # 요청 보낸 유저 및 날짜에 맞는 테이블 체크
    user = request.user

    # DateCount.objects.filter()의 형태로 가져올 경우,
    # object가 아니라 QuerySet으로 가져옴
    # QuerySet 보다 object로 가져올 경우 수정이 쉽다
    day = get_object_or_404(DateCount, user=user, date=today)
    
    # 해당하는 기능에 카운트를 +1 하고 저장한다
    day.vocabulary_count += 1
    day.save()

    return Response(data)

@api_view(['POST'])
def speaking(request):
    speak = Speaking.objects.order_by('?')[0:1]
    for val in speak:
        # print(val)
        text = val.image
    return_text = caption.main(text)
    
    # print('텍스트 체크')
    # print(text)
    serializer = SpeakingSerializer(speak, many=True)
    data = {
        'return_text': return_text,
        'serializer': serializer.data
    }
    return Response(data)

@api_view(['POST'])
def do_captioning(request):
    text = caption.main("1.jpg")
    return Response(text)

@api_view(['PUT'])
def image_upload(request):
    # 저장할 db 호출
    speak = Speaking()

    # 전송받은 파일 저장
    speak.image = request.FILES['inputImage']
    speak.cap_text = 'test'
    speak.save()

    # 이미지 캡셔닝 모델 실행
    text = speak.image
    return_text = caption.main(text)

    # 기능 이용 카운트를 추가
    user = request.user
    today = DateFormat(datetime.now()).format('Y-m-d')

    # 테이블에서 해당하는 오브젝트를 가져옴
    day = get_object_or_404(DateCount, user=user, date=today)
    
    # 해당하는 기능에 카운트를 +1 하고 저장한다
    day.image_speak_count += 1
    day.save()

    # 결과물 전송
    return Response(return_text)

@api_view(['POST'])
def situation(request):
    text = speech.main()
    return Response(text)

@api_view(['PUT'])
def sound_upload(request):
    # 저장할 db 호출
    listen = Listening()

    # 전송받은 파일 저장
    listen.sound = request.FILES['inputFile']
    listen.extraction_text = 'test'
    listen.save()

    # STT 모델 가동
    text = listen.sound
    return_text = STT.main(text)
    # print(return_text)
    print(request.user)
    # 기능 이용 카운트를 추가
    user = request.user
    today = DateFormat(datetime.now()).format('Y-m-d')

    # 테이블에서 해당하는 오브젝트를 가져옴
    day = get_object_or_404(DateCount, user=user, date=today)
    
    # 해당하는 기능에 카운트를 +1 하고 저장한다
    day.listening_count += 1
    day.save()

    # 결과물 전송
    return Response(return_text)

@api_view(['POST'])
def checktext(request):
    sttText = list(map(str, request.data['STTtext'].split()))
    userText = list(map(str, request.data['usertext'].split()))
    data = {
        'usertext': userText,
        'stttext': sttText
    }
    return Response(data)