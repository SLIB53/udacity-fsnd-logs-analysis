#! /usr/bin/env python3

"""
    Make file for running log analysis scripts.

    Before executing scripts in this project, run
        $ ./make.py setup
"""

import sys
import argparse
from pathlib import Path
import psycopg2


def setup():
    """Sets up views required for tools."""

    print("Creating articles_ok_logs view...")
    create_articles_ok_logs()


def clean():
    """Removes all tool artifacts."""

    print("Ensuring removal of articles_ok_logs view...")
    delete_articles_ok_logs()


def create_articles_ok_logs():
    """Loads articles_ok_logs view into the news database."""

    conn = psycopg2.connect("dbname=news user=vagrant")
    cur = conn.cursor()

    try:
        sql = Path('src/sql/create_view_articles_ok_logs.sql').read_text()
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as db_error:
        print("Warning: ", db_error)
    except:
        raise
    finally:
        cur.close()
        conn.close()


def delete_articles_ok_logs():
    """Deletes (idempotent) articles_ok_logs view in the news database."""

    conn = psycopg2.connect("dbname=news user=vagrant")
    cur = conn.cursor()

    try:
        cur.execute("DROP VIEW articles_ok_logs;")
        conn.commit()
    except psycopg2.Error:
        pass
    except:
        raise
    finally:
        cur.close()
        conn.close()


def main():
    parser = argparse.ArgumentParser(prog='make')
    parser.add_argument('commands', nargs='+', help="setup, clean")

    commands_buffer = []

    for command in parser.parse_args().commands:
        if command == "setup":
            commands_buffer.append(setup)
        elif command == "clean":
            commands_buffer.append(clean)
        else:
            print("Error: Unrecognized command:", command)
            sys.exit(1)

    for command in commands_buffer:
        try:
            command()
        except:
            print("Error: Python Exception:", sys.exc_info()[0])
            sys.exit(1)


if __name__ == '__main__':
    main()
