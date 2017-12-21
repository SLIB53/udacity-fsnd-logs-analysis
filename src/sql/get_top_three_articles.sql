  SELECT articles.title, count(articles.id) AS article_count
    FROM articles_ok_logs
         JOIN articles
           ON articles_ok_logs.article_id = articles.id
GROUP BY articles.id
ORDER BY article_count DESC
LIMIT(3);
