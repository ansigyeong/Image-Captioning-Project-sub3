from django.shortcuts import render
from .serializers import VocabularySerializer, SpeakingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Vocabulary, Speaking
from datetime import datetime
from django.utils.dateformat import DateFormat
from captioning import main as caption

@api_view(['POST'])
def vocabulary(request):

    # 선택한 필드가 'True'인 단어 중에서 랜덤으로 30개 선정
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
    # print('여기')
    # print(request.FILES['inputImage'])
    speak = Speaking()
    speak.image = request.FILES['inputImage']
    speak.cap_text = 'test'
    speak.save()
    text = speak.image
    return_text = caption.main(text)
    return Response(return_text)
    