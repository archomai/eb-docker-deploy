## Secrets

**`.secrets/base.json`**

`RAVEN_DSN`: Sentry의 SecurityToken

```json
{
  "SECRET_KEY": "<Django settings SECRET_KEY value>",
  "RAVEN_DSN": "https://<SecurityToekn>@sentry.io/..."
}
```

**`.secrets/local.json`**

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "localhost",
      "NAME": "<DB name>",
      "USER": "<DB username>",
      "PASSWORD": "<DB user password>",
      "PORT": <Port number, default:5432>
    }
  }
}
```

