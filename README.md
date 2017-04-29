# sports

1. Install virtualenv if not already installed
  pip install virtualenv
  
2. create a virtualenv dir
  virtualenv sports
  
3. enter that dir and pull down the 'sports' repository from github
  cd <rootdir>/sports
  git clone https://github.com/indika2000/sports.git
  
4. Activate the virtualenv (from the sports dir)
  source bin/activate
  
5. use the requirements file to install prerequsites for the web app
  pip install -r requirements.txt
