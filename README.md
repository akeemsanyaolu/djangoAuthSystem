
This repository contains a Django project. This README provides step-by-step instructions on how to set up and run the project.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python: [Download and install Python](https://www.python.org/downloads/).
- Pip: Pip is usually included with Python. You can check its version with `pip --version`.

## Project Setup

1. **Clone the Repository:**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/akeemsanyaolu/yetti_assessment.git
   ```


2. **Create a Virtual Environment (Optional):**

   ```bash
   cd yetti_assessment
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Project Dependencies:**

   Install the required Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```


4. **Generate a Secret Key:**

   You can use the provided Python script to generate a secret key. Execute the script:

   ```bash
   python generate_secret_key.py
   ```

5. **Run the Django Development Server:**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The Django project should now be running. Access it on your web browser at `http://localhost:8000/`.
