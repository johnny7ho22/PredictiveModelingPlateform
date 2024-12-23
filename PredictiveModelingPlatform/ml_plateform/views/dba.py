from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from openpyxl import load_workbook

from ml_plateform import models
from ml_plateform.utils.BootstrapModelForm import BootstrapModelForm 
from ml_plateform.utils.pagination import Pagination


class EmployeeModelForm(BootstrapModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'

def show_user_list(request):
    """展示員工資訊"""
    form = EmployeeModelForm()

    fields_name = [field.name for field in models.Employee._meta.get_fields() if not field.is_relation]
        
    user_data = models.Employee.objects.all()

    page_object = Pagination(request, user_data)

    page_queryset = page_object.page_queryset

    #生成頁碼
    page_string = page_object.html()

    context = {"fields_name" : fields_name, "user_data":page_queryset, "page_string" : page_string, "form":form}


    return render(request, 'dba_list.html', context)


@csrf_exempt
def user_add(request):
    """新增員工"""

    form = EmployeeModelForm(data = request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({"status":True})
    else:
        return JsonResponse({"status":False, "error":form.errors})
    

def user_delete(request):
    """刪除員工"""
    uid = request.GET.get("uid")

    print(uid)

    exists = models.Employee.objects.filter(id = uid).exists()
    
    if not exists:
        return JsonResponse({"status":False, "error": "刪除失敗：數據不存在"})
    
    models.Employee.objects.filter(id = uid).delete()
    
    return JsonResponse({"status":True})


def edit_detail(request):
    """取得要編輯的員工的資訊"""

    uid = request.GET.get("uid")
    
    print(uid)
    
    row_dict = models.Employee.objects.filter(id = uid).values("name", "password", "age", "job_title").first()
    
    if not row_dict:
        return JsonResponse({"status":False, "error": "該數據已經不存在"})
    
    result = {
        "status":True,
        "data": row_dict
    }

    
    return JsonResponse(result)


@csrf_exempt
def user_edit(request):
    """編輯員工"""

    uid = request.GET.get("uid")
    
    row_object = models.Employee.objects.filter(id = uid).first()
    
    if not row_object:      
        return JsonResponse({"status":False, "tips": "該數據已經不存在"})
    
    form = EmployeeModelForm(data=request.POST, instance = row_object)
    
    if form.is_valid():
        form.save()
        return JsonResponse({"status":True})
    
    return JsonResponse({"status":False, "error": form.errors})



    

    
