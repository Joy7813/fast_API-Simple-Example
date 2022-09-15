from fastapi import FastAPI, Request, Form ,HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import templates
import pandas


templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/login')     
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request}) 

@app.post('/loginpage')
def get_user(request: Request, email:str=Form(), password:str=Form()):
    d = {'abc@gmail.com':'pass@123','bidut@mail':'qwe123','xyz@gmail.com': 'Digj'}
    if email in d.keys():
        if d[email]==password:
            return templates.TemplateResponse("home_old.html", {"request": request})           
        else:
            return HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="Incorrect password")
    else:
        return HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="Incorrect Username")


@app.post('/result')
def get_user(request: Request, keyword:str=Form(), email:str=Form()):   
    # You can do any operation  here and can return the result                  
    df= pandas.DataFrame([[keyword, email]], columns=['user ID', 'search_keyword'])
    df.to_csv('search_data.csv')

    return {
        "your email is": email,
        "your keyword is " : keyword
    }

@app.get('/get_excel')
def dowload_excel(request: Request):
    file_path='search_data.csv'
    headers = {'Content-Disposition': 'attachment; filename= "search_data.csv"'}
    return FileResponse(file_path, headers=headers) 