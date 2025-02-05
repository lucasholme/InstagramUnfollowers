📸 Instagram Unfollower Tracker
===============================

This script tracks Instagram followers using Instaloader and stores data in an SQLite database. It helps identify users who have unfollowed an account.

🚀 Features
-----------

-   ✅ **Fetch Followers** -- Retrieves the latest followers of an Instagram account.

-   ✅ **Track Unfollowers** -- Compares previous and current followers to find unfollowers.

-   ✅ **Store Data** -- Saves follower lists in an SQLite database for tracking changes.

-   ✅ **Auto-Update** -- Keeps the database up to date with every run.

📥 Installation
---------------

### 1️⃣ Clone the Repository

sh

```
git clone https://github.com/your-username/instagram-unfollower-tracker.git
cd instagram-unfollower-tracker

```

### 2️⃣ Install Dependencies

Make sure you have Python 3.x installed. Then, install Instaloader:

sh

```
pip install instaloader
```

🛠️ Usage
---------

### 1️⃣ Add Your Instagram Credentials

Edit the `main()` function in `tracker.py` and replace:

python

```
username = "your_instagram_username"
password = "your_instagram_password"
```

### 2️⃣ Run the Script

sh

```
python tracker.py
```

It will:

-   Log in to Instagram

-   Fetch current followers

-   Compare with previously stored followers

-   Print users who unfollowed

🗄️ Database Structure
----------------------

The script uses an SQLite database `Instagram.db` with a table:

| Column | Type | Description |
| --- | --- | --- |
| username | TEXT | Instagram username |
| followers | TEXT | Comma-separated list of followers |

🔥 Example Output
-----------------

css

```
['user1', 'user2', 'user3']
```

This means `user1`, `user2`, and `user3` unfollowed the account since the last check.

🛑 Notes
--------

-   **Enable 2FA App Passwords** -- If Instagram blocks logins, use an app password.

-   **Rate Limits** -- Instagram may temporarily block excessive login attempts.

📜 License
----------

This project is open-source under the MIT License.
