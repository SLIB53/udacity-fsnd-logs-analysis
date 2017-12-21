# Logs Analysis Project

Project submission for the Logs Anaylsis Project for the Full Stack Web Developer Udacity nanodegree.

## Setup

Before using the tools, perform the **required** preliminary setup by using the `make.py` script.

```sh
chmod u+x make.py && ./make.py setup
```

Make scripts executable:

```sh
chmod u+x src/tools/*.py
```

## Usage

### List top 3 viewed articles

```sh
$ cd tools
$ ./get_top_three_articles.py
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views
```

### List most popular authors

```sh
$ cd tools
$ ./list_authors_by_popularity.py
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
```

### List days with high error rate

```sh
$ ./list_high_error_days.py
July 17, 2016 - 2.3% errors
```
