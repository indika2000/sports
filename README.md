# sports

1. Install virtualenv if not already installed
  ``` 
  pip install virtualenv
  ``` 
  
2. create a virtualenv dir
  ``` 
  virtualenv sports
  ``` 
  
3. enter that dir and pull down the 'sports' repository from github
  ``` 
  cd <rootdir>/sports
  git clone https://github.com/indika2000/sports.git
  ``` 
  
  or unzip the provide compressed folder
  
4. Activate the virtualenv (from the sports dir)
  ``` 
  source bin/activate
  ``` 
  
5. use the requirements file to install prerequsites for the web app
  ``` 
  pip install -r requirements.txt
  ``` 
  
6. From the project folder (location of the manage.py file)
```
  i.e. <root dir>/sports/sports/app
  ```
  a. Run tests by calling
     ``` 
      python manage.py test
      ```
      This will run both the unit tests and the functional tests
      
  b. When ready to test locally in a web browser, launch the development Django web server by
      
      python manage.py runserver 0.0.0.0:8000
      
      Now in a web browser navigate to:
      http://localhost:8000/
      
      or
      
      http://localhost:8000/fixtures
      
