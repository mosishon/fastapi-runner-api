[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-blue)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-2.18.0-green)](https://fastapi.tiangolo.com/)

# FastAPI Runner API

This is a project that provides a FastAPI-based API for running code snippets securely and efficiently. It offers endpoints for user and admin authentication, creating new users, and executing code.

## Features

- **User Authentication**: Provides endpoints for both admin and regular user login to access the API securely.
- **User Management**: Allows admins to create new users.
- **Code Execution**: Users can submit code files along with necessary arguments to execute code snippets.

## Setup

1. **Clone the Repository**:
-
    ```bash
    git clone https://github.com/mosishon/fastapi-runner-api.git
    cd fastapi-runner-api
    ```

2. **Environment Configuration**:
- Ensure you have Docker installed on your system.
- Set up your constants in `constants.py`:
  ```python
  RUNNER_ADDRESS = "http://runner:8000"  # RUNNER CONTAINER ADDRESS
  REDIS_HOST = "redis"  # REDIS CONTAINER NAME
  REDIS_PORT = 6379
  ```

3. **Build and Run Docker Containers**:
- Run the following command to build and start your Docker containers:
  ```bash
  cd fastapi-runner-api
  docker build -t fastapi-runner-api .
  docker run -dit --name {name} --cpus=1 --memory="1g" --network=runner-network -p {PORT}:80 --restart always fastapi-runner-api
  ```

4. **Access the API**:
- The API will be accessible at `http://localhost:{PORT}`.

 ## Description
- This web service is designed to handle user management tasks while separating the execution of code into another container. By doing so, it ensures that even if potentially malicious code is submitted, it will be executed in a separate container, thus maintaining the necessary security measures. This separation also enhances the development of the API by decoupling the code execution aspect from the main functionality.


## Supervisoring

- The project utilizes Supervisor to manage Nginx and Uvicorn processes.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is built using FastAPI, Nginx, and Docker.
- Special thanks to contributors and the open-source community for their valuable libraries and tools.

---
