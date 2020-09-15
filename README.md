# OpenML

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

OpenML is a web application based on Django/python, Machine Learning.Which makes user to 'Run' the dataset easily and get the output.

  - Upload dataset
  - Run the model
  - See the Graph

# Steps

  - Signup 
  - Login
  - Uplaod the SLR dataset
  - Give the X and Y value
  - Split that into Train and Test set
  - Train the SLR Model
  - Prediction
  - Print test set graph
  - print train set graph


You can also:
  - Find your dataset in your local directory
  - Also see the Graphs saved in png format
  ### Installation

OpenML requires [Djaango/Python]to run.

Install the dependencies and devDependencies and start the server(follow the Steps Below) .

```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ git clone https://github.com/guneshprasads/ML_using_Django.git
$ cd ML_using_Django
$ pip install -r requirements.txt
```

For production environments...

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
# Now Open your web Browser and visit (http://127.0.0.1:8000/)
# You'll see the Below screen
![1](https://user-images.githubusercontent.com/13889409/93187298-4af7e280-f75d-11ea-9144-940250213286.png)
![2](https://user-images.githubusercontent.com/13889409/93187312-4fbc9680-f75d-11ea-8ac5-7428ecbf1fe5.png)
![3](https://user-images.githubusercontent.com/13889409/93187318-50552d00-f75d-11ea-9551-fcda5484e35e.png)
![4](https://user-images.githubusercontent.com/13889409/93187340-54814a80-f75d-11ea-9c7b-d01b527b6985.png)
![5](https://user-images.githubusercontent.com/13889409/93187344-5519e100-f75d-11ea-9489-bced14f53517.png)


