from django.urls import path
#将fastApp/views.py 中的方法导入到fastApp/urls.py
#以便将方法与URL绑定，访问URL自动执行绑定的方法
from . import views

urlpatterns = [
    # ex: /fastApp/
    path('', views.get_test, name='get_test'),
    # ex: /fastApp/5/
    path('<int:id>/', views.api_path_params, name='api_path_params'),
    # ex: /fastApp/post_test
    path('post_test/', views.post_test, name='post_test'),
    path('get_method_params/', views.get_method_params, name='get_method_params'),
    path('post_method_data/', views.post_method_data, name='post_method_data'),
    path('upload_file/', views.upload_file, name='upload_file'),
     # ex: /fastApp/database_save
    path('database_save/', views.database_save, name='database_save'),
    path('database_select/', views.database_select, name='database_select'),
    path('database_update/', views.database_update, name='database_update'),
    path('database_delete/', views.database_delete, name='database_delete'),
]