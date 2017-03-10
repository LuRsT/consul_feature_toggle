# Consul feature toggle

A Consul environment to show how to use consul for configuring projects

## Requirements

You only need to install `docker-compose` (https://docs.docker.com/compose/install/)

## How to set it up

    # Build containers
    docker-compose build

    # Run containers
    docker-compose up

Then go to http://localhost:8500/ui (this is the consul UI), press on "Key/Value" and add a new Key/value called "name" with a string (don't forget the surrounding ") of your choosing.

![screenshot](http://imgur.com/aJImlukl.png)

Have fun reading the logs that change depending on what you pick :).
