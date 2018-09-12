#!/bin/bash

set -ue

# Allow setting either DATABASE_URL (takes precedence) or POSTGRESQL_*
POSTGRESQL_USERNAME="${POSTGRESQL_USERNAME:-kompassi}"
POSTGRESQL_PASSWORD="${POSTGRESQL_PASSWORD:-secret}"
POSTGRESQL_HOSTNAME="${POSTGRESQL_HOSTNAME:-postgres}"
POSTGRESQL_DATABASE="${POSTGRESQL_DATABASE:-kompassi}"
export DATABASE_URL="${DATABASE_URL:-psql://$POSTGRESQL_USERNAME:$POSTGRESQL_PASSWORD@$POSTGRESQL_HOSTNAME/$POSTGRESQL_DATABASE}"

# Allow setting either BROKER_URL (takes precedence) or RABBITMQ_*
RABBITMQ_USERNAME="${RABBITMQ_USERNAME:-kompassi}"
RABBITMQ_PASSWORD="${RABBITMQ_PASSWORD:-secret}"
RABBITMQ_HOSTNAME="${RABBITMQ_HOSTNAME:-rabbitmq}"
RABBITMQ_VHOST="${RABBITMQ_VHOST:-}"
export BROKER_URL="${BROKER_URL:-amqp://$RABBITMQ_USERNAME:$RABBITMQ_PASSWORD@$RABBITMQ_HOSTNAME/$RABBITMQ_VHOST}"
export KOMPAQ_URL="${KOMPAQ_URL:-$BROKER_URL}"

exec "$@"
