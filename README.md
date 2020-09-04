# Flask :crystal_ball:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Flask controllers
* Flask routing
* Flask templates
* Flask static files

# Assignments' list 

## Assignment 1

### Description

The task will consist of two parts, the first part is to prepare a page with a list of students, and the second part is to prepare a page with personal information of those students.

**Required for the first part**

* ```/students/``` url should return the list of students when requesting a GET query

   - Students' information should be in the form of a dictionary and have the following fields.
      - Id
      - Name
      - Surname
      - Gender (male / female)
      - Status (active / deactive)
      - Image (url)
      - Bio

* Only first name, last name, bio and picture should be seen on this page
* Only students with active status should be seen
* The student's name and surname must be capitalized. Regardless of the position in the dictionary
* If a student's bio is empty, the default is "I'm a student at Tech academy."
* Any styles can be given on the page. For example, give styles to make a student's picture rounded. Written styles must be written in a separate css file and added to the template.

**Required for the second part**

* When you apply to the ```/students/1/``` url with a GET query, a page with the first student's personal information should open. Note that the numbers in the url must match the students' ids
* All fields should be on this page

The templates used on both pages must be inherited from the main **base.html**. The block mechanism should be considered in the main base template and the appropriate static files should be included.


**Powered by [TechAcademy](https://www.tech.edu.az/)**

