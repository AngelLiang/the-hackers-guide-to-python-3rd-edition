from flask import Flask, Response, render_template
import psycopg2
import psycopg2.extensions
import select

app = Flask(__name__)


def stream_messages(channel):
    conn = psycopg2.connect(database='mydatabase',
                            user='postgres', password='postgres',
                            host='127.0.0.1')
    conn.set_isolation_level(
        psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
    )

    curs = conn.cursor()
    curs.execute('LISTEN channel_%d;' % int(channel))

    while True:
        select.select([conn], [], [])
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop()
            yield 'data: ' + notify.payload + '\n\n'


@app.route('/message/<channel>', methods=['GET'])
def get_messages(channel):
    return Response(stream_messages(channel),
                    mimetype='text/event-stream')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
