#!/bin/bash

if [ "$1" = 'python' ]; then
    exec 'python'
fi

exec "$@"