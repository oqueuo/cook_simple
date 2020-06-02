import sqlite3

conn = sqlite3.connect(get_file_path('nu.db'))
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Pages (url, title, summary, body, words)
        VALUES (?, ?, ?, ?, ?)''', 
        (
            row['url'], 
            row['title'], 
            row['summary'], 
            row['body'], 
            row['words']
        )
    )
    cur.close()
    conn.commit()
    conn.close()
