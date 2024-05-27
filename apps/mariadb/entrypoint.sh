#!/bin/bash
set -e

# Initialiser la base de données si elle n'existe pas
if [ ! -d "/var/lib/mysql/mysql" ]; then
  mysqld --initialize-insecure --user=mysqluser
fi

# Démarrer MariaDB
exec mysqld --user=mysqluser
