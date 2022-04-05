# Problem statement
A single user blog with comment and replies feature. App allows guest users to comment on posts as well.

# Getting Started

## Prerequisites

- Docker
- Python3
- Pip3

## Installation

1. Clone this repo in your local workspace
2. Create environment variables
   ```
   mv .env.example .env
   ```
3. Install dependencies
   ```
   make install-dependencies
   ```
4. Initialize dependencies.
   ```
   make init-depedencies
   ```
5. Apply migrations
   ```
   make migrate
   ```
6. Run the service
   ```
   make run
   ``` 

You can also run server after migrations by using `make run-with-migration`

# Notes
- accounts app handles user authentication and registration
- pages app handles static pages
- blog_handler app handles posts, comments.

# Known issues
- Re hiding the comment box
- Displaying history with user information
- Versioning for post and comment instances is available, can be manipulated from backend.