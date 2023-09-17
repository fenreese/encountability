import psycopg2

def query_friends_list(conn, id: str):
    cur = conn.cursor()

    cur.execute("""
            SELECT client_id AS id1, friend_id AS id2 FROM friendships
            WHERE %s in (client_id, friend_id);
            """, (id,))
    
    query_res = cur.fetchall()

    return query_res

def query_profiles(conn, id: list):
    cur = conn.cursor()

    cur.execute("""
                SELECT email_address, id, name FROM clients
                WHERE id in %s;
                """, (id,))
    
    query_res = cur.fetchall()

    return query_res

def query_created_reqs(conn, id: str):
    cur = conn.cursor()

    cur.execute("""
                SELECT id FROM money_requests
                WHERE requester_id = %s;
                """, (id,))
    
    return cur.fetchall()

def query_requestee_reqs(conn, id: str):
    cur = conn.cursor()

    cur.execute("""
                SELECT id FROM money_requests
                WHERE requestee_id = %s;
                """, (id,))
    
    return cur.fetchall()

def insert_request(conn, info: dict):
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO money_requests (id, requester_id, requestee_id, amount, message, status)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id;
                """, 
                (info["id"], info["requesterId"], info["requesteeId"], info["amount"], info["message"], info["requestStatus"].lower()))
    
    return "success" if cur.fetchone()[0] else "failure"

def update_request(conn, id: str, status: str):
    cur = conn.cursor()

    cur.execute("""
                UPDATE money_requests
                SET status = %s
                WHERE id = %s
                """, (status, id))
    
    return "success" if cur.rowcount != -1 else "failure"