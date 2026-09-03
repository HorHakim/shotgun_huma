# Petit bot pour shotgun une place camping à la fête de l'huma

Si le bot réussit à shotgun il envoie à l'utilisateur un mail pour le prevenir. La place camping reste disponible 10 min dans le panier.

## Pré-requis

- installer [chromium]
- installer [uv](https://docs.astral.sh/uv/getting-started/installation/)
- avoir [un mot de passe d'application Google](https://myaccount.google.com/apppasswords?continue=https://myaccount.google.com/security)

## Utilisation

- `cp .env.example .env`
- remplir `.env` avec les vraies valeurs
- `uv run shotgun-huma`
