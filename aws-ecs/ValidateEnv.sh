#!/bin/bash

echo "Verify required Environment variables"
POSTGRE_DB_NAME="${POSTGRE_DB_NAME:-default_value}"
if [[ ${POSTGRE_DB_NAME} == "default_value" ]];
then
    echo "Log: POSTGRE_DB_NAME environment variable not found. Exiting program"    
    exit 1
else
    echo "Log: POSTGRE_DB_NAME environment variable value is ${POSTGRE_DB_NAME}"
fi

POSTGRE_DB_USER="${POSTGRE_DB_USER:-default_value}"
if [[ ${POSTGRE_DB_USER} == "default_value" ]];
then
    echo "Log: POSTGRE_DB_USER environment variable not found. Exiting program"    
    exit 1
else
    echo "Log: POSTGRE_DB_USER environment variable value is ${POSTGRE_DB_USER}"
fi

POSTGRE_DB_PASSWORD="${POSTGRE_DB_PASSWORD:-default_value}"
if [[ ${POSTGRE_DB_PASSWORD} == "default_value" ]];
then
    echo "Log: POSTGRE_DB_PASSWORD environment variable not found. Exiting program"    
    exit 1
else
    echo "Log: POSTGRE_DB_PASSWORD environment variable value found"
fi

POSTGRE_DB_HOST="${POSTGRE_DB_HOST:-default_value}"
if [[ ${POSTGRE_DB_HOST} == "default_value" ]];
then
    echo "Log: POSTGRE_DB_HOST environment variable not found. Exiting program"    
    exit 1
else
   echo "Log: POSTGRE_DB_HOST environment variable value is ${POSTGRE_DB_HOST}"
fi

POSTGRE_DB_PORT="${POSTGRE_DB_PORT:-default_value}"
if [[ ${POSTGRE_DB_PORT} == "default_value" ]];
then
    echo "Log: POSTGRE_DB_PORT environment variable not found. Exiting program"    
    exit 1
else
    echo "Log: POSTGRE_DB_NAME environment variable value is ${POSTGRE_DB_PORT}"
fi


exit 0