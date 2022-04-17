
# Image Crawler

  

# Objective

The objective of this crawler is to scrap images from a website (wich we redacted for security reasons) and save all the image files in two places:

  

- A local folder => ./img/content-name/ directory

- A Google Drive folder=> ./content-name/

  

# Installing requirements

### Requirements:

- Python 3.8 or newer.

- Pip

### Checking Python version:
```sh
$ python -V
or
$ python --version
```
### Checking Pip version:
```sh
$ pip -V
ou
$ pip --version
```
### Installing project dependencies:
All the requirements are in requirements.txt.
```sh
$ pip install requirement.txt
```
# Setup

After installing all requirements using requirements.txt, rename the file ```settings.yaml.sample``` to ```settings.yaml```.

You can use the follow command:

```sh
$ cp settings.yaml.sample settings.yaml
```

Change the values of ```client_id``` and ```client_secret``` to your real credentials.
Now we do the same to ```.env.sample```:
```sh
$ cp .env.sample .env
```
In ```.env``` change the values of the ```URL``` and  ```MAX``` to your target values.

Now copy your client_secrets.json file into your root folder.

The first time you run crawler.py you shall be prompted with a google auth prompt, after this first login the informations will be stored.

# Running tests

### Running unit tests

You can generate the tests report using pytest-html:

```sh
$ cd tests
$ py.test --html=report.html --self-contained-html
```
The results are stored in report.html file ;)