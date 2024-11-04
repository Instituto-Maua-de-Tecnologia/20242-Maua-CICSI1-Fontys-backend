# Instituto-Maua-de-Tecnologia-20242-Maua-CICSI1-Fontys-backend-B
This repository hosts the backend code for the collaborative scheduling application developed by Instituto Mauá de Tecnologia and Fontys. This application allows the coordinator at Mauá to generate class schedules based on the availability of teachers.

## Installing and running the project.
1. **Create a virtual env**

`python -m venv venv`

2. **Use the virtual env**

`source venv/bin/activate` To activate.

`deactivate` to deactive.

3. **Install the required packages**

`pip install -r requirements.txt`

4. **Configure Environment variables**

Copy the `.env.EXAMPLE.env` to `.env` 

Open the file and update the values

5. **Run the project**

`python main.py` while inside of the virtual env

## Branching
We use specific branches for different stages and types of work. Here’s an overview:

### Main branches
- **Dev:** The development branch used as a staging area
- **Prod:**  The production branch holding the latest stable version

### Work branches
For ongoing work, create branches based on the task type:

- **feature/** - For new features

Example: `feature/generate-schedule`
- **bug/** - For bugfixes

Example: `bug/fix-login-error`
- **chore/**

Example: `chore/update-readme`

Use **lowercase kebab-case** for naming branches, with the task type followed by a descriptive name.

## Pull requests
1. When you've completed work in a feature, bug or chore branch create a **pull request** to merge it into `dev`
2. Assign the **Ready For Review** label to the pull request.
3. Assign a team member who did not contribute to that branch as a **reviewer**. The reviewer should verify the changes before they can be merged.

