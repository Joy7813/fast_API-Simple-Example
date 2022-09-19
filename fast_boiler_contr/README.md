<b>This is a separated part which is added in fast-api boiler plate for learning purpose</b>

#  A simple example of templates rendering with FastAPI and performing various operations in backend.

### In this tutorial we exemplify a basic idea which is how our client talk to the server through the apis using FastAPI

### What will we discussed here?
1. Basics of FastAPI.
2. Installing Fastapi and other dependencies.
3. Simple rendering of a login page.
4. Accepting form data in a post request.
5. Simple example for performing operation in backend from frontend data.
6. Creating an api that downloads files.

## Basics of FastAPI
FastAPI is a fast, web framework for developing apis in python. Some of the great advantages of using FastAPI is -it is Fast.
-Support Asyncronous Programming.
-Short development time.
-Easy testing and deployment.
-It uses pydantic as type hint and data validation module and 
using dependency injections plugins can easily be created.

## Few points you should know as a pre-requisite:
<b> Asyncronous Programming:</b> Asyncronous programming is a non blocking methods that executes a program without blocking other operations. As an example three requests hit a server which are suppose to do following work. Request_1 is about requesting to get the forgotten email of the client. Request_2 is about getting data from a particular webpage which is stored in server database. Request_3 is about just addition operation of two integer.So now lets say we are using asynchronous program, than after the execution of first request, second request should not wait for the response of the first request, similarly, even if the second request have had taken time to prepare for response, the third request should be sent in mean time and utilize the idle time rather than waiting to complete the response of second request.

<b> Type Hints: </b> Type hints are nothing but some special syntax that declares the type of a variable. As an example 
`email: str
id: int `
Here email and id are the variable where only string data and integer data can be stored respectively.

<b> Dependency Injections:</b>  It simply means a way in programming where code functions or classes are declared and use while they needed to work. Dependency Injections are very useful when we need to write shared logic, Share database connections, enforce security and authentication. It minimizes the repetition of code.

## Installing Fastapi and other dependencies:
1. Create virtual environment in your working directory using command `python -m venv venv`
2. Create a requirements.txt file and include uvicorn, fastapi, jinja2, pydantic, multipart.
3. Run in your terminal `pip install -r requirements.txt`

<b> Note: </b>
uvicorn is a asyncronous server for python.
jinja2 is for templates handling.
pydantic is data validation library.
Multipart is used for the requests to combine one or more sets of data into a single body, separated by boundaries.

## Rendering of a simple login page:
write the following code given below.
login api
<figure align = "center" width="100%">
<img src="screenshots\login_tr1.PNG" width="800"/>
</figure>

Here, give the path of your templates directory where all the html files are present. As shown bellow
<figure align = "center" width="100%">
<img src="screenshots\templates.PNG" width="400"/>
</figure>

and run the code to run the server `uvicorn main:app --reload` where main is the filename and app is the FastAPI object name.
A simple html login.html page is written and stored under the templates folder.
<figure align = "center" width="100%">
<img src="screenshots\html_login.PNG" width="800"/>
</figure>

In the main.py a GET request api is created where a html templates is returned as a response.
## Accepting form data in a post request:
Now, Let's create a POST request api that will hit when we click the submit button in the login page. 
Copy the following code to create the post request.
For the shake of simplicity our password is stored in the code as a dictionary, the get_user function accept the post request with Form data email and password and if the email and password are matched return another html page as response. One thing to be noted that in login.html line number 11  (where method="post" and action="/loginpage")
the api endpoint is hit when the submit button of login page is clicked.
## Simple example for performing operation in backend from frontend data:
Now, suppose we want to perform some operation in backend from the frontend data and return the result of it. So how will you do that?
Lets figure it out how!
See the following code.
<figure align = "center" width="100%">
<img src="screenshots\post_loginpage.PNG" width="800"/>
</figure>
Here, we have created an api endpoint which accept email and keyword & take those input and save it in csv file,also return it as a response.You can perform any operations like this.

## Creating an api that downloads files:
Now, let say we want to download that csv file and see the result, So how do we do that!!
See the following code snapshot
<<figure align = "center" width="100%">
<img src="screenshots\get_excel.PNG" width="800"/>
</figure>
Basically, what happens under the hood is when the Download Result button is clicked in home_old.html the get_excel endpoint is hit, the download function is executed and return the file as response.