# Social media analysis

This is a tutorial on getting data from Twitter for research purposes (or, really, any old purpose you might have).

## Setup (please do this before the tutorial begins)

Using the Twitter REST API (the method we'll use to perform our searches) requires a Twitter account and a client for accessing the API.  These are really easy to set up, and it'll be helpful if everyone can have them set up before we start.

### Get a Twitter account

If you already have a Twitter account, you can just use it to access the API.  But if you think you're going to be regularly performing these API searches, you may want to set up a separate account specifically for doing the searches, since calls to the API are rate limited and this could potentially interfere with other things you want to do with your account.  Setting up an account should be easy, but contact me if you're having trouble.

### Set up a Twitter app for accessing the API

Accessing the API also requires an "app" login for your account. This is also easy to set up.

* If you don't have a phone number tied to your account, you have to add one before adding an app: https://support.twitter.com/articles/110250 (You can remove your number once the app is created.)
* Go to https://apps.twitter.com/ and log in
* Hit the "Create New App" button at the top right
* Enter an app name, description, and website; these can just be placeholders, really, since you're going to be the only one seeing them. (If you're stuck on name/description, mine are "SeeTweet" and "maps tweets for linguistic research")
* Check that you have read the agreement and hit "Create your Twitter application"
* On the app page, click on the "Permissions" tab
* Set permissions to "Read only" & click "Update settings"
* Click the "Keys and Access Tokens" tab, scroll to the bottom, and click the "Create my access token" button

That's all you need to do ahead of time; we'll input the access keys during the tutorial itself!
