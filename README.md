# OneDayAdventure

Web Dev Project based on Django

# How to Run
## 1. Requirements
- postgresql, redis, Pillow, openai, django, python-dotenv, django-imagekit, psycopg2 or psycopg2-binary, celery

## 2. .env 파일 작성
oda 디렉터리에 .env 파일 생성 
비밀 키와 Postgresql db 이름 유저 정보 작성

```
SECRET_KEY = 비밀키
NAME = 데이터베이스 명
USER = 데이터베이스 유저 이름
PASSWORD = 데이터베이스 유저 비밀번호
OPENAI_API_KEY = 
```

## 3. migrate
```
python manage.py makemigrations
python manage.py migrate
```

## 4. celery worker 실행  
```celery -A config worker -l info```


## 5. Django Run : 
```
python manage.py runserver
```

---
ui 스타일 변경 : [bootswatch](https://bootswatch.com/morph/)
