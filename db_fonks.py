from db import get_connection

# ==================== USER ====================

def get_user_id(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM users WHERE username = %s AND password = %s",
        (username, password)
    )
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row[0] if row else None


def user_ekle(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )

    conn.commit()
    cur.close()
    conn.close()
    return True


def user_sil(uid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM users WHERE id = %s",
        (uid,)
    )

    conn.commit()
    cur.close()
    conn.close()
    return True  

# ==================== NOTES ====================

def not_ekle(uid, title, content):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO notes (user_id, title, content) VALUES (%s, %s, %s)",
        (uid, title, content)
    )

    conn.commit()
    cur.close()
    conn.close()


def not_sil(not_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM notes WHERE id = %s",
        (not_id,)
    )

    conn.commit()
    cur.close()
    conn.close()


def notes_getir(uid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, user_id, title, content FROM notes WHERE user_id = %s ORDER BY id DESC",
        (uid,)
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()

    notes = []
    for r in rows:
        notes.append({
            "id": r[0],
            "user_id": r[1],
            "title": r[2],
            "notlar": r[3]
        })

    return notes


def not_guncelle(not_id, yeni_baslik, yeni_icerik):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE notes SET title = %s, content = %s WHERE id = %s",
        (yeni_baslik, yeni_icerik, not_id)
    )

    conn.commit()
    cur.close()
    conn.close()
    return True
