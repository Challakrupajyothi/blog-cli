# Blog CLI Project

A command-line interface (CLI) application to manage blog posts. This project allows users to create, view, and search for blog posts, and manage tags associated with each post. It uses a MySQL database to store the posts, tags, and a linking table for associating posts with tags.

## Features

- **Create Blog Posts**: Add new posts with titles, content, and tags.
- **View Posts**: List all blog titles and view content for a specific post.
- **Search Posts by Tag**: Find posts by tag.
- **Database**: MySQL database with tables for posts, tags, and a post_tags linking table.

## Setup

### Requirements

- Python 3.x
- MySQL
- `mysql.connector` library
- 
# 🤖 Technical Help Chatbot (CLI-based)

This is a simple command-line based chatbot built with Python using **ChatterBot**. It provides technical support by answering frequently asked questions and interacting with users based on a predefined knowledge base.

---

## 📌 Features

- Trained using **ChatterBot Corpus** and custom conversation data.
- CLI-based interface for user interaction.
- Provides answers to basic technical help and support questions.
- Uses SQLite or `.db` to store chatbot knowledge and conversation history.

---

## 🛠️ Technologies Used

- Python 3.x
- [ChatterBot](https://github.com/gunthercox/ChatterBot)
- SQLite (via ChatterBot)
- tqdm (for training progress)
- Git for version control
