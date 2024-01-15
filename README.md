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

8. To limit no of rows return in response:
    e.g.
            http://127.0.0.1:8000/libraryview/?limit=20

       ![image](https://github.com/Vidit-Kumar/LibraryHtmx/assets/70143937/a196cd1a-d4f5-4449-910b-47312fbf5e83)


Press populate to load the data

![image](https://github.com/Vidit-Kumar/LibraryHtmx/assets/70143937/c5f2e4e0-6072-47f4-917b-9b68fad8bcb7)

Loaded data

![image](https://github.com/Vidit-Kumar/LibraryHtmx/assets/70143937/df53bfc3-e9a5-41fa-9c5f-78fd5830b9c9)





