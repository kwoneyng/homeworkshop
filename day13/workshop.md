urls.py

```python
"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# django_intro/urls.py
from django.contrib import admin
from django.urls import path
from pages import views

# www.ssafy.com/login => 404 not found
# www.ssafy.com/index => views.index

urlpatterns = [
    # path('사용자가 접속하는 경로')
    path('student/<str:name>/<int:age>/', views.student),
    path('info/', views.info),
]

```

views.py

```python
from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def info(request):
    return render(request, 'info.html')


def student(request, name, age):
    context = {
        'name':name,
        'age':age,
    }
    return render(request, 'student.html', context)
```

student.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Student</title>
</head>
<body>
  <h1>이름 : {{name}}</h1>
  나이 : {{age}}
</body>
</html>
```

info.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>우리반정보</h1>
  <h3>Teacher</h3>
  <ul><li>Name</li></ul>
  <h3>Student</h3>
  <ul>
  <li>홍길동</li>
  <li>김길동</li>
  <li>박길동</li>
  </ul>
</body>
</html>
```

