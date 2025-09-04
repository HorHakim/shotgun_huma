# Petit bot pour shotgun une place camping à la fête de l'huma
Si le bot réussit à shotgun il envoie à l'utilisateur un mail pour le prevenir. La place camping reste disponible 10 min dans le panier.

Il faut créer un fichier .env qui contient ces 4 champs :

MAIL='le mail pour recevoir la notification'

MAIL_PASSWORD='la clef pour pouvoir envoyer un mail cf en bas du readme pour avoir un tuto pour la reccup'

HUMA_MAIL='La mail du compte sur le site de la fête de l'huma'

HUMA_PASSWORD='Le mdp du compte sur le site de la fête de l'huma'

### Voici comment récupérer le "MAIL_PASSWORD" (mot de passe d’application):

1) sur votre compte GMAIL : dans Sécurité → Mots de passe d’application.

2)Choisis “Mail” et “Appareil : autre (PythonBot)” par exemple.

3) Google va te donner un mot de passe à 16 caractères (style abcd efgh ijkl mnop).
