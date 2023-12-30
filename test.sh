#!/bin/bash

set -eux

mypy plur
isort plur test_plur.py
black plur test_plur.py
ruff check --fix plur test_plur.py
coverage run $(which pytest)
coverage html
