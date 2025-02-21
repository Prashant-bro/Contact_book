# Contact Book

A simple Contact Book application built using Python and Tkinter with MySQL database integration.

## Features
- Add new contacts (Name, Phone, Email, Address)
- Search for contacts by name
- Display all saved contacts
- Update existing contact details
- Delete contacts from the database

## Technologies Used
- Python
- Tkinter (GUI)
- MySQL (Database)

## Installation and Setup

### Prerequisites
Make sure you have Python installed along with the required dependencies:
- Install Python (https://www.python.org/downloads/)
- Install MySQL Server (https://dev.mysql.com/downloads/installer/)
- Install required Python libraries:

```bash
pip install mysql-connector-python
```

### Database Setup
1. Open MySQL and create a database:
   ```sql
   CREATE DATABASE ContactBook;
   USE ContactBook;
   ```
2. Create a `contacts` table:
   ```sql
   CREATE TABLE contacts (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       phone VARCHAR(15) NOT NULL,
       email VARCHAR(255),
       address TEXT
   );
   ```

### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/Prashant-bro/Contact_book.git
   cd Contact_book
   ```
2. Update database credentials in `contact_book.py`:
   ```python
   db = m.connect(host="localhost", user="your_username", passwd="your_password", database="ContactBook", charset="latin1")
   ```
3. Run the application:
   ```bash
   python contact_book.py
   ```

## Usage
- Enter a name in the search box and click `SEARCH` to find contacts.
- Click `ADD CONTACT` to open a new window and enter details for a new contact.
- Click `UPDATE CONTACT` to modify an existing contact's phone number.
- Click `DELETE` to remove a contact from the database.

## Contributing
Feel free to fork this repository and contribute to the project!



