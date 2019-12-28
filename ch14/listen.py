import psycopg2
import psycopg2.extensions
import select

conn = psycopg2.connect(database='mydatabase',
                        user='postgres', password='postgres',
                        host='127.0.0.1')

conn.set_isolation_level(
    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
)

curs = conn.cursor()
curs.execute('LISTEN channel_1;')

while True:
    select.select([conn], [], [])
    conn.poll()
    while conn.notifies:
        notify = conn.notifies.pop()
        print('Got NOTFIFY:', notify.pid, notify.channel, notify.payload)
