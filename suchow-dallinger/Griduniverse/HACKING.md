# Developing Griduniverse

The frontend of Griduniverse is implemented in JavaScript
and must be compiled to create static/scripts/bundle.js
before being served by a web server.

## Installing dev tools

First [install `yarn`](https://yarnpkg.com/en/docs/install).
(`yarn` is similar to `npm` but better,
and uses the same package repository.)

Next run `yarn` to install the dependencies:

    $ yarn

## Building bundle.js

To update bundle.js:

    $ yarn run build

To watch for changes and rebuild bundle.js whenever you save:

    $ yarn run dev

While running the dev command, you can start the experiment in debug mode
with Dallinger and then adjust the URL in your browser to port 6000.
This proxies the Dallinger webserver (port 5000) for everything except `/static`,
where it serves the current contents of the `static` directory.
It also automatically reloads whenever the bundle is updated.

Note: Updates to the bundle should be committed to version control.

## Managing dependencies

To add a new dependency, use the `yarn add` command:

    $ yarn add snargle-fraster

If it's a dependency only at build time, use `yarn add [pkg] --dev`.

This updates the `yarn.lock` file, which records the specific
releases which were used. Other developers will get those
releases when they run `yarn`. Updates to `yarn.lock`
should be committed to version control.

## Running Bots

See [documentation](http://docs.dallinger.io/en/latest/running_bots.html) for
instructions on running bots in Dallinger. We recommend using the Chrome
web driver, needed to render the WebGL components. In `config.txt`, set:

```
webdriver_type = chrome
```

Use the classes in bot.py as an example of how to create your own bot. You can
create a class, then change the `bot_policy` option in `demo.py` to your class.
