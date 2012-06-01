# Box.net API wrapper for Python #
---

*This api module is in **developing**, any advice is welcome*

### Usage

Developers should apply for an api key while using Box.net API. (Where to apply: [Box.net: Developer Services](https://www.box.com/developers/services))

	>>> from boxapi import Session
	>>> api_key = "boxnetapikeyexample"
	>>> session = Session(api_key)
	>>> session.apply_new_authtoken()
	Please go to the following url for authentication: https://www.box.com/api/1.0/auth/boxnetapiticketexample
	>>> ticket = session.ticket

After the user authorized your app on the above webpage, you can shoot the `authorize()` method to get the auth token.

	>>> session.authorize(ticket)
	>>> session.auth_token
	'boxnetauthtokenexample'
