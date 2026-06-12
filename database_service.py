import sqlite3

DB_NAME = "workouts.db"

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS workouts (
    video_id TEXT PRIMARY KEY,
    channel TEXT,
    title TEXT,
    duration INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS workout_today (
    id INTEGER PRIMARY KEY,
    video_id TEXT,
    channel TEXT,
    title TEXT,
    duration INTEGER
)
""")

conn.commit()


def insert_workout(workout_data):
    cursor.execute("""
    INSERT OR REPLACE INTO workouts
    (video_id, channel, title, duration)
    VALUES (?, ?, ?, ?)
    """, (
        workout_data["video_id"],
        workout_data["channel"],
        workout_data["title"],
        workout_data["duration"]
    ))
    conn.commit()


def delete_workout(workout_id):
    cursor.execute(
        "DELETE FROM workouts WHERE video_id=?",
        (workout_id,)
    )
    conn.commit()


def get_all_workouts():
    cursor.execute("""
    SELECT video_id, channel, title, duration
    FROM workouts
    """)

    rows = cursor.fetchall()

    return [
        {
            "video_id": r[0],
            "channel": r[1],
            "title": r[2],
            "duration": r[3]
        }
        for r in rows
    ]


def get_workout_today():
    cursor.execute("""
    SELECT id, video_id, channel, title, duration
    FROM workout_today
    WHERE id=0
    """)

    rows = cursor.fetchall()

    return [
        {
            "id": r[0],
            "video_id": r[1],
            "channel": r[2],
            "title": r[3],
            "duration": r[4]
        }
        for r in rows
    ]


def update_workout_today(workout_data, insert=False):

    cursor.execute("""
    INSERT OR REPLACE INTO workout_today
    (id, video_id, channel, title, duration)
    VALUES (?, ?, ?, ?, ?)
    """, (
        0,
        workout_data["video_id"],
        workout_data["channel"],
        workout_data["title"],
        workout_data["duration"]
    ))

    conn.commit()