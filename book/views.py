from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo


def index(request):
    obj = BookInfo.objects.all()
    print(obj)
    return HttpResponse("ok")


################增加数据###################

from book.models import BookInfo

book = BookInfo(
    name="必然",
    pub_date="2010-1-6"
)
# 必须要调用函数才可以实现增加
book.save()
# 方法二
BookInfo.objects.create(
    name="java",
    pub_date="2020-1-17",
    readcount=10,
    commentcount=2
)

################修改数据####################
# 方法一
book = BookInfo.objects.get(id=6)
book.name = "python入门"
book.readcount = 1
book.save()
# 方法二
BookInfo.objects.filter(id=7).update(name="django从基础到高级", readcount=200)
#################删除数据###################
# 方法一
book = BookInfo.objects.get(id=6).delete()
# 方法二
BookInfo.objects.filter(id).delete()

