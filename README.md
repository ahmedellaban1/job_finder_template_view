# Job Finder Template View
django project create job board website with function based view and class based view template
<hr>

### python version  3.11.4 <br>
*run this command in terminal or CMD*
```bash
python3 -V
```
**if you have version older than 3.11.4 you can go to **www.python.org** and get suitable version.**
<hr>

## Steps to run this project (*windows*):
 - open CMD in path you want to download repo on it 
 - clone this repo in your device
 - create python virtual environment
 - active the virtual environment
 - install the modules and requires pakages
 - apply migrations files to create database 
 - run django server
```bash
    git clone repo-link
    cd repo-folder-name
    python -m venv venv
    venv\Scripts\activate
    pip install requirements.txt
    python manage.py migrate
    python manage.py runserver
```

## steps to run this project (*linux*):
 - open terminal in directory you want to git repo on it 
 - clone this repo in your device
 - create python virtual environment
 - active the virtual environment
 - and run django server
```bash
    git clone repo-link
    cd repo-folder-name
    python3 -m venv venv
    source venv/bin/activate
    pip install requirements.txt
    python manage.py migrate
    python manage.py runserver
```
<hr>

## Folder structure
![Screenshot from 2023-10-22 14-51-17](https://github.com/ahmedellaban1/job_finder_template_view/assets/75578565/d883b4b8-aaa3-4d41-99c8-d3db5b62e526)

| Folder     | Description                                                             |
|:-----------|:------------------------------------------------------------------------|
| core       | contains settings files and main root url                               |
| etc        | contains every extra files help function, validators                    |
| job        | contains every thing about posts (db models, tables, views, urls)       |
| media      | this folder not in repo but once you upload image django will create it |
| migrations | contains db tables files that allow django to create database           |
| templates  | contains (html) files                                                   |
| static     | contains ( css, Js, img) files                                          |

| File             | Description                                                                                      |
|:-----------------|:-------------------------------------------------------------------------------------------------|
| db.sqlite3       | sql-lite file this file depends on database settings in the [core/settings.py](core/settings.py) |
| manage.py        | this file auto-created when the django project created                                           |
| requirements.txt | contains installed modules in the project with versions                                          |
