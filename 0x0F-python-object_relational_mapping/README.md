## 0x0F. Python - Object-relational mapping
This directory contains Python scripts that demonstrate Object-Relational Mapping (ORM) using SQLAlchemy with MySQL databases. The project aims to bridge the gap between Python's object-oriented programming and relational databases, allowing for more intuitive database interactions.

Key concepts covered in this project include:
- Connecting to a MySQL database from a Python script
- Executing SQL queries using Python
- Mapping Python classes to database tables (ORM)
- Handling database operations using SQLAlchemy
- Implementing relationships between database tables

The scripts in this directory showcase various operations such as selecting, filtering, and manipulating data in MySQL databases using both raw SQL queries and SQLAlchemy ORM. They also demonstrate how to create models, establish relationships between models, and perform CRUD (Create, Read, Update, Delete) operations using these models.

This project serves as an introduction to more advanced database management techniques in Python, bridging the gap between SQL knowledge and Python programming skills.


| File Name                                | Description                                                  |
|------------------------------------------|--------------------------------------------------------------|
| `0-select_states.py`                     | Select states from a database.                               |
| `1-filter_states.py`                     | Filter states based on a condition.                          |
| `2-my_filter_states.py`                  | Custom filter for states.                                    |
| `3-my_safe_filter_states.py`             | Custom safe filter for states.                               |
| `4-cities_by_state.py`                   | Retrieve cities grouped by state.                            |
| `5-filter_cities.py`                     | Filter cities based on a condition.                          |
| `7-model_state_fetch_all.py`             | Fetch all states using a model.                              |
| `8-model_state_fetch_first.py`           | Fetch the first state using a model.                         |
| `9-model_state_filter_a.py`              | Filter states using a model.                                 |
| `10-model_state_my_get.py`               | Custom state retrieval using a model.                        |
| `11-model_state_insert.py`               | Insert a new state using a model.                            |
| `12-model_state_update_id_2.py`          | Update a state with ID 2 using a model.                      |
| `13-model_state_delete_a.py`             | Delete a state with name 'a' using a model.                  |
| `14-model_city_fetch_by_state.py`        | Fetch cities by state using a model.                         |
| `100-relationship_states_cities.py`      | Define a relationship between states and cities.             |
| `101-relationship_states_cities_list.py` | List states and associated cities using relationships.       |
| `102-relationship_cities_states_list.py` | List cities and their associated states using relationships. |
| `model_city.py`                          | Model for city objects.                                      |
| `model_state.py`                         | Model for state objects.                                     |
| `relationship_city.py`                   | Define a relationship for city objects.                      |
| `relationship_state.py`                  | Define a relationship for state objects.                     |
