"""
URL configuration for department project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from job import views

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT},name='media'),
    # path("admin/", admin.site.urls),/
    
    
    path("depart_list",views.depart_list),
    path('depart_add',views.depart_add),
    path('depart_delete',views.depart_delete),
    path('depart<int:nid>_edit',views.depart_edit),
    path('depart/mutil',views.depart_mutil),

    path("user_list",views.user_list),
    path("user_add",views.user_add),
    path("user<int:nid>_edit",views.user_edit),
    path("user<int:nid>_del",views.user_delete),
    
    path("Admin_list",views.Admin_list), 
    path("admin_add",views.admin_add),
    path("admin<int:nid>_edit",views.admin_edit),
    
    path('login',views.login),
    path("logout",views.logout),
    path("img_code",views.img_code),
    
    path('task_list',views.task_list),
    path('task_ajax',views.task_ajax),
    path('task_add',views.task_add),
    
    path('order/list/',views.order_list),
    path('order/add/',views.order_add),
    path('order/delete/',views.order_del),
    path('order/detail/',views.order_detail),
    path('order/edit/',views.order_edit),
    
    path('chart/list',views.chart_list),
    path('char/bar/',views.chart_bar),
    
    path('upload/list',views.upload_list),
    path('upload/modelform',views.upload_modelform),
    path('city/list',views.city_list),
    path('city/add',views.city_add),
]
