# webhook-bridge

`webhook-bridge` is a simple python micro service you can run on heroku to bridge two webhooks that don't agree on the formatting.

The only bridge currently supported converts from ProdPad Ideas to Slack posts in the format of my liking. Want more? send me some [feedback](mailto:hello@untangleconsulting.io). Like it? [Let everyone know](https://twitter.com/calvingiles).

The private details of your webhooks live only in the parametes of the url you post to in the first place - to use the hook requires no code changes whatsoever.

## To use

Push to heroku and find your `{heroku_app_name}.heroku.com`.

Create an incoming webhook on slack and copy the url (I will call it `{slack_hook_url}` (something like `https://your-company.slack.com/services/hooks/incoming-webhook?token=jGIb86HJD35agksoHnn28`).

Create an outgoing webhook on Prodpad and set the url to:

`{heroku_app_name}.heroku.com/interpret_webhook?hook_url={slack_hook_url}`


## Customising behaviour

Change 'translator.translate_payload()` to modify the behaviour of the hook.

## Feedback?

Get in touch on [twitter](https://twitter.com/calvingiles), [email](mailto:hello@untangleconsulting.io) or by posting an [issue](https://github.com/calvingiles/webhook-bridge/issues) if you have any feedback or just want to say you like it.


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
