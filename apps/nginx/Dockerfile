FROM ubuntu

# Installer NGINX
RUN apt-get update && apt-get install -y nginx

# Exposer le port 80
EXPOSE 80

# Exécuter NGINX
CMD [ "nginx", "-g", "daemon off;" ]
