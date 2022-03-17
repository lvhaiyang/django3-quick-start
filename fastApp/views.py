from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


# @require_http_methods(["GET", "POST"])
@require_http_methods(["GET"])
def get_test(request):
    res = {
        'code': 0,
        'method': "GET",
        'msg': "Hello! This is /fastApp/index"
    }
    return JsonResponse(res)

@require_http_methods(["GET"])
def api_path_params(request, id):
    res = {
        'code': 0,
        'method': "GET",
        'msg': "api_path_params is %s." % id
    }
    return JsonResponse(res)

@require_http_methods(["POST"])
@csrf_exempt
def post_test(request):
    res = {
        'code': 0,
        'method': "POST",
        'msg': "csrf_exempt 是为了解决post请求安全校验报错"
    }
    return JsonResponse(res)

@require_http_methods(["GET"])
def get_method_params(request):
    if request.method == 'GET':
        params = request.GET.lists()
        res = {
            'code': 0,
            'msg': "获取请求的参数",
            'data': dict(params)
        }
        return JsonResponse(res)

@require_http_methods(["POST"])
@csrf_exempt
def post_method_data(request):
    if request.method == 'POST':
        data = request.POST.lists()
        res = {
            'code': 0,
            'msg': "获取请求的参数",
            'data': dict(data)
            }
        return JsonResponse(res)

@require_http_methods(["POST"])
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        with open('./fastApp/upload/upload_test.zip', 'wb+') as fp:
            for chunk in request.FILES['file'].chunks():
                fp.write(chunk)
        res = {
            'code': 0,
            'msg': "上传文件"
            }
        return JsonResponse(res)