# About
This is a smarthome school project. It has some iot and ai inference.

# System Architecture
![System Architecture](./public/system_architecture.jpg)
# Requirements

1. node (Can use nvm to version management, I'm using nvm --lts so it's node v20.12.1 (npm v10.5.0))
2. python
3. docker compose

# Run
## Backend + Database
1. `docker compose up` or `docker-compose up` (whatever works for you)
2. `cd app`
3. Create a virtual environment if needed, then `pip install -r requirements.txt`
4. Create the .env file from .env.example. And fill in the fields.
5. Run backend: `fastapi dev app.py --host 0.0.0.0 --port 8000`
6. Initialize the rooms in the database: `python database/scripts/init_light.py`
7. Modify database/scripts/init_camera_links.py for the camera links you want for your app. Then run python database/scripts/init_camera_links.py
## Frontend
1. `cd smarthome`
2. Install dependencies, use: `yarn` or `npm install`.
3. Create the .env file from .env.example. And fill in the fields.
4. Run the frontend: `yarn dev` (add `--host` to expose ip).
