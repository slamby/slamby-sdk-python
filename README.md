## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/slamby/slamby-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/slamby/slamby-sdk-python.git`)

Then import the package:
```python
import slamby_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import slamby_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import slamby_sdk
from slamby_sdk.rest import ApiException
from pprint import pprint

client = slamby_sdk.ApiClient("http://<api_host>/")
client.set_default_header("Authorization", "Slamby <api_secret>")
```

Getting DataSet list

```python
dataset_api = slamby_sdk.DataSetApi(client)
data_sets = dataset_api.get_data_sets()
```

Selecting a DataSet for work

```python
client.set_default_header("X-DataSet", "<my_dataset>");
```

Get Tag list

```python
tag_api = slamby_sdk.TagApi(client)
tags = tag_api.get_tags()
```

Creating a new Tag

```python
try:
    tag = slamby_sdk.Tag()
    tag.id = "123"
    tag.name = "New tag"
    
    tag_api.create_tag(tag = tag)
except ApiException as e:
    print ("Exception when calling TagApi->create_tag: %s\n" % e)
```

Get a Document

```python
document_api = slamby_sdk.DocumentApi(client)
document = document_api.get_document("123456")
```

Update a Document

```python
try:
    document["language"] = "hu"
    document_api.update_document(id="123456", document = Document)
except ApiException as e:
    print ("Exception when calling DocumentApi->update_document: %s\n" % e)
```