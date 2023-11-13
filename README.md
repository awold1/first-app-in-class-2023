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
python -m app.my_script
```
Run the Unemployment report:
```sh
python -m app.unemployment
```
Send an email:
```sh
python -m app.email_service
```
## Testing

Run tests:

```sh
pytest
```