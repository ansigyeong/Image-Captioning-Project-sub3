from django.shortcuts import render
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

    return Response(data)

@api_view(['POST'])
def speaking(request):
    speak = Speaking.objects.order_by('?')[0:1]
    for val in speak:
        print(val)
        text = val.image
    return_text = caption.main(text)
    
    print('텍스트 체크')
    print(text)
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
    print(return_text)

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