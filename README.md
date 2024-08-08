# ScheduPulse

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [User Stories](#user-stories)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
ScheduPulse is a meeting organizer application designed to help you plan and manage your meetings effectively. With features like meeting creation, editing, and deletion, along with a list of available rooms, ScheduPulse ensures you have everything you need to keep your schedule on track.

## Features
- User authentication and profile management
- Create, edit, and delete meetings
- View a list of meetings and available rooms
- Responsive design for use on various devices
- Dynamic form validation using JavaScript

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/schedupulse.git
    ```
2. Navigate to the project directory:
    ```sh
    cd schedupulse
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
6. Set up the database:
    ```sh
    python manage.py migrate
    ```
7. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage
1. Navigate to `http://127.0.0.1:8000` in your web browser.
2. Register a new user account or log in with your superuser credentials.
3. Start managing your meetings!

## Testing
To run the tests for the application, use the following command:
```sh
python manage.py test