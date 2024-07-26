# ourCommonsScraper

This program is designed to manage and track the various expenses and related claims of Members of Parliament. The application interfaces with a MySQL database to store, retrieve, and update data on members' expenses, travel claims, hospitality claims, and contracts. The database schema includes several tables that detail the structure and relationships between different types of data.

### Key Features

* **Members of Parliament Management** :
* Stores details about members including their first name, last name, constituency, caucus, and salary.
* **Contact Information** :
* Manages contact details for each member, including email, website, office addresses, and phone numbers.
* **Committee Participation** :
* Records the committees each member is part of, including committee names and abbreviations.
* **Parliamentary Associations and Interparliamentary Groups** :
* Tracks membership and executive committee participation in various parliamentary associations and interparliamentary groups.
* **Expense Tracking** :
* Logs various expenses incurred by members, categorized by type (travel, hospitality, contract, etc.), and includes reporting period details.
* **Travel Claims** :
* Manages travel-related expenses, including costs of transportation, accommodation, meals, and incidental expenses.
* Tracks individual trips with detailed information about dates, departure, and destination points, and purpose.
* **Hospitality Claims** :
* Records hospitality expenses, including details about the date, location, purpose, and total cost of events hosted by members.
* **Contract Claims** :
* Stores information on expenses related to contracts with suppliers for various services such as office supplies, advertising, and utilities.
* **Travellers** :
* Keeps records of individuals who travel on behalf of members, detailing their names and types (e.g., member, employee).
* **Events** :
* Logs events related to hospitality claims, including details about the type of event, the supplier, and the total cost.

### Database Schema

The database schema comprises multiple tables to organize and relate the data efficiently:

* `MembersOfParliament`: Information about MPs.
* `Contact`: Contact details for MPs.
* `Committees`: Committee memberships.
* `ParliamentaryAssociationsAndInterparliamentaryGroups`: Memberships in parliamentary associations and groups.
* `Expense`: General expenses data.
* `TravelClaim`: Specific travel-related expenses.
* `HospitalityClaim`: Expenses related to hosting events.
* `ContractClaim`: Expenses related to contracts with suppliers.
* `Traveller`: Details of individuals traveling on behalf of MPs.
* `Travel`: Detailed travel records for each trip.
* `Event`: Records of events associated with hospitality claims.
