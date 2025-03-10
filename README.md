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
   or..
In pycharm community edition, press "File" at the top, "Project from Version Control"
and paste https://github.com/skullblaze56/project1 into the URL text box and press ok.

Every step here should be done in the terminal in pycharm community. (Bottom left, 3rd option from the bottom).
Copy paste the commands.
   
3. Create a virtual environment:
   ```bash
   # Windows
   Copy this command below into terminal!
   python -m venv venv

   # Mac/Linux
   Copy this command below into terminal!
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```bash
   # Windows
   Copy this command below into terminal!
   venv\Scripts\activate

   # Mac/Linux
   Copy this command below into terminal!
   source venv/bin/activate
   ```
   
   Note: Your command prompt should now show (venv) at the beginning

5. Install required packages:
   ```bash
   Copy this command below into terminal!
   pip install -r requirements.txt
   ```

6. Initialize the database:
   ```bash
   Copy this command below into terminal!
   python setup_db.py
   ```
   You should see the message "Database initialized successfully!"

7. Run the application:
   ```bash
   Copy this command below into terminal!
   python run.py
   ```
   You should see output indicating that the Flask server is running

8. Open your web browser and go to:
   ```
   Copy this website below into google!
   http://localhost:5000
   ```
   You should see a table displaying student records
