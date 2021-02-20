from rest_framework.views import APIView
from rest_framework.response import Response
import requests


# 爬虫获取登录标语
class SloganView(APIView):

    def get(self, request):
        url = "http://www.yogapi.com/api/getPresentQuote.php"
        data = requests.get(url).json()['quote']
        res = {
            'data': data
        }
        return Response(res)
