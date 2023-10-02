
# WeatherService

This microservice is designed to fetch and store temperature data for a specified city, such as Kyiv, on an hourly basis using the OpenWeatherMap API. It also provides the ability to retrieve historical temperature data for a specific day.


## Information

Celery Beat is responsible for scheduling periodic tasks, such as fetching hourly temperature data.

 
Celery Worker processes the scheduled tasks and stores temperature data.

This addition emphasizes the importance of **Redis** as a message broker for Celery and provides instructions on how to start Celery Beat and Celery Worker in that context. So, you should have worhing Redis on your PC.
## Installation and Setup

Clone the project

```bash
  git clone https://link
```

Go to the project directory

```bash
  cd weatherService
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create a `.env` file (from `.env_example`):
```bash
  WEATHER_CITY="Kyiv"
  OPENWEATHER_API_KEY="<your_openweather_api_key>"
  CELERY_BROKER_REDIS_URL="redis://localhost:6379"
  DEBUG=True
  X_TOKEN="f6f06b276a3e66c32893febcf73839c2"
```

Apply database migrations to create the database:
```bash
  python manage.py migrate
```
Start Celery Beat for task scheduling:
```bash
  celery -A weatherService beat
```

Start Celery Worker to process the scheduled tasks:
```bash
  celery -A weatherService worker -l INFO
```
  

Finally, start the microservice:
```bash
  python manage.py runserver
```


Now, your microservice is set up and running, with Celery Beat and Celery Worker handling the scheduled tasks for temperature data retrieval and storage.

## Usage/Examples

### Fetching Hourly Temperature Data

The microservice automatically fetches and stores hourly temperature data for the specified city.

### Retrieving Historical Temperature Data for a Day

To retrieve the historical temperature data for a specific day, use the following request:



```http
GET /api/v1/weather_data/?day=2023-10-02
```


## API Reference

#### Get the historical temperature data for a specific day

```http
GET /api/v1/weather_data/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `X-Token` |  `string`| **Required Header**. Const from .env |
|    `day`  |  `date`  | *Optional*. Format: Y-m-d |

