# Personal Article Bookmark Tool

It is a Python (fastapi) web application using the Wikipedia API that allows users to
search for Wikipedia articles based on a keyword. It should display the results and allow
users to save their favorite articles.

## Following frameworks/modules are used it this project:
* Fastapi
* sqlAlchemy
* Pydentic

## Following external api’s are used it this project:
* Wikipedia Api
* Texteazor

## Project system design
![Flow](https://github.com/user-attachments/assets/c8021257-8381-477b-b54b-e38e4a990eb3)

## Setup the app on local machine
To run the application on local machine you should have installed the following:
* Python
* Git

## Download and run
### Clone the repo from github
Open command prompt and type the following commands:
  ```
  git clone https://github.com/LokeshJangid01/wiki-search-UI
  ```
### Create virtual env or activate the env if already created
```
python -m venv v
v\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run server
```
uvicorn app:app --reload
```
# To use the application 
 After running the server with command uvicorn app:app --reload got browser and paste following url
## Root url [localhost](http://127.0.0.1:8000) or (http://127.0.0.1:8000)
