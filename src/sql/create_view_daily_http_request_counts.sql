  CREATE VIEW daily_http_request_counts AS
  SELECT http_requests_count.day,
         http_requests_count.count as total_count,
         http_error_counts.count as error_count
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
