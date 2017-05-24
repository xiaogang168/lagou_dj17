#encoding: utf-8
__author__ = ''

from login.models import Resume,WorkExperience,StudyExperience,User
from dj17 import function as fun

def get_resume_info(uid):
    try:
        #return Resume.objects.get(uid=uid) #当查询到多个值时，不会raise MultipleObjectsReturned 直接返回none
        return Resume.objects.filter(uid=uid).first()  
    except:
        return {}

def get_work_experience(resume_id):
    try:
        return WorkExperience.objects.filter(resume_id=resume_id)
    except:
        return []

def get_study_experience(resume_id):
    try:
        return StudyExperience.objects.filter(resume_id=resume_id)
    except:
        return []

def resume_post(data):
    id = data.pop('id')
    uid=data.pop('uid')
    data['uid']=User.objects.get(id=uid)
    if id:  ##更新
        return Resume.objects.filter(id=id).update(**data)
    else: ##插入
        r = Resume(**data)
        r.save()
        #print r.id,r.name  ##因为是自动生成id,所以在插值之前还不能拿到id
        #return r.id
        return r.name

def resume_work(data):
    id = data.pop('id')
    if id:  ##更新
        return WorkExperience.objects.filter(id=id).update(**data)
    else: ##插入
        w = WorkExperience(**data)
        w.save()
        return w.company_name

def resume_study(data):
    id = data.pop('id')
    if id:  ##更新
        return StudyExperience.objects.filter(id=id).update(**data)
    else: ##插入
        w = StudyExperience(**data)
        w.save()
        return w.school_name


def resume_search(keywords):
    qs = Resume.objects.filter(hope_work__contains=keywords)
    return qs