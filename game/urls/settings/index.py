from django.urls import path
from game.views.settings.getinfo import getinfo # 引入上面写的getinfo函数
from game.views.settings.login import signin # 引入自己写的逻辑

urlpatterns = [
    path("getinfo/", getinfo, name = "settings_getinfo"), # 增加这个路由
    path("login/", signin, name = "settings_login")
]