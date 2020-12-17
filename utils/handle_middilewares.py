from django.utils.deprecation import MiddlewareMixin


# 禁止爬虫,需要在settings指定MIDDLEWARE = ['utils.handle_middilewares.DeclineSpidersMiddleware']
class DeclineSpidersMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META.get('HTTP_USER_AGENT').startswith('Mozilla/5.0'):
            return JsonResponese({'ret': False, 'msg': '只能使用浏览器访问'})
        return None

