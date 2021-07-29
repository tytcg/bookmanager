from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from book.models import BookInfo, PersonInfo

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

##################查询数据##################
# get查询单一的结果
# 如果查询不到会报DoesNotExist错，故在执行get方法时要抛异常。
try:

    BookInfo.objects.get(id=6)
except  BookInfo.DoesNotExist:
    print("查询的数据不存在！")

# all查询多个结果
BookInfo.objects.all()
# count查询结果的数量
BookInfo.objects.all().count()
BookInfo.objects.count()

# ##############过滤数据##################
# filter 过滤出多个结果
# exclude  排除符合条件的剩余的结果
# get 获得单一结果

# 书写格式
# 模型类名.objects.filter(属性名__运算符=值)
# 模型类名.objects.exculde(属性名__运算符=值)
# 模型类名.objects.get(属性名__运算符=值)

# 练习
# 1、查询图书编号为1的图书
book = BookInfo.objects.get(id=1)
book1 = BookInfo.objects.get(is_delete__exact=1)
book2 = BookInfo.objects.get(pk=1)
book3 = BookInfo.objects.filter(id=1)
# 2、查询书名包含'湖'字的图书
BookInfo.objects.filter(name__contains='湖')
# 3、查询书名以'部'字结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 4、查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 5、查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1, 3, 5))
# 6、查询编号大于3的图书
# gt 大于
# gte 大于等于

# lt 小于
# lte 小于等于

BookInfo.objects.filter(id__gt=3)
# 7、查询编号不等于3的图书
BookInfo.objects.exclude(id__exact=3)
# 8、查询1980年发行的图书
BookInfo.objects.filter(pub_date__year=1980)
# 9、查询1990年1月1日以后发行的图书
BookInfo.objects.filter(pub_date__gt=1990-1-1)

###################过滤两个字段的数据#########################
# 两个字段进行比较
# 使用语法  类名.objects.filter(属性名__运算符=F('另一个字段'))
from django.db.models import F
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))
# 查询阅读量大于两倍评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)

# 并且查询
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
BookInfo.objects.filter(readcount__gt=20, id__lt=3)  # 查询阅读量大于20，id小于3的图书

# 或查询
# 使用Q对象  在django.db.models中导入
from django.db.models import Q
# 使用语法  类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|....)
# 使用Q作或用法
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 使用Q作与用法  # 只是比较麻烦，不常用
BookInfo.objects.filter(Q(readcount__gt=20) & Q(id__lt=3))

#使用Q还可以作非用法
BookInfo.objects.filter(~Q(id=3))

######################聚合函数##########################
from django.db.models import Sum,Max,Min,Avg,Count

# 基本语法  模型类名.objects.aggregate(xxx('字段'))
BookInfo.objects.aggregate(Sum('readcount'))  # 对readcount字段进行求和。
# order_by 对所有数据进行排序
# 基本语法  模型类名.objects.all().order_by('字段名')  # 默认是升序
# 降序只要在字段前面加个-号
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.all().order_by('-readcount')

###################级联查询#######################
# 在一对多的关系模型中
# 系统会自动在一的模型中创建一个关联模型(小写)_set
# 在一的模型中查询出对应的数据，通过该字段就可以查询出所有的关联模型中的数据。

# 查询书籍为1的所有人物信息
book1 = BookInfo.objects.get(id=1)
book1.personinfo_set.all()
# 查询人物为1的书籍信息

person = PersonInfo.objects.get(id=1)
person.book.name  # 通过外键得到了书籍表中的name字段

#################关联过过滤查询####################
# 基本语法
# 查询1，条件n
# 模型类名.objects.filter(personinfo__属性名__运算符=值)

# 查询图书，要求图书的人物为"郭靖"
BookInfo.objects.filter(personinfo__name__exact='郭靖')
# 查询图书，要求人物的描述中包含'八'
BookInfo.objects.filter(personinfo__description__contains='八')

# 查询n 条件为1
# 查询书名为"天龙八部"的所有人物
PersonInfo.objects.filter(book__name__exact='天龙八部')
# 查询图书阅读量大于30的所有人物
PersonInfo.objects.filter(book__readcount__gt=30)

