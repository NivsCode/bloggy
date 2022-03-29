# Assumptions
- Users can create blogs to which they can submit multiple posts.

# Getting Started
## Prerequisites

* (docker and docker-compose)[https://docs.docker.com/desktop/mac/install]

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
