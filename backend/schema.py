import psycopg2

def init_db(conn: psycopg2.connection):
    cur = conn.cursor()

    cur.execute("""
    CREATE TYPE request_status AS ENUM ('pending', 'accepted', 'declined');
    """)

    # create clients
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        email_address VARCHAR NOT NULL,
        id VARCHAR PRIMARY KEY,
        name VARCHAR NOT NULL
    );
    """)

    # create friendships
    cur.execute("""
    CREATE TABLE IF NOT EXISTS friendships (
        client_id VARCHAR REFERENCES clients (id),
        friend_id VARCHAR REFERENCES clients (id),
        CHECK (client_id > friend_id),
        PRIMARY KEY (client_id, friend_id)
    );
    """)

    # requests
    cur.execute("""
    CREATE TABLE IF NOT EXISTS money_requests (
        id VARCHAR PRIMARY KEY,
        requester_id VARCHAR REFERENCES clients (id),
        requestee_id VARCHAR REFERENCES clients (id),
        amount INT NOT NULL,
        paid_amount INT NOT NULL DEFAULT 0,
        message VARCHAR,
        status request_status,
        PRIMARY KEY (id, requester_id, requestee_id)
    );
    """)

    # group requests
    cur.execute("""
    CREATE TABLE IF NOT EXISTS group_requests (
        id VARCHAR PRIMARY KEY,
        requester_id VARCHAR REFERENCES clients (id),
        amount INT NOT NULL,
        paid_amount INT NOT NULL DEFAULT 0,
        message VARCHAR,
        PRIMARY KEY (id, requester_id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS requests_list (
        id VARCHAR PRIMARY KEY,
        requester_id VARCHAR REFERENCES clients (id),
        amount INT NOT NULL,
        paid_amount INT NOT NULL DEFAULT 0,
        message VARCHAR,
        PRIMARY KEY (id, requester_id)
    );
    """)