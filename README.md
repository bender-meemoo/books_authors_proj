"# books_authors_proj" 

Objectives:
Practice using the Django Shell to run ORM commands to manipulate our database
Practice many-to-many relationships
Create a new project called books_authors_proj and an app called books_authors_app. Use the following diagram as a guide for designing your models:



 Create the Book class model
 
 Create the Author class model
 
 Create and run the migration files to create the tables in your database
 
 Create a .txt file where you'll save each of your queries from below
 
 Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
 
 Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
 
 Add a new text field in the authors table called 'notes'.
 
 Create and run the migration files to update the table in your database.
 
 Query: Change the name of the C Sharp book to C#
 
 Query: Change the first name of the 4th author to Bill
 
 Query: Assign the first author to the first 2 books
 
 Query: Assign the second author to the first 3 books
 
 Query: Assign the third author to the first 4 books
 
 Query: Assign the fourth author to the first 5 books (or in other words, all the books)
 
 Query: Retrieve all the authors for the 3rd book
 
 Query: Remove the first author of the 3rd book
 
 Query: Add the 5th author as one of the authors of the 2nd book
 
 Query: Find all the books that the 3rd author is part of
 
 Query: Find all the authors that contributed to the 5th book
 
 Submit your .txt file that contains all the queries you ran in the shell

Assignment: Books/Authors with Templates
Objectives:
Practice incorporating a many-to-many relationship in a full-stack application
Using the same project from the previous assignment, create an application that does the following:



 Add a template for creating books that also displays a table of all books in the database
 
 Complete the route for adding a book to the database
 
 Add a template that displays a specific book and its details, including all the authors associated with the given book
 
 Create a form on the specific book template that has a dropdown of all the authors in the database. The "Add" button should add the selected author to the given book.
 
 Add a template for creating authors that also displays a table of all authors in the database
 
 Complete the route for adding an author to the database
 
 Add a template that displays a specific author and its details, including all the books associated with the given author
 
 Create a form on the specific author template that has a dropdown of all the books in the database. The "Add" button should add the selected book to the given author.
 
 SENSEI BONUS: Have the dropdown menus only include 
