# LibraryHtmx
1. Clone repository in your choce of editor VSCode\PYCharm

2.  Goto folder "LibraryHtmx and create virtual environment

    >py -m venv yourenvnamehere

    yourenvnamehere>\Scripts\activate.bat (It will prompt envirnment folder as (envname) C:\Users\Your Name>)

3. Install package for custome environment

    >py -m pip install -r requirements.txt

    Navigate to \LibraryHtmx\projectlims folder

4. Initialize migrate

    py manage.py makemigrations library

    py manage.py migrate

5. libraryuser1 user created with password django123
   i.  admin  group is created
   ii. admin user  password is admin

6.  python manage.py runserver
    Open url in browser: http://127.0.0.1:8000/

7. Note**- 
    On deleting the  libraryuser1. Run the migration command again as mentioned in Step-3
    Create SuperUser(admin) 
       >python manage.py createsuperuser --username admin
     






