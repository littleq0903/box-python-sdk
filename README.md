![boxapi logo](http://dl.dropbox.com/u/2587385/images/boxapi/boxapi_logo_850.png "Title")

## Box.net SDK for Python ##

This api module is in **developing**, any advice is welcome.

Box.net SDK for Python made developers could access Box.net v2 RESTful API with Python programming language in a easier way, from authentication to query/update the information of files/folders.


### Authentication

Developers should apply for an api key while using Box.net API. (Where to apply: [Box.net: Developer Services](https://www.box.com/developers/services))

	>>> from boxapi import Session
	>>> api_key = "boxnetapikeyexample"
	>>> session = Session(api_key)
	>>> session.apply_new_authtoken()
	Please go to the following url for authentication: https://www.box.com/api/1.0/auth/boxnetapiticketexample
	>>> ticket = session.ticket 
	
The url for authenticating will be stored in `session.auth_url`.

After the user authorized your app on the above webpage, you can shoot the `authorize()` method to get the auth token.

	>>> session.authorize(ticket)
	>>> session.auth_token
	'boxnetauthtokenexample'

Take a look and execute `test.py` for more action detail.

### Action

Action is the general function for calling API methods. To operate correctly, you must know the auth token of the user.

```python

import boxapi
	
api = boxapi.Session("<Your API Key>", auth_token="<Your Auth Token>")
api.action("/folders/0")
```
	
`api.action()` will return a dictionary which contains the response from the api call, and already has been transformed into dictionary from JSON format.

---

### Test
Here's a test script under the root folder of this project, named `test.py`. Before using the test script, you need to fill `API_KEY` and `AUTH_TOKEN`(optional) manually to make sure it will execute successfully.

If you didn't fill the field `AUTH_TOKEN`, you will need to authorize by open the url appear in the prompt, otherwise you will do the default action (call `/folders/0`) and see the prettified response on your screen.

#### Usage of test.py

	python test.py

will do the default action `/folders/0`.

	python test.py "/folders/<other_folder_id>"
	
will call the action you specified by assigning the first argument and display the response.


### Roadmap

**boxapi** now can work well with all the api methods with `GET` and `POST`, excluding file downloading and file uploading.

I will implement these following features recently:

* Uploading file(s)
* Downloading file(s)
* Directories tranversal
* Session's methods for simplify the progress of doing specify method
* Exception handling
