from multiprocessing import context
from plistlib import UID
from unicodedata import name
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
# Create your views here.
def index(request):
    #执行Model的操作

    #添加操作
    #ob = Users()
    #ob.name = "张某勇"
    #ob.age = 23
    #ob.phone = '19990301'
    #ob.save()


    #删除操作
    #mod = Users.objects  #获取model对象
    #user = mod.get(id=4) #获取id信息
    #print(user.name)
    #user.delete()

    #修改操作
    #ob = Users.objects.get(id = 2)
    #print(ob.name)
    #ob.name = "小张"
    #ob.age = 13
    #ob.save()

    #数据查询
    mod = Users.objects#获取user模型的model操作对象
    #ulist = mod.all()#获取所有数据
    #ulist = mod.filter(name='小张')
    ulist = mod.filter(age__gt=20)#年龄大于20的所有数据

    for u in ulist:
        print(u.id,u.name,u.age,u.phone,u.addtime)

    return HttpResponse("首页 <br/> <a href = 'users'>用户信息管理</a>")


#浏览用户信息
def indexUsers(request):
    try:
        ulist = Users.objects.all() #获取全部信息
        context = {"userslist":ulist}
        return render(request,"myapp/users/index.html",context)#加载模板
    except:
        return HttpResponse("没有找到异常信息！")
#加载添加用户信息表单
def addUsers(request):
    return render(request,"myapp/users/add.html")

#执行用户信息添加
def insertUsers(request):
    try:
        ob = Users()
        #从表单中获取要添加的信息并封装到ob中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()#执行保存
        context = {"info":"添加成功！"}
    except:
        context = {"info":"添加失败! "}
    return render(request,"myapp/users/info.html",context)
#执行用户信息删除
def delUsers(request,uid=0):
    try:
        ob = Users.objects.get(id = uid) #获取要删除的数据
        ob.delete()
        context = {"info":"删除成功！"}
    except:
        context = {"info":"删除失败! "}
    return render(request,"myapp/users/info.html",context)

#加载用户信息修改表单
def editUsers(request,uid = 0):
    try:
        ob = Users.objects.get(id = uid) #获取要修改的数据
        context = {"user":ob}
        return render(request,"myapp/users/edit.html",context)
    except:
        context = {"info":"没有找到要修改的数据! "}
    
#执行用户信息修改
def updateUsers(request):
    try:
        uid = request.POST['id']#获取要修改数据的id
        ob = Users.objects.get(id=uid)#查询要修改的数据
        #从表单中获取要添加的信息并封装到ob中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()#执行保存
        context = {"info":"修改成功！"}
    except:
        context = {"info":"修改失败! "}
    return render(request,"myapp/users/info.html",context)