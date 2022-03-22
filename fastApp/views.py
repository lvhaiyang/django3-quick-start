from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Person


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

@require_http_methods(["POST"])
@csrf_exempt
def database_save(request):
    if request.method == 'POST':
        # 获取请求参数
        data = dict(request.POST.lists())
        person_age = data['age'][0]
        person_name = data['name'][0]
        # 写入数据库
        Person(name=person_name, age=person_age).save()
        res = {
            'code': 0,
            'msg': "写入数据库成功",
            'data': dict(data)
            }
        return JsonResponse(res)

@require_http_methods(["GET"])
def database_select(request):
    if request.method == 'GET':
        data1 = []
        # 原生sql查询数据
        for r in Person.objects.raw('SELECT * FROM person'):
            data1.append((r.name, r.age))
        
        # 用 all() 检索全部对象
        data2 = []
        for r in Person.objects.all():
            data2.append((r.name, r.age))

        # 用 get() 检索单个对象
        # 否则报错 fastApp.models.Person.MultipleObjectsReturned: get() returned more than one Person -- it returned 2!
        p = Person.objects.get(name="张三")
        data3 = [p.name, p.age]
        print(data3)

        # 通过过滤器检索指定对象
        # filter() 包含的对象满足给定查询参数
        data4 = []
        for r in Person.objects.filter(name='李四'):
            data4.append((r.name, r.age))

        # exclude() 包含的对象不满足给定查询参数
        data5 = []
        for r in Person.objects.exclude(name='李四'):
            data5.append((r.name, r.age))

        res = {
            'code': 0,
            'msg': "查询成功",
            'data1': data1,
            'data2': data2,
            'data3': data3,
            'data4': data4,
            'data5': data5
        }
        return JsonResponse(res)

@require_http_methods(["POST"])
@csrf_exempt
def database_update(request):
    if request.method == 'POST':
        # 获取请求参数
        data = dict(request.POST.lists())
        person_age = data['age'][0]
        # 更新数据
        Person.objects.filter(name='李四').update(age=person_age)
        data = []
        for r in Person.objects.filter(name='李四'):
            data.append((r.name, r.age))
        res = {
            'code': 0,
            'msg': "数据更新成功",
            'data': data
            }
        return JsonResponse(res)

@require_http_methods(["POST"])
@csrf_exempt
def database_delete(request):
    if request.method == 'POST':
        # 获取请求参数
        data = dict(request.POST.lists())
        name = data['name'][0]
        # 删除数据
        Person.objects.filter(name=name).delete()
        data = []
        for r in Person.objects.filter(name=name):
            data.append((r.name, r.age))
        res = {
            'code': 0,
            'msg': "数据删除成功",
            'data': data
            }
        return JsonResponse(res)