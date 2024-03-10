
from huey import SqliteHuey
import django
# Initialize Django
django.setup()
from libraryapp.models import Library
from libraryapp.models import Jobs

huey = SqliteHuey(filename='db.sqlite3')

@huey.task()
def generate_books_task(jobid:int):
    #This task will perform two operation as below
    # 1. Add books 
    Library.populate_library_data(True)
    # 2. After completion update the Job  status in job table.
    jobinstance = Jobs.objects.get(pk=jobid)
    jobinstance.status="COMPLETED"
    jobinstance.save()
    print('generated')
    pass
