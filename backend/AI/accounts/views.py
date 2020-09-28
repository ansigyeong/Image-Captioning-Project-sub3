from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import PointSerializer, PointListSerializer, DailySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point, User, DateCount
from django.forms.models import model_to_dict

# 오늘 날짜 가져오기 위함
from datetime import datetime
from django.utils.dateformat import DateFormat

finduser = get_user_model()

@api_view(['POST'])
def point_reward(request):

    user_pk = request.data['user']

    user = get_object_or_404(User, pk=user_pk)

    serializer = PointSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data)

@api_view(['GET'])
def point_list(request):
    user = get_object_or_404(User, user=request.user)

    points = Point.objects.filter(user=user).order_by('-pk')
    
    # 해당 유저의 전체 포인트를 리스트로 정리
    user_point_list = []
    for point in points:
        if point.use_type == True:
            user_point_list.append(point.value)
        else:
            user_point_list.append(-point.value)
    
    # 합계를 구하여 user 모델의 db에 저장
    user_points = sum(user_point_list)
    user.total_point = user_points
    user.save()

    serializer = PointListSerializer(points, many=True)

    # data 라는 dict를 생성하여 total_point와 point_list를 return
    # point_list는 기존의 serializer를 활용
    data = {
        "total_points": user_points,
        "point_list": serializer.data
    }
    return Response(data)

@api_view(['POST'])
def daily(request):
    
    # json 으로 넘어온 날짜 데이터를 받아서 사용
    time = request.data['day']

    # print(request)
    # print(request.data)
    # print(request.data['day'])
    # print(request.user)

    user = request.user

    day = DateCount.objects.filter(user=user).filter(date=time)

    day_serializer = DailySerializer(day, many=True)

    # 받아온 date 값에서 year과 month를 추출
    year = time[0:4]
    month = time[5:7]

    # 해당하는 연도의 해당하는 달에 해당하는 값들을 filter로 검색
    month_list = DateCount.objects.filter(user=user).filter(date__year__gte=year, date__month__gte=month, date__year__lte=year, date__month__lte=month).values('date')

    month_day_list = []
    # month_list 쿼리셋에서 개별 dict를 추출
    for month_value in month_list:
        # dict에서 필요한 value 값만 추출
        for key, value in month_value.items():
            # 해당 값을 list에 저장
            month_day_list.append(value.day)

    data = {
        'day': day_serializer.data,
        'month': month_day_list
    }

    return Response(data)

@api_view(['POST'])
def userdelete(request):
    print(request.user)
    user = get_object_or_404(User, username=request.user)
    # user = User.objects.get(username=request.user)
    print(user)
    print(type(user))
    request.user.delete()
    return Response('삭제됨')

@api_view(['POST'])
def createattendance(request):
    user = request.user
    
    # 오늘(요청이 온 날) 체크
    today = DateFormat(datetime.now()).format('Y-m-d')

    # db에서 해당 날짜와 유저에 해당하는 테이블 체크
    day = DateCount.objects.filter(user=user).filter(date=today)
    
    # 해당하는 테이블이 없는지 체크 len(day) == 0
    if len(day) == 0:
        day = DateCount()
    # 이미 존재하면 Response
    else:
        return Response('이미 있음')
    
    # 없을 경우 새로 생성
    day.user = user
    day.save()

    return Response('생성완료')