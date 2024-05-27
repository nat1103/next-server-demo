# Utiliser l'image officielle Ubuntu comme base
FROM ubuntu:latest

# Installer MariaDB
RUN apt-get update && apt-get install -y mariadb-server

# Créer un utilisateur non-root
RUN useradd -u 1001 -m mysqluser

# Créer les répertoires nécessaires et changer le propriétaire
RUN mkdir -p /var/run/mysqld && chown -R mysqluser:mysqluser /var/lib/mysql /var/run/mysqld

# Copier le script d'entrée
COPY entrypoint.sh /usr/local/bin/

# Donner les permissions appropriées au script d'entrée
RUN chmod +x /usr/local/bin/entrypoint.sh

# Changer l'utilisateur
USER mysqluser

# Exposer le port MySQL
EXPOSE 3306

# Définir le point d'entrée
ENTRYPOINT ["entrypoint.sh"]
