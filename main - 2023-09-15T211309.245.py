import psycopg2

# Database connection parameters
db_params = {
    'host': 'your_host',
    'database': 'your_database',
    'user': 'your_user',
    'password': 'your_password'
}

# Sample mushroom finding data
mushroom_data = {
    'longitude': 123.456,
    'latitude': 45.678,
    'species_name': 'Amanita muscaria',
    'date_found': '2023-09-15',
    'found_by': 'John Doe'
}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)

    # Create a cursor object
    cursor = connection.cursor()

    # SQL statement to insert data
    insert_query = """
    INSERT INTO mushroom_findings (longitude, latitude, species_name, date_found, found_by)
    VALUES (%(longitude)s, %(latitude)s, %(species_name)s, %(date_found)s, %(found_by)s);
    """

    # Execute the query with the provided data
    cursor.execute(insert_query, mushroom_data)

    # Commit the transaction
    connection.commit()

    print("Data inserted successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
