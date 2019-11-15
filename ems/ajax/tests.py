from django.test import TestCase
import django,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_project.settings")
# Create your tests here.
django.setup()
from datetime import datetime
from ajax.models import User


# User.objects.create(name='wangwu',age=32 ,salary=1123,brithday=datetime.now())
# User.objects.create(name='zhangsan',age=34,salary=2134,brithday=datetime.now())
# User.objects.create(name='lisi',age=36,salary=1231,brithday=datetime.now())
# User.objects.create(name='zhaoliu',age=26,salary=2124,brithday=datetime.now())
# User.objects.create(name='ergou',age=43,salary=2121,brithday=datetime.now())


list1=[input(),input()]
print(list1)


dict1={'name':input('请输入姓名'),'age':input('请输入年龄'),'sex':input('请输入性别')}
