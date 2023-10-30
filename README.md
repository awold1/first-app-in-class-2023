# first-app-in-class-2023

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

## Install Packages
```sh
pip install -r requirements.txt
```
You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

## Usage

Run the Example Script:

```sh 
python app/my_script.py
```
Run the Unemployment report:
```sh
python app/unemployment.py
```
Send an email:
```sh
python app/email-service.py
```