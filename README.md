# Problem statements
A single user blog with comment and replies feature
# Getting Started

## Prerequisites

[Docker for mac](https://docs.docker.com/desktop/mac/install)

## Installation

1. Clone this repo in your local workspace

2. Initialize dependencies.
   ```
   make init-depedencies
   ```
3. Run the services.
   ```
   make run
   ``` 
4. Apply migrations
   ```
   make migrate
   ```

# Notes
- accounts app handles user authentication and registration
- pages app handles static pages
- blog_handler app handles posts, comments.

# Known issues
- Re hiding the comment box
- displaying history with user information