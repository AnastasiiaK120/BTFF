#  Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See installing for notes on how to get the project setup.

# Tools:

pip, virtual environment

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AnastasiiaK120/BTFF.git
$ cd BTFF

```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.




![Screenshot from 2022-08-15 06-06-30](https://user-images.githubusercontent.com/82476413/184621380-a0eef8a4-9974-4fc8-bdbd-595938fc115a.png)
![Screenshot from 2022-08-15 06-08-46](https://user-images.githubusercontent.com/82476413/184621382-60d27f85-9ffc-46eb-9208-d87e5943e9c7.png)




