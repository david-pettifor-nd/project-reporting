#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 <<-EOSQL
    CREATE USER $DATABASE_USER WITH CREATEDB PASSWORD '$DATABASE_PASSWORD';
    CREATE DATABASE $DATABASE_NAME with owner $DATABASE_USER;
EOSQL