# CO2 Emission App

This project is a Streamlit application that connects to a PostgreSQL database to display the PostgreSQL version. It utilizes the `psycopg2` library for database connectivity and reads the database configuration from a `secrets.toml` file.

## Project Structure

```
co2emis
├── app.py               # Main application code
├── streamlit
│   └── secrets.toml     # Database configuration
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd co2emis
   ```

2. **Install required packages**:
   Make sure you have Python installed, then install the necessary packages using pip:
   ```
   pip install streamlit psycopg2
   ```

3. **Configure the database connection**:
   Edit the `streamlit/secrets.toml` file to include your PostgreSQL database configuration:
   ```toml
   [postgres]
   host = "your_host"
   port = "your_port"
   dbname = "your_dbname"
   user = "your_user"
   password = "your_password"
   ```

4. **Run the application**:
   Start the Streamlit application by running:
   ```
   streamlit run app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://localhost:8501` to view the application.

## Usage

The application will connect to the PostgreSQL database and display the version of the database. If there are any connection issues, an error message will be displayed.