# ShowerThoughts
A Q&amp;A app where users can create an account, ask questions, receive answers and more.

made with Django rest framework and Vuejs/Tailwind.

## Main features

### Questions 
- Write
- Update
- Delete 

### Answers 
- Write
- Update
- Delete
- Like/Unlike

### Users
- Create account
- Login
- Logout

### Security
- Token Authentication
- Session Authentication


## How to run the app
- Fork or download the app.

- Install python.

- Open the project via cli and create a virtual enviroment `py -m venv /name of the venv folder i call it venv`.

- Activate the venv `venv\Scripts\activate.bat`.

- Install Django/DRF and other requirments by running `py -m pip install Django djangorestframework dotenv`.

- Download Node.js.

- Install vue `npm install -g @vue/cli`.

- Install Tailwind and other requirments `npm install -D tailwindcss@npm:@tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9`.

- Run the venv then open the qq folder inside the terminal run python server by typing `py manage.py runserver`.

- Run vue by opening the frontend folder inside of the terminal and running `npm run serve`.

- open the project in the localhost.

## Currently disabled

for the time being there are 2 main features that the design for is not finished but can be found in the Api which are the Categories and the User questions and answers queryset, will be implemented in future updates.

## Future updates

- redesign the site.
- Add categories.
- Add a user profile/page.
- Add search functionality.
