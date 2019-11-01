# Market Place - Sample App

A sample application using python's django framework to manage service requests and fulfill them.

## User Groups
* Worker: Can change task and complete it.
* Consumer: Can submit new task.

## Models
* TaskCategory
* Task

## How to run

```
    cd tasks
    pip3 install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata main/fixtures/initial_data.json
    python manage.py runserver
```

## Sample Users for https://bhaskarmarketplace.herokuapp.com/admin/
* SuperUser = Username: bhaskar Password: bhaskar
* Worker 1 = Username: worker1 Password: worker1
* Worker 2 = Username: worker2 Password: worker2
* Consumer 1 = Username: consumer1 Password: consumer1

