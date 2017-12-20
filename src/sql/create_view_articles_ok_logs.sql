CREATE view articles_ok_logs AS
SELECT log.*, articles.id AS article_id
  FROM log
       JOIN articles
       ON log.path=concat('/article/', articles.slug)
 WHERE log.status='200 OK';
