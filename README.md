
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



## Running the Tests

To run the unit tests, use the following command:

```bash
python manage.py test
```

This will execute all the unit tests in the project.


### Test Description

Here is a description of the tests included in this project:

#### User Registration Tests

- `test_user_registration_valid_data`: Tests user registration with valid data, including a valid username and matching passwords.
- `test_user_registration_invalid_data`: Tests user registration with invalid data, including an empty username and non-matching passwords.

#### User Login and Logout Tests

- `test_user_login_valid_credentials`: Tests user login with valid credentials.
- `test_user_login_invalid_credentials`: Tests user login with invalid credentials.
- `test_user_logout`: Tests user logout after successful login.

#### Home View Tests

- `test_home_view_authenticated_user`: Tests access to the home view by an authenticated user.
- `test_home_view_unauthenticated_user`: Tests redirection to the login page when an unauthenticated user tries to access the home view.

#### Session Fixation Test

- `test_session_id_changes_on_login`: Tests that a user's session ID changes after login, ensuring session fixation protection.

### Test Results

5. After running the tests, review the test results in the console. Each test case should provide feedback on whether it passed or failed.
