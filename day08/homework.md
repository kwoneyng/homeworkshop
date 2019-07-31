1.

```
request, respone
```

2.

```
pip install Flask
```

3.

```python
from flask import flask
app = flask(__name__)

@app.route('/')
def hello():
	return 'hello world'
```

4.

env FLASK_APP=hello.py flask run

