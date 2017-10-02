# developingapps-python

## Overview

Meant to parallel the node version of this lab, using Python and Flask.

Application is within the ```end``` directory; ```end-back``` is currently just working files and can be ignored.

## Setup

### Server setup

* Open Cloud Shell
* Clone this repo
* Change directories into the ```end``` directory
* Run the setup bash file and the run_server python file
```
.  ./prepare_web_environment.sh
python run_server.py
```

### Worker setup
* Open 2nd tab in Cloud Shell
* Run the worker using ```run_worker.sh```

## App architecture

* App files live within ```quiz``` directory
* App is logically broken into pieces
  * ```api``` contains api routes/logic
  * ```console``` contains worker logic
  * ```gcp``` contains gcp helper modules
  * ```webapp``` contains web app routes/logic
* Within ```webapp```...
  * ```templates``` contains web views, excluding client
  * ```static``` contains static files, including client
* App is run from ```end``` using run_server.py
* The ```api``` and ```webapp``` modules use Flask blueprints. This allows for module-local routes files to create handlers.
* The ```gcp``` directory houses gcp heloper modules used by the ```api```, ```worker```, and ```webapp``` modules.

## Miscellaneous

* List API method doesn't do paging