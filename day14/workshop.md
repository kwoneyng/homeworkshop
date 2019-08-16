workshop2.html

```python
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Pull</title>
</head>
<body>
  <h1>Pull Number</h1>
  <h3>Pull 해보니 {{pull}} 입니다!</h3>
</body>
</html>
```

workshop.html

```python
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>Push Number</h1>
  <form action="/workshop2">
    <input type="text" name="pull">
    <button type="submit">Push!</button>
  </form>
</body>
</html>
```

views.py

```python
def workshop(request):
    return render(request, 'workshop.html')


def workshop2(request):
    pull = request.GET.get('pull')
    context = {
        'pull':pull,
    }
    return render(request, 'workshop2.html', context)
```

urls.py

```html
    path('workshop2/', views.workshop2),
    path('workshop/', views.workshop),
```

