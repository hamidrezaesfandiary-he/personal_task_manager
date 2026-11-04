## Personal Task Manager
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)

A simple Task Manager built with python


## Features
- add multiple tasks
- save tasks
- load save tasks
- admin mode

## Requirements
- python
- python-dotenv


## Project Structure
```text
Personal_task_manager/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirements
│   tasks.py
|
├───gifs/
│       demo.gif
│
├───screenshots/
│       screenshot.png
```

## Installation 
Install the require packages

```bash

python -m pip install -r requirements.txt

```

## Envoirment setup
Create a `.env` file in the project folder

Use `.env.example` file as a template

Add your admin password 

```env
ADMIN_PASSWORD = "YOUR_PASSWORD_HERE"
```
Replace `YOUR_PASSWORD_HERE` with your own addmin password

## Run the program

Run the main file: 
```bash
python main.py
```

## Screen Shot

![run project](screenshots\screenshot.png)

## demo
![](gifs\demo.gif)