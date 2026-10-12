# [Backstage](https://backstage.io)

This is your newly scaffolded Backstage App, Good Luck!

## Environment variables

Secrets are kept out of `app-config.yaml` and read from environment variables
(e.g. `clientId: ${AUTH_GITHUB_CLIENT_ID}`). Locally they live in a
`.env` file, which is git-ignored and must never be committed.

| Variable                    | Used for                          |
| --------------------------- | --------------------------------- |
| `AUTH_GITHUB_CLIENT_ID`     | GitHub OAuth app client ID        |
| `AUTH_GITHUB_CLIENT_SECRET` | GitHub OAuth app client secret    |

First time only, create your `.env` from the template and fill in the values:

```sh
cp .env.example .env
```

Backstage does not load `.env` by itself, so load it into your shell before
starting the app (run this from this folder, in every new terminal):

```sh
set -a && source .env && set +a
```

`set -a` exports every variable defined in `.env` so the Backstage process
can see it. Check it worked with `echo $AUTH_GITHUB_CLIENT_SECRET`.

## Start the app

```sh
yarn install
set -a && source .env && set +a
yarn start
```
