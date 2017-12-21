  SELECT authors.name, author_article_views.total_article_views
    FROM author_article_views
         JOIN authors
         ON author_article_views.author_id = authors.id
ORDER BY author_article_views.total_article_views DESC;
