# SeaTeacher

### Installing
1. Create data base
```
    >>>from models import db
    >>>from app import app
    >>>app.app = app
    >>>db.app = app
    >>>db.init_app(app)
    >>>db.creat_all()
```
