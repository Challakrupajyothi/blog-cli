import mysql.connector
from mysql.connector import Error

# Database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='blog_db'
    )

# Add new post with tags
def create_post():
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    tags = input("Enter comma-separated tags: ").split(',')

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        post_id = cursor.lastrowid

        for tag in tags:
            tag = tag.strip().lower()
            cursor.execute("SELECT id FROM tags WHERE name = %s", (tag,))
            tag_row = cursor.fetchone()
            if tag_row:
                tag_id = tag_row[0]
            else:
                cursor.execute("INSERT INTO tags (name) VALUES (%s)", (tag,))
                tag_id = cursor.lastrowid

            cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (%s, %s)", (post_id, tag_id))

        conn.commit()
        print("✅ Post created successfully.")
    except Error as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        conn.close()

# View all post titles
def view_titles():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM posts")
        titles = cursor.fetchall()
        if titles:
            print("📚 Blog Posts:")
            for title in titles:
                print(f" - {title[0]}")
        else:
            print("No posts found.")
    finally:
        cursor.close()
        conn.close()

# View post by title
def view_post_by_title():
    title = input("Enter the post title: ")
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM posts WHERE title = %s", (title,))
        result = cursor.fetchone()
        if result:
            print(f"\n📄 Content:\n{result[0]}")
        else:
            print("Post not found.")
    finally:
        cursor.close()
        conn.close()

# Search posts by tag
def search_by_tag():
    tag = input("Enter a tag to search posts: ").strip().lower()
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.title 
            FROM posts p
            JOIN post_tags pt ON p.id = pt.post_id
            JOIN tags t ON t.id = pt.tag_id
            WHERE t.name = %s
        """, (tag,))
        results = cursor.fetchall()
        if results:
            print("🔍 Posts with tag:")
            for r in results:
                print(f" - {r[0]}")
        else:
            print("No posts found with that tag.")
    finally:
        cursor.close()
        conn.close()

# Menu
def main():
    while True:
        print("\n=== Blog Manager CLI ===")
        print("1. Create New Post")
        print("2. View All Post Titles")
        print("3. View Post by Title")
        print("4. Search Posts by Tag")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_post()
        elif choice == '2':
            view_titles()
        elif choice == '3':
            view_post_by_title()
        elif choice == '4':
            search_by_tag()
        elif choice == '5':
            print("👋 Exiting Blog Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
