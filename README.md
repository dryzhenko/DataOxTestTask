# Parser for autoria


## Installing using GitHub

1. Install **PostgreSQL** and create a database.
2. Clone the repository: 

    ```bash
    git clone https://github.com/dryzhenko/DataOxTestTask.git
    cd parser
    ```
   
3. Create and activate a virtual environment:

    ```bash
    python -m venv venv 
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables:

    ```bash
    set BASE_URL=<url_autoria>
    set DATABASE_URL=<your db url>
    set POSTGRES_DB=<your postgres db>
    set POSTGRES_USER=<your postgres user>
    set POSTGRES_PASSWORD=<your postgres password>
    ```

6. Run the development server:

    ```bash
    python parser/parser.py
    ```

## Running with Docker

Docker should be installed on your system.

1. Build the Docker containers:

    ```bash
    docker-compose build
    ```

2. Start the Docker containers:

    ```bash
    docker-compose up
    ```


