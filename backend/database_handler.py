import psycopg2

def query_friends_list(conn, id: str):
    cur = conn.cursor()

    cur.execute("""
            SELECT client_id AS id1, friend_id AS id2 FROM friendships
            WHERE %s in (client_id, friend_id);
            """, (id,))
    
    query_res = cur.fetchall()

    return query_res

def query_client(conn, id:str) -> tuple:
    cur = conn.cursor()

    cur.execute("""
                SELECT email_address, id, name FROM clients
                WHERE id=%s;
                """, (id,))
    
    query_res = cur.fetchone()

    return query_res

def query_request(conn, id: str):
    cur = conn.cursor()

    cur.execute("""
                SELECT status FROM money_requests 
                WHERE id=%s;
                """, (id,))
    
    query_res = cur.fetchone()

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
                SELECT mr.id, mr.requestee_id, mr.amount, mr.message, mr.paid_amount, c.name, c.email_address 
                FROM money_requests mr LEFT OUTER JOIN clients c 
                ON mr.requestee_id = c.id
                WHERE mr.requester_id = %s
                AND mr.status NOT IN ('accepted', 'declined');
                """, (id,))
    
    return cur.fetchall()

def query_requestee_reqs(conn, id: str):
    cur = conn.cursor()

    cur.execute("""
                SELECT mr.id, mr.requester_id, mr.amount, mr.message, mr.paid_amount, c.name, c.email_address 
                FROM money_requests mr LEFT OUTER JOIN clients c
                ON mr.requester_id = c.id
                WHERE mr.requestee_id = %s
                AND mr.status NOT IN ('accepted', 'declined');
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
                WHERE id = %s;
                """, (status, id))
    
    return "success" if cur.rowcount != -1 else "failure"