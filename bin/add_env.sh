#!/bin/bash

echo "This is a script to write env variables to .env file for pipenv"

# Main Django Project Settings

read -p "Django Secret Key: " django_secret_key
read -p "Django Debug: " django_debug
read -p "Django Allowed Hosts (Specify one at a time separated by a space): " django_allowed_hosts

# Database

read -p "Django Use Database: " django_use_db
read -p "Django Database Host: " django_db_host
read -p "Django Database Name: " django_db_name
read -p "Django Database User: " django_db_user
read -p "Django Database Password: " django_db_password

# Media and Static files

read -p "Django Static Root: " django_static_root
read -p "Django Media Root: " django_media_root

# Logging

read -p "Django Logging: " django_logging
read -p "Django Logging File (Path): " django_logging_file

# Mails

read -p "Django Use Mails App: " django_use_mails
read -p "Django Mails Host: " django_mails_host
read -p "Django Mails Port: " django_mails_port
read -p "Django Mails Use TLS: " django_mails_use_tls
read -p "Django Mails Use SSL: " django_mails_use_ssl
read -p "Django Mails Email Address: " django_mails_email_address
read -p "Django Mails User: " django_mails_user
read -p "Django Mails Password: " django_mails_password

# ReCaptcha

read -p "Django Recaptcha Public Key: " django_recaptcha_public_key
read -p "Django Recaptcha Private Key: " django_recaptcha_private_key

# Yandex Mertica

read -p "Django Yandex Metrica Counter ID: " django_yandex_metrica_counter_id


read -p "Do you want to overwrite .env file? [Y/n]: " agre

if [[ "$agre" == Y || "$agre" == y ]]
then
{
    echo DJANGO_SECRET_KEY=$django_secret_key
    echo DJANGO_DEBUG=$django_debug
    echo DJANGO_ALLOWED_HOSTS=$django_allowed_hosts

    echo DJANGO_USE_DB=$django_use_db
    echo DJANGO_DB_NAME=$django_db_name
    echo DJANGO_DB_USER=$django_db_user
    echo DJANGO_DB_PASSWORD=$django_db_password
    echo DJANGO_DB_HOST=$django_db_host

    echo DJANGO_STATIC_ROOT=$django_static_root
    echo DJANGO_MEDIA_ROOT=$django_media_root

    echo DJANGO_LOGGING=$django_logging
    echo DJANGO_LOGGING_FILE=$django_logging_file

    echo DJANGO_MAILS_USE=$django_use_mails
    echo DJANGO_MAILS_HOST=$django_mails_host
    echo DJANGO_MAILS_PORT=$django_mails_port
    echo DJANGO_MAILS_USE_TLS=$django_mails_use_tls
    echo DJANGO_MAILS_USE_SSL=$django_mails_use_ssl
    echo DJANGO_MAILS_EMAIL_ADDRESS=$django_mails_email_address
    echo DJANGO_MAILS_USER=$django_mails_user
    echo DJANGO_MAILS_PASSWORD=$django_mails_password

    echo DJANGO_RECAPTCHA_PUBLIC_KEY=$django_recaptcha_public_key
    echo DJANGO_RECAPTCHA_PRIVATE_KEY=$django_recaptcha_private_key

    echo DJANGO_YANDEX_METRICA_COUNTER_ID=$django_yandex_metrica_counter_id

} > .env

echo "Переменные окружения записаны"

else

echo "Отменена"

fi
