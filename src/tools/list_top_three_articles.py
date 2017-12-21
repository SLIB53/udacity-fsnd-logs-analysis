#! /usr/bin/env python3

"""
    Prints the top three most viewed articles.
"""

import sys
from pathlib import Path
import psycopg2


def main():
    conn = psycopg2.connect("dbname=news user=vagrant")
    cur = conn.cursor()

    try:
        sql = Path('../sql/get_top_three_articles.sql').read_text()
        cur.execute(sql)

        for row in cur.fetchall():
            print("%s - %d views" % (row[0], row[1]))
    except psycopg2.Error as db_error:
        print("Error: DB Error:", db_error)
        sys.exit(1)
    except Exception:
        print("Error: Python Exception:", sys.exc_info()[0])
        sys.exit(1)
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    main()
