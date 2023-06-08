# Elevator System Project

This project implements a simplified elevator system using Python and Django, specifically Django REST Framework (DRF). The system allows users to initialize elevators, manage elevator operations, and handle user requests for elevator services.

## Features

- Create and initialize the elevator system with N elevators.
- Fetch all requests for a given elevator.
- Fetch the next destination floor for a given elevator.
- Fetch whether the elevator is currently moving up or down.
- Mark an elevator as not working or under maintenance.
- Open or close the elevator door.
- Save user requests for elevator services.

## Requirements

- Python (version 3.11.3)
- Django (version 4.2.2)
- Django REST Framework (version 3.14.0)

## Installation

1. Clone the repository:
- git clone https://github.com/your-username/elevator-system.git

2. Install the Python dependencies:
- pip install -r requirements.txt

## Update the database settings in settings.py
## Run database migrations
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


## API Endpoints

### Initialize the elevator system

- **URL:** `/api/v1/elevators/initializesystem/`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "num_elevators": 3
  }
  ```
Response:
```json
[
  {
    "elevator_id": 1,
    "name": "Elevator 1",
    "status": "Working",
    "current_floor": 0,
    "direction": "Upward",
    "doors_open": false
  },
  {
    "elevator_id": 2,
    "name": "Elevator 2",
    "status": "Working",
    "current_floor": 0,
    "direction": "Upward",
    "doors_open": false
  },
  {
    "elevator_id": 3,
    "name": "Elevator 3",
    "status": "Working",
    "current_floor": 0,
    "direction": "Upward",
    "doors_open": false
  }
]
```

### 2. Fetch all requests for a given elevator
- **URL**: `/api/v1/elevators/<elevator_id>/get_elevator_requests/`
- Method: GET
- Response:
``` json
[
  {
    "id": 1,
    "elevator": 1,
    "floor": 3,
    "timestamp": "2023-06-07T12:34:56Z"
  },
  {
    "id": 2,
    "elevator": 1,
    "floor": 5,
    "timestamp": "2023-06-07T12:36:00Z"
  }
]
```

### 3. Fetch the next destination floor for a given elevator
- **URL**: `/api/v1/elevators/<elevator_id>/nextfloor/`
- **Method**: GET
- Response:
```json
{
  "next_destination_floor": 4
}
```

### 4. Fetch if the elevator is moving up or down currently
- **URL**: `/api/v1/elevators/<elevator_id>/elevatorcurrentdirection/`
- **Method**: GET
- Response:
```json
{
  "elevator_direction": "Upward"
}
```

### 5. Mark an elevator as not working or in maintenance
- **URL**: `/api/v1/elevators/<elevator_id>/undermaintenance/`
- **Method**: PUT
- Response:
```json
{
  "elevator_status": "Under_Maintenance"
}
```

### 6. Open or close the elevator door
- **URL**: `/api/v1/elevators/<elevator_id>/openclosedoor/`
- **Method**: PUT
- Response:
```json
{
  "elevator_doors_open": false
}
```

### 7. Save a user request for elevator service
- **URL**: `/api/v1/elevators/<elevator_id>/userrequest/`
- **Method**: POST
- Request Body:
```json
{
  "floor": 7
}
```
Response:
```json
{
  "id": 3,
  "elevator": 1,
  "floor": 7,
  "timestamp": "2023-06-07T12:40:00Z"
}
```

## Contribution
Contributions are welcome! If you find any issues or want to add new features, please create a pull request.

## License
This project is licensed under the MIT <u>License</u>.
```
This software is released under the MIT License. It grants permission to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the software, allowing for both personal and commercial use.
The software is provided "as is," without any warranties or conditions.
```







