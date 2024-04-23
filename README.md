# Python Programming Module Capstone
#### Purwadhika Module 1 Python Capstone Project (DTIDS On Campus Batam 2024)

This program aims to simulate an inventory and renting system for books that implements CRUD, although changes made to the data collection types and display outputs of this program allows flexibility to mimic other similar renting systems.

The primary collection data type for this program is a list, more specifically, a list containing dictionaries as its elements. the dictionaries themselves represent an individual book entry, which consists of the primary key ('index'), and seven other keys ('title', 'author', 'pages', 'allowed_rent_days', 'price_per_day', 'rentable', 'days_being_rented') which describe the characteristics of each book.

Below are some keys that are crucial to be defined, due to its role and/or relationship with other variables in this program:

1. 'index': The primary key of this program, which serves as the primary means of conducting CRUD operations. This key will be asked as input whenever the user intends to run a primary feature

2. 'allowed_rent_days': The maximum number of days allowed to be allocated to a customer should they wish to rent the book. Constrained to always be larger than or equal to days_being_rented, as all rent bookings made beforehand must specify its renting period as being less than or equal to the allowed maximum in order to be a valid booking

3. 'price_per_day': Denotes the daily fee charged to the customer for a particular book they are renting

4. 'rentable': Boolean that indicates whether a book is currently available for rent or not. Indicates that a customer is currently renting the book if specified as False, and therefore, constrains days_being_rented as being greater than zero when False and equal to zero when True

5. 'days_being_rented': The amount of days that a customer is currrently renting the book for. It signals that a customer is currently renting the book when its value is larger than zero and not being rented out if zero. Also constrains rentable to False if larger than zero, and constrains it to True if equal to zero

IMPORTANT NOTES: 
- The update feature implemented in this program permits the manipulation of non-primary keys without constraints, although some variable interdependencies do exist and are explained above. It is therefore important for the Admin user to take heed of the interplays that each variable has before conducting the update operation. These constraint mechanisms are active for customer features
