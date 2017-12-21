# Logs Analysis Project

Project submission for the Logs Anaylsis Project for the Full Stack Web Developer Udacity Nanodegree program.

## Setup

Before using the tools, perform the **required** preliminary setup by using the `make.py` script. The `setup` command will create all the views listed in the [Views](#views) section below.

```sh
chmod u+x make.py && ./make.py setup
```

Additionally, please remember to make tools executable.

```sh
chmod u+x src/tools/*.py
```

To remove views and possibly other artifacts, use `make.py clean`.

```sh
chmod u+x make.py && ./make.py setup
```

## Usage

### Views

#### `articles_ok_logs`

Articles are associated with their logs.

```sql
CREATE view articles_ok_logs AS
SELECT log.*, articles.id AS article_id
  FROM log
       JOIN articles
         ON log.path=concat('/article/', articles.slug)
 WHERE log.status='200 OK';
```

##### Preview

```text
news=> select * from articles_ok_logs order by time desc limit(5);
            path             |      ip       | method | status |          time          |   id    | article_id
-----------------------------+---------------+--------+--------+------------------------+---------+------------
 /article/so-many-bears      | 203.0.113.219 | GET    | 200 OK | 2016-07-31 19:59:55+00 | 3355778 |         29
 /article/candidate-is-jerk  | 198.51.100.78 | GET    | 200 OK | 2016-07-31 19:59:41+00 | 3355773 |         26
 /article/candidate-is-jerk  | 198.51.100.78 | GET    | 200 OK | 2016-07-31 19:59:39+00 | 3355774 |         26
 /article/bears-love-berries | 192.0.2.115   | GET    | 200 OK | 2016-07-31 19:59:38+00 | 3355769 |         25
 /article/candidate-is-jerk  | 192.0.2.115   | GET    | 200 OK | 2016-07-31 19:59:37+00 | 3355771 |         26
(5 rows)
```

#### `author_article_views`

Lists authors with the total number of page views for their articles.

```sql
  CREATE VIEW author_article_views AS
  SELECT articles.author AS author_id,
         count(articles.author) AS total_article_views
    FROM articles_ok_logs
         JOIN articles
           ON articles_ok_logs.article_id = articles.id
GROUP BY articles.author;
```

##### Preview

```text
news=> select * from author_article_views order by author_id;
 author_id | total_article_views
-----------+---------------------
         1 |              507594
         2 |              423457
         3 |              170098
         4 |               84557
(4 rows)
```

#### `daily_http_request_counts`

Lists HTTP request traffic counters per day.

```sql
  CREATE VIEW daily_http_request_counts AS
  SELECT http_requests_count.day,
         http_requests_count.count AS total_count,
         http_error_counts.count AS error_count
    FROM
         (
             SELECT date_trunc('day', log.time) AS day, count(*)
               FROM log
           GROUP BY day
         ) AS http_requests_count,
         (
             SELECT date_trunc('day', log.time) AS day, count(*)
               FROM log
              WHERE log.status SIMILAR TO '(4|5)%' -- 400, 500 series status codes
           GROUP BY day
         ) AS http_error_counts
   WHERE http_requests_count.day = http_error_counts.day;
```

##### Preview

```text
news=> select * from daily_http_request_counts limit(3);
          day           | total_count | error_count
------------------------+-------------+-------------
 2016-07-01 00:00:00+00 |       38705 |         274
 2016-07-02 00:00:00+00 |       55200 |         389
 2016-07-03 00:00:00+00 |       54866 |         401
(3 rows)
 ```

### Tools

#### List top 3 viewed articles

```sh
$ cd tools
$ ./get_top_three_articles.py
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views
```

#### List most popular authors

```sh
$ cd tools
$ ./list_authors_by_popularity.py
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
```

#### List days with high error rate

```sh
$ ./list_high_error_days.py
July 17, 2016 - 2.3% errors
```
