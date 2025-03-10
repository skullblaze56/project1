# Student Records Flask Application

A simple Flask web application that displays student records from a database.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher (Download from [python.org](https://www.python.org/downloads/))
- Git (Download from [git-scm.com](https://git-scm.com/downloads))

## Step-by-Step Setup Instructions

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd flask-student-records
   ```

2. Create a virtual environment:
   ```bash
   # Windows
   python -m venv venv

   # Mac/Linux
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate

   # Mac/Linux
   source venv/bin/activate
   ```
   
   Note: Your command prompt should now show (venv) at the beginning

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Initialize the database:
   ```bash
   python setup_db.py
   ```
   You should see the message "Database initialized successfully!"

6. Run the application:
   ```bash
   python run.py
   ```
   You should see output indicating that the Flask server is running

7. Open your web browser and go to:
   ```
   http://localhost:5000
   ```
   You should see a table displaying student records
