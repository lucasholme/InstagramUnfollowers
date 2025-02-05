import instaloader
import sqlite3

def get_followers(username, password):
    L = instaloader.Instaloader()
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, username)

    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)

    return followers

def check_value(cursor, username):
    cursor.execute("SELECT EXISTS(SELECT 1 FROM Instagram WHERE username = ?)", (username,))
    exists = cursor.fetchone()[0]
    return exists

def insert_value(cursor, conn, username, followers):
    with conn:
        cursor.execute("INSERT INTO Instagram (username, followers) VALUES (:username, :followers)", {"username": username, "followers": followers})

def create_database(cursor, conn, username, followers):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Instagram (
        username TEXT,
        followers TEXT
    )
    ''')

    if check_value(cursor, username) == 0:
        followers = ",".join(followers)
        insert_value(cursor, conn, username, followers)

    cursor.execute("SELECT followers FROM Instagram WHERE username = ?", (username,))
    data = cursor.fetchone()

    followers_list = data[0].split(",")

    return followers_list

def new_followers(data, followers):
    unfollowers = []
    for follower in data:
        if follower not in followers:
            unfollowers.append(follower)
    
    return unfollowers

def update_database(cursor, conn, username, followers):
    cursor.execute("DELETE FROM Instagram WHERE username = ?", (username,))
    conn.commit()

    followers = ",".join(followers)
    insert_value(cursor, conn, username, followers)

def main():
    username = ""
    password = ""
    followers = get_followers(username, password)

    conn = sqlite3.connect("Instagram.db")
    cursor = conn.cursor()

    data = create_database(cursor, conn, username, followers)
    unfollowed = new_followers(data, followers)

    update_database(cursor, conn, username, followers)

    print(unfollowed)

    conn.close()

if __name__ == "__main__":
    main()
