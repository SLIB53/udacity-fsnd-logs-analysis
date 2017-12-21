  CREATE VIEW author_article_views AS
  SELECT articles.author as author_id,
         count(articles.author) as total_article_views
    FROM articles_ok_logs
         JOIN articles
         ON articles_ok_logs.article_id = articles.id
GROUP BY articles.author;
