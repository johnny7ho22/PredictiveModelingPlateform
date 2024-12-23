from django.shortcuts import render,redirect,HttpResponse
from django import forms
from ml_plateform.utils.BootstrapModelForm import BootstrapForm 
from ml_plateform.utils.encrypt import md5
from ml_plateform import models


# 建立login表單
class LoginForm(BootstrapForm):
    name = forms.CharField(
        label="用戶名",
        widget=forms.TextInput,
        required=True #欄位是必填的
    )

    password = forms.CharField(
        label="密碼",
        widget=forms.TextInput,
        required=True
    )
    # 當表單被提交時，Django 會自動調用每個欄位的 clean_<fieldname> 方法（比如 clean_password）
    # 在 clean_password 方法中，可以對 password 欄位的數據進行自定義處理
    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
        
    #     return md5(password)



def login(request):
    """"用戶登入"""

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form' : form})


    form = LoginForm(data = request.POST)

    if form.is_valid():
        #去資料庫校驗用戶名和密碼是否一致 
        user_object = models.Employee.objects.filter(**form.cleaned_data).first()

        if user_object:
            #主管
            if user_object.job_title == 1:
                pass
            
            #工程師 
            if user_object.job_title == 2:
                return redirect("/engineer/list")

            #資料庫管理員 
            if user_object.job_title == 3:
                return redirect("/dba/user_list")


        return redirect('/login/')
                



