from django.db import models


class Employee(models.Model):
    """使用者"""
    name = models.CharField(verbose_name="員工姓名", max_length=16)
    password = models.CharField(verbose_name= '密碼', max_length=64)
    age = models.IntegerField(verbose_name="年齡")

    job_title_choice = (
        (1, "主管"),
        (2, "工程師"),
        (3, "資料庫管理員"),
    )

    job_title = models.SmallIntegerField(verbose_name='職稱', choices=job_title_choice)



class Supervisor(Employee):
    """主管"""
    team_size = models.IntegerField(verbose_name="管理團隊的規模", default=0)

    # subordinate_submit = models.CharField(verbose_name="下屬上傳的研究成果", max_length=64)



class Engineer(Employee):
    """工程師"""
    is_oncall = models.CharField(verbose_name="是否可以oncall", max_length=16)



class DBA(Employee):
    """資料庫管理員"""
    database_type = models.CharField(verbose_name="管理DB的類型", max_length=16)



class HeartFailure(models.Model):
    """心臟病資料集"""
    Age = models.IntegerField()
    Sex = models.IntegerField()
    ChestPainType = models.IntegerField()
    FastingBS = models.IntegerField()
    MaxHR = models.IntegerField()
    ExerciseAngina = models.IntegerField()
    Oldpeak = models.FloatField()
    ST_Slope = models.IntegerField()
    HeartDisease = models.IntegerField()

    




   