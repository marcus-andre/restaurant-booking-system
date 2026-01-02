# CODE INSTITUTE - PORTFOLIO 4 ASSESSMENT CRITERIA (FULL-STACK TOOLKIT)

## PROJECT PURPOSE
Build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

## MAIN TECHNOLOGIES
* HTML, CSS, JavaScript, Python + Django
* Relational database (PostgreSQL recommended)

---

## 🟢 PASS CRITERIA (Must be achieved to Pass)

### LO1: Agile, Planning & Design (MVC)
* **1.1 UX Design:** Design a Front-End that meets accessibility guidelines, follows UX principles, and provides user interactions.
* **1.2 Responsive Design:** Implement custom HTML/CSS for a responsive Full-Stack application.
* **1.3 Database-Backed App:** Build an MVC app that allows users to store and manipulate data records.
* **1.4 Data Model:** Design a database structure with a minimum of one custom model.
* **1.5 Agile Tool:** Use an Agile tool (GitHub Projects/Jira) to manage planning and implementation.
* **1.6 User Stories:** Document and implement all User Stories and map them within the Agile tool.
* **1.7 PEP8 & Validation:** Python code must conform to PEP8 style guide. HTML/CSS must be validated.
* **1.8 Python Proficiency:** Include sufficient custom Python logic.
* **1.9 Logic Control:** Include functions with compound statements (if conditions, loops).
* **1.10 Readability:** Code must meet standards for comments, indentation, and naming conventions.
* **1.11 Naming Conventions:** File names must be consistent, descriptive, lowercase, and without spaces.
* **1.12 Agile Mapping:** Map User Stories to project goals.
* **1.13 UX Documentation:** Document UX design (wireframes, mockups, diagrams) in the README and show they were followed.

### LO2: Data Model & Business Logic
* **2.1 Database Structure:** Develop a usable database where data is stored consistently.
* **2.2 CRUD:** Functionality for users to Create, Read, Update, and Delete records.
* **2.3 Notifications:** All changes to data should be notified to the relevant user (Flash messages).
* **2.4 Forms:** Implement at least one form with validation for creating/editing models.

### LO3: Authorization & Authentication
* **3.1 Role-Based Auth:** Apply role-based login and registration (e.g., User vs Admin or just Logged-in User).
* **3.2 Login State:** The current login state is reflected to the user (e.g., "Welcome, User" or Login/Logout buttons change).
* **3.3 Restricted Access:** Users cannot access restricted content/functionality without logging in (Routes protection).

### LO4: Testing
* **4.1 Python Testing:** Manual and/or automated tests for functionality, usability, and data management.
* **4.2 JavaScript Testing:** Manual and/or automated tests for JS functionality.
* **4.3 Documentation:** Document all implemented testing in the README.

### LO5: Version Control (Git)
* **5.1 Git Usage:** Use Git & GitHub up to deployment. Commit messages must document the process.
* **5.2 Security:** Commit final code FREE of passwords or security-sensitive info (use .gitignore).

### LO6: Deployment
* **6.1 Cloud Deployment:** Deploy final version to a cloud platform (Heroku) and ensure it matches dev version.
* **6.2 Clean Code:** Deployed code must be free of commented-out code and broken links.
* **6.3 Deployment Docs:** Document the deployment process in the README in English.
* **6.4 Security:** Ensure DEBUG is off, secret keys are hidden in environment variables.

### LO7: Object-Oriented Concepts
* **7.1 Custom Model:** Design a custom data model that fits the project purpose.

---

## 🔵 MERIT CRITERIA (Pass + All below)

* **General:** Fully functioning, well-documented, relational DB app. No logic errors.
* **1.1 UX:** Site is easy to navigate and intuitive.
* **1.2 Templates:** Demonstrates solid understanding of template syntax/logic (Jinja2/Django Templates).
* **1.3 Agile:** Evidence of refining Epics to User Stories to Tasks.
* **1.4 Acceptance Criteria:** Clear acceptance criteria defined for stories.
* **2.1 Feedback:** Immediate and complete feedback on data processes.
* **2.2 Robustness:** Code is free of errors.
* **2.6 Full CRUD:** All CRUD functionality present and working.
* **2.7 UI Updates:** CRUD actions immediately reflected in the UI.
* **3.1 Rationale:** Clear rationale in README addressing target audience and security features.
* **4.1 Bug Evaluation:** Evaluation of bugs found, their fixes, and explanation of any unfixed bugs.
* **5.1 Schema Docs:** Describe data schema fully in README.
* **5.2 Commits:** Commit often, small commits, descriptive messages.
* **6.1 Deployment Docs:** Fully document deployment with consistent formatting.

---

## 🟠 DISTINCTION CRITERIA (Pass + Merit + All below)

* **Real-World App:** Professional-grade UI, publishable quality.
* **UX Principles:** Information hierarchy, user control, consistency, confirmation messages.
* **Accessibility:** Clear conformity to accessibility guidelines.
* **Clean Code:** DRY principles, clear naming, separation of concerns.
* **File Structure:** Organized directories (assets, css, js).
* **Validation:** * HTML (W3C) - No errors.
    * CSS (Jigsaw) - No errors.
    * JS (JSLint) - No major issues.
    * Python (PEP8) - No errors.
* **Defensive Design:** Inputs validated, internal errors handled gracefully, custom 404/500 pages.
* **Security:** Passwords/Keys in env vars, appropriate permissions.

---

## 📝 README REQUIREMENTS
* Must be named `README.md`.
* Must be in English.
* **Deployment Section:** Must cover steps to deploy, files to create (Procfile, requirements.txt), packages to install, environment variables, and steps to clone/run locally.

## ⚠️ CRITICAL FAIL POINTS (Avoid these)
* **Plagiarism:** Any code not written by you must be credited.
* **Security:** Committing `SECRET_KEY` or passwords to GitHub.
* **Debug Mode:** Leaving `DEBUG = True` in production.
* **Empty/Bad Readme:** Missing deployment steps or testing evidence.