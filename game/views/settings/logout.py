from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def signout(request):  //request是django語法糖
    user = request.user
    if not user.is_authenticated:  //未登錄也直接返回success
        return JsonResponse({
            'result': "success",
        })
    logout(request)
    return JsonResponse({
        'result': "success",
    })
