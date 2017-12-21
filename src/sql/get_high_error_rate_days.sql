SELECT error_rates.day, error_rates.rate AS error_rate
  FROM (
        SELECT day,
               CAST(error_count AS REAL) / CAST(total_count AS REAL) AS rate
          FROM daily_http_request_counts
       ) AS error_rates
 WHERE error_rates.rate > 0.01;
