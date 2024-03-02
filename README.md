#TestTask
Test app simulating a course store(backend part)

Функции:
1. View courses available to purchase
2. Purchasing a course
3. Group distribution
4. View purchased courses
5. Authorisation

##Quick start

git clone https://github.com/Ravehdd/TestTask

cd TestTask

python3 venv venv

venv/Scripts/activate

pip install requirements.txt


##Run the app locally:

python manage.py runserver 127.0.0.1:8000

##IGDB usage:

1. Registration:
POST http://127.0.0.1:8000/api/v1/auth/users  Body: username, password, email(optional)
2. Login: 
POST http://127.0.0.1:8000/auth/token/login/  Body: username, password.
COPY received auth_token
3. Product list:
Add to headers - Authorisation: Token + your token
GET http://127.0.0.1:8000/api/v1/productlist/
4. Buy product:
Add to headers - Authorisation: Token + your token
POST http://127.0.0.1:8000/api/v1/productlist/  Body: product_id, money=cost of selected product
5. Purchased products list:
Add to headers - Authorisation: Token + your token
GET http://127.0.0.1:8000/api/v1/available/
6. Admin panel:
http://127.0.0.1:8000/admin/  Login: max, Password: 1234



   
