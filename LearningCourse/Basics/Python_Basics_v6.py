'''
#venv() : virtual environment : Python uses virtual environments to create an isolated environment for every project. In other words, each project will have its own directory to store third-party packages.
#In case you have multiple projects that use different versions of a package, you can store them in separate virtual environments.
#step1
mkdir D:\test_env
cd test_env
#step2
python -m venv project_env #The above command will create a new folder called project_env with all necessary tools and libraries for running Python programs.
#step3
project_env\Scripts\activate #activate the virtual environment
#step4
mkdir web_crawler
cd web_crawler
#step5
pip install requests
#step6
pip freeze > requirements.txt #with the content
certifi            2023.11.17
charset-normalizer 3.3.2
idna               3.6
pip                22.2.2
requests           2.31.0
setuptools         63.2.0
urllib3            2.2.0
#step7 : work on the directory and file you want #https://www.pythontutorial.net/python-basics/python-virtual-environments/
#step8:
deactivate

'''