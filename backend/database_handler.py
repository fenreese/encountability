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