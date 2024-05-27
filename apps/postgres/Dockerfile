FROM ubuntu:latest

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y postgresql

RUN service postgresql start

# Exposer le port 5432
EXPOSE 5432

# Exécuter le serveur postgres
CMD [ "postgres" ]
