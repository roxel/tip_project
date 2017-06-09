#!/bin/sh

echo "running command $1"

case "$1" in
  "sender" )
    python sender.py
    ;;
esac

exec "$@"
