from yorum.models import Yorum
from yorum.api.serializers import YorumOlusturSerializer,YorumGetirSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers



@csrf_exempt
def yorum_list(request):
    if request.method == 'GET':
        yorum = Yorum.objects.all()
        serializer = YorumGetirSerializer(yorum, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = YorumGetirSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def yorum_detay(request,id):
    try:
        yorum = Yorum.objects.get(id=id)
    except Yorum.DoesNotExist:
        return HttpResponse(status=400)
    if request.method == 'GET':
        serializer = YorumGetirSerializer(yorum)
        return JsonResponse(serializer.data)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = YorumOlusturSerializer(yorum,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        yorum.delete()
        return HttpResponse(status=204)
    


