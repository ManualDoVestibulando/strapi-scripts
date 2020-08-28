# strapi-scripts
Python scripts for automatically interacting with Strapi's API and with the admin console to compensate for API shortcomings (specifically relational fields) 

Specifically for interacting with the API backend of manualdovestibulando.com.br

## Assumptions and Instructions

- Grades are loaded into CSV files inside the mdv-strapi folder
    - Enem grades have the fields for each exam's individual scores and for the admission course
    - Fuvest grades have fields for each exam's scores, essay and admission course
    - Both have fields for quotas, with options "AC", "EP" and "PPI"
- Courses and institutes are loaded into the same CSV
    - The file contains fields for course full name, acronym and institute
    - There are no institutes or courses with the exact same name
    - Courses are related to grades through a relational field
- Grades for essays are in the name of the picture files that contain the essays
    - Scripts for generating these files are in the essays folder
    - Enem grades should be loaded into a .xlsx file, filling the first column of the first page in chronological order of submission, following the pattern:

        sum-comp1-comp2-comp3-comp4-comp5_randomNumber

    - Fuvest grades are loaded into a .xslx as above, following the pattern:

        grade_randomNumber

    - These scripts must be run from the folder containing the .png image files
    - Exam year must be added manually to the script
- Student accounts are linked via Google Drive
    - Links and titles are loaded into a CSV
    - Relational field to course must be filled in manually