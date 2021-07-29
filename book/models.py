from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)


    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍管理"

    def __str__(self):
        return self.name


class PersonInfo(models.Model):
    GENDER_CHOICE = [
        (1, 'male'),
        (2, 'female')
    ]
    name = models.CharField(max_length=10,unique=True)
    gender = models.IntegerField(choices=GENDER_CHOICE)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = "personinfo"

    def __str__(self):
        return self.name