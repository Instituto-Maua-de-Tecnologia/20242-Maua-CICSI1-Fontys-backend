# Instituto-Maua-de-Tecnologia-20242-Maua-CICSI1-Fontys-backend-B
This is the repository for the backend of the collaberative project between Fontys and Maua. The project is an application that allows the coordinator of Maua to generate schedules for the different classes based on the teacher availability.

## Install instructions
Create a virtual env (optional)
`python -m venv venv`
Install the required packages
`pip install -r requirements.txt`
Copy the `.env.EXAMPLE.env` to `.env` and update the values

## Branching
Our main branches are
`dev` for staging changes
`prod` for the production version of the application

Besides that we split up work branches as follows:
- feature/
Used for new features.
- bug/
For bugfixes.
- chore/
Refactoring, making tweaks to existing code / features.

For the name use lowercase kebab-case e.g. `feature/generate-schedule-chatgpt`.

## Pull requests
When you are done with any of the work branches, create a pull request to dev where someone who did not commit any work in the branch should review it before it can be merged.

