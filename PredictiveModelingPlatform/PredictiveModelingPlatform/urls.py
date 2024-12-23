"""
URL configuration for PredictiveModelingPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from ml_plateform import views
from ml_plateform.views import account,engineer,dba
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name = 'media'),

    #用戶登入
    path('login/', account.login),


    
    #工程師-資料上傳區
    path('engineer/upload/', engineer.upload_data),

    #工程師-資料視覺化
    path('engineer/visualization/', engineer.visualization),
    #工程師-資料集是否平衡
    path('engineer/chart/imbalance/', engineer.chart_imbalance),
    #工程師-男、女性患有心臟病之分佈
    path('engineer/chart/sexDisease/', engineer.sex_disease),
    #工程師-男、女性胸口疼痛類型分佈
    path('engineer/chart/chestPain/', engineer.chest_pain),
    #工程師-盒鬚圖
    path('engineer/chart/boxplot/', engineer.box_plot),
    #工程師-類別型特徵對心臟病之影響
    path('engineer/chart/cfeatureTarget/', engineer.cfeature_target),

    #工程師-模型預測區-展示數據
    path('engineer/model/page/', engineer.model_page),
    #工程師-模型預測區-新增數據
    path('engineer/model/add/', engineer.model_add),
    #工程師-模型預測區-刪除數據
    path('engineer/model/delete/', engineer.model_delete),
    #工程師-模型預測區-取得要編輯的數據
    path('engineer/model/edit_detail/', engineer.edit_detail),
    #工程師-模型預測區-編輯數據
    path('engineer/model/edit/', engineer.model_edit),
    #工程師-模型預測區-預測數據
    path('engineer/model/predict/', engineer.model_predict),

    
    

    


    #資料庫管理員-員工管理
    path('dba/user_list/', dba.show_user_list),
    #資料庫管理員-新增員工
    path('dba/user_add/', dba.user_add),
    #資料庫管理員-刪除員工
    path('dba/user_delete/', dba.user_delete),
    #資料庫管理員-取得要編輯的員工的資訊
    path('dba/edit_detail/', dba.edit_detail),
    #資料庫管理員-編輯員工
    path('dba/user_edit/', dba.user_edit),


]
