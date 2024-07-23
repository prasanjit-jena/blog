# Django Blog Application

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd blog_project
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

5. Run the server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

- `POST /api/posts/`: Create a new post
- `GET /api/posts/`: List all posts
- `GET /api/posts/<id>/`: Retrieve a single post
- `PUT /api/posts/<id>/`: Update a post
- `DELETE /api/posts/<id>/`: Delete a post
- `POST /api/posts/<post_id>/comments/`: Create a comment for a post
- `GET /api/posts/<post_id>/comments/`: List comments for a post

## Authentication

- `POST /api/token/`: Obtain a token
- `POST /api/token/refresh/`: Refresh a token
