# recipe-app
It let's user search their favourite recipes, add recipe, edit
and delete their own recipes.i.e. through user login, registration,
profile creation. 
Also user can view recipes by other users.

Environment:
  virtual user : me
  OS: Ubuntu Linux

dependencies:
    astroid==2.3.3
    Django==2.1.5
    django-cleanup==4.0.0
    django-crispy-forms==1.8.1
    django-mysql==3.3.0
    django-search-views==0.3.7
    isort==4.3.21
    lazy-object-proxy==1.4.3
    mccabe==0.6.1
    mysqlclient==1.4.6
    Pillow==7.0.0
    pytz==2019.3
    six==1.14.0
    typed-ast==1.4.1
    wrapt==1.11.2

Steps Required to run:
  Step 1. Setup project by:
              user@machine:$ bash setup.sh
  Step 2. Don't forget to setup mysql server (only for first time), just run 'script.sql'
              user@machine:$ mysql script.sql
              
