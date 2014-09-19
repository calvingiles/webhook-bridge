# Project interpret

## For develompent

* Clone the repo
* Get the [Heroku Toolbelt](https://toolbelt.heroku.com/)
* push to your heroku account. [Calvin](https://github.com/calvingiles) is keeper of the keys for this one for now.

### requirements.txt and virtualenv

To set up a veritual env locally, `cd` to the root of the project and run:

```bash
$ virtualenv venv
```

This will reate a `venv` folder with virtualenv wrapped python and pip executables. To activate them in the current shell, use:

```bash
$ source venv/bin/activate
```

To install the requirements from the existing `requirements.txt` file, run:

```bash
$ pip install -r requirements.txt --allow-all-external
```

If you subsequently change the configuration by installing additional packages via the venv pip, use `pip freeze` to create a new requirements.txt file.

```bash
$ pip freeze > requirements.txt
```

With a locally installed venv, start your app in a heroku-like manor with `foreman start web`.

## API

Set the outgoing webhook of a service to the url this is served on followed by `interpret_webhook`.

Pass the destination webhook url as the `hook_url` parameter.

Change the function `translator.translate_payload()` to convert the passed payload to the desired destination payload.

POST json data.