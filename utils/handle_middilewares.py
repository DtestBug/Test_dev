from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


# 禁止爬虫,需要在settings指定MIDDLEWARE = ['utils.handle_middilewares.DeclineSpidersMiddleware']
class DeclineSpidersMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.META.get('HTTP_USER_AGENT').startswith('Mozilla/5.0'):
            return JsonResponse({'ret': False, 'msg': '爬虫吃屁屁！来，对暗号，天王盖地虎下一句是啥'})
        return None

