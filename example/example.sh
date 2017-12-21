#! /usr/bin/env bash

cd .. # go to project base

# Run setup

# ./make.py clean setup

# Run tools

cd src/tools

printf "\nAnswers:\n\n"

printf "1. What are the most popular three articles of all time?\n\n"
./list_top_three_articles.py
printf '\n'

printf "2. Who are the most popular article authors of all time?\n\n"
./list_authors_by_popularity.py
printf '\n'

printf "3. On which days did more than 1%% of requests lead to errors?\n\n"
./list_high_error_days.py
printf '\n'
