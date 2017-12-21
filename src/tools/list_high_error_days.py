#! /usr/bin/env python3

"""
    Prints days with a high rate of errors.
"""

import sys
from pathlib import Path
import psycopg2


def main():
    conn = psycopg2.connect("dbname=news user=vagrant")
    cur = conn.cursor()

    try:
        sql = Path('../sql/get_high_error_rate_days.sql').read_text()
        cur.execute(sql)

        def format_row(row):
            day = row[0].strftime("%B %d, %Y")
            error_percent = "{0:.1f}%".format(row[1] * 100)
            return "%s - %s errors" % (day, error_percent)

        for row in cur.fetchall():
            print(format_row(row))
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
