# TransistorDatabase
When selecting electronic components such as resistors or capacitors only one or two parameters need to be taken into account. But in the case of transistors, several parameters need to be considered before making a choice. This Python Script and API helps get information and choose equivalent transistors for an appliance from a database of upto 4000 Transistors.

## API Details
Read the [API Documentation](API_README.md) for detailed documentation of the API
API can be tested at https://api.amateurcraft.tech

### Testing API with docker
  Requisites: Docker, Docker Compose and git

  1. clone repo and change dir
     ```
     git clone https://github.com/AalmanSadath/TransistorDatabase.git
     cd TransistorDatabase
     ```
  2. Build and Run container
     ```
     docker-compose up --build
     ```
  3. Base url for testing http://localhost:8080

## Python Script Details
### Functions
  1. Get Information Regarding a certain Transistor
  2. Get Equivalent Transistors of a certain Transistor and their Information
  3. Add a new transistor to Database
  
### Requirements
  1. Python 3.7 or above
  2. MySQL Server and Workbench
  3. Premade Database of Transistors
  
### Installation

#### Windows

  1. Click on Code and then on Download zip
  2. Extract components of zip file into folder
  3. Open Command Prompt and run the following to install required modules
  ```
  python -m pip install mysql-connector-python tabulate requests
  ```
  4. Open Command Prompt as admin and move to the location of mysql.exe, use:
  ```
  cd C:/Wherever-mysql.exe-is-stored/
  ```
  5. Add the databases to MySQL using mysql.exe (run one after the other):
  ```
  mysql.exe -u YourMySQLUsername -p transitors < C:/Folder-extracted-from-github/transistors.sql
  
  mysql.exe -u YourMySQLUsername -p newtransitors < C:/Folder-extracted-from-github/newtransistors.sql
  ```
  6. In the TransistorDatabase.py Script, change the MySQL Config user and password under mydb and newdatabse and Pastebin config. Pastebin api_dev_key can be obtained by registering and opening https://pastebin.com/doc_api.
 
