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

def insert_request(conn, info: dict):
    cur = conn.cursor()

    cur.execute("""
                INSERT INTO money_requests (id, requester_id, requestee_id, amount, message, status)
                VALUES (%s, %s, %s, %s, %s, %s);
                """, 
                (info["id"], info["requesterId"], info["requesteeId"], info["amount"], info["message"], info["requestStatus"].lower()))
    
    return "something happened i think" 

