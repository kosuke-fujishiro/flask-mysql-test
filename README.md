# flask-mysql-test

This is a test of using flask with mysql.

## Requirements

- Python 3.9 or later
- Docker

## Usage

### 1. Run mysql in docker

```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=example -e MYSQL_DATABASE=testdb -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 -d mysql:5.7 --default-authentication-plugin=mysql_native_password
```

### 2. Run flask app

```bash
git clone https://github.com/kosuke-fujishiro/flask-mysql-test.git
cd flask-mysql-test
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

### 3. Test

Access to http://localhost:5000/

If you see "Success Connection! Current time: {current time}", it works well.
