# cs-messaging-web-app
Customer Service Messaging App API.  
The accompanying frontend is here: https://github.com/dansonmuia/cs-messaging-frontend

## Description
This is a simple API to simulate a customer service messaging app. It is built using FastAPI and a react.js frontend.
It is available here: https://branch.myduka.online, the API is available here: https://branch-api.myduka.online and the docs are here: https://branch-api.myduka.online/docs

## Features

- User login
- Retrieve messages
- Filter messages by customer_id
- Order messages by urgency, and by date(lastest first)
- Send messages
- Assign messages to yourself. This way, multiple agents won't work on the same message.
- Respond to messages
- Quick responses in the UI

## Installation

Here is how to install the app. You can install it locally or in a docker container.

### Installing locally

You need to have python3 and postgresql installed, and a postgresql database created.

1. Clone the repo  
`git clone https://github.com/dansonmuia/cs-messaging-web-app.git`
2. Create a virtual environment  
`cd cs-messaging-web-app`  
`python3 -m venv venv`  
`source venv/bin/activate`  
3. Install the requirements  
`pip install -r requirements.txt`  
4. Export the environment variables  

````
export SECRET_KEY=your_secret_key

export POSTGRES_DB=your_db_name
export POSTGRES_USER=your_db_user
export POSTGRES_PASSWORD=your_db_password

export DB_URL=postgresql://your_db_user:your_db_password@localhost:5432/your_db_name

export ADMIN_EMAIL=your_admin_email
export ADMIN_NAME='Your Name'
export ADMIN_PASSWORD=your_admin_password
````

5. Run migrations:  
`alembic upgrade head`  

6. Initialize app admin and seed messages data:  
`python seed.py`  

7. Run the app:  
`uvicorn app.main:app`  

Open the app in your browser or postman: http://localhost:8000
Docs will be here: http://localhost:8000/docs

### Installing in a docker container

1. Clone the repo  

`git clone https://github.com/dansonmuia/cs-messaging-web-app.git`  

2. Export the environment variables  

Export the environment variables same way as above, but use the following for the DB_URL:  

`export DB_URL=postgresql://your_db_user:your_db_password@branch_pgdb:5432/your_db_name`  

3. Build the docker image and run the containers  

`docker-compose up --build`  

Open the app in your browser or postman: http://localhost:7000

