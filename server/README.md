# XQ Queue Manager

A simple web interface and API for managing XQ queues and messages.

## Features

- View all available queues
- Create new queues
- View messages in a queue
- Add new messages to a queue
- Delete messages from a queue
- Poll messages from a queue
- Schedule messages with cron expressions

## Setup

1. Install the required dependencies:

```bash
pip install -r server/requirements.txt
```

2. Make sure Redis is running on localhost:6379

3. Start the server:

```bash
cd /path/to/xq
python server/api.py
```

4. Open your browser and navigate to http://localhost:8000

## API Endpoints

- `GET /api/queues` - List all available queues
- `GET /api/queues/{queue_name}/messages` - List all messages in a queue
- `POST /api/queues/{queue_name}/messages` - Add a new message to a queue
- `DELETE /api/queues/{queue_name}/messages/{message_id}` - Delete a message from a queue
- `POST /api/queues/{queue_name}/poll` - Poll messages from a queue

## Web UI

- `/` - Home page with list of queues
- `/queues/{queue_name}` - Queue detail page with message management