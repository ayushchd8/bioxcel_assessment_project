# Django Backend for Relationship Graph

This is a Django backend application for managing relationship data and providing API endpoints for a frontend application. The backend supports fetching the entire dataset, showing data on a graph, and fetching child nodes for a given parent node.

## Requirements

- Python 3.7+
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

### 2. Create Virtual Environment

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Apply Migrations

python manage.py migrate

### 5. Load Initial Data

Inside bioxcel_assessment_project folder, run "python manage.py load_relationship_data" to load the data to DB.

### 6. Run the Development Server

"python manage.py runserver"
