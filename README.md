# CiCo
## Link
<br/>
https://cico-web-app.herokuapp.com/%2F<br/>

## About
<br/>
CICO ( stands for Check-In Check-Out ) is a web application used for marking attendance. It has minimalistic design and hence provides a quick easy way to mark the check-in and check-out time , replacing the traditional register system.

## How to use ?
<br/>
1 - Go to the URL
<br/>
2 - If registered , click on Login else click on Sign up to register
<br/>
3 - After successful login , the Check page opens
<br/>
4 - Click on Check-in or Check-out accordingly

## Languages and Frameworks
Django<br/>HTML<br/>CSS<br/>Bootstrap<br/>SQLite

## Further Enhancements
- Adding more organizations<br/>
- GPS Location verification

## Documents

| Document         | Link                 | 
| -----------  | ---------------------- | 
| Software Requirements Specification  | [SRS](https://drive.google.com/file/d/1TeNqjpUORz8fvE4DMTLEZVHeQFoI6rwB/view?usp=sharing) |
| Essence Kernel and Additional Practices |  [Essence](https://drive.google.com/file/d/1kktzM5GDseAKeuHL-2CB4tFTMazaojzV/view?usp=sharing)     |
| Architecture and Design |  [ArchDes](https://drive.google.com/file/d/1znjxN_R-TDiUxYGU-3IrmNmJsXLD2cGX/view?usp=sharing)     |
| Test Cases | [Test](https://drive.google.com/file/d/1c3P_tRe-SFQMFD85RyJEgam0RZSe6sP_/view?usp=sharing)             |

## Instructions for setup.

1. Fork and clone this repository. Press the fork button on the top right of this page. Then on your console type `git clone https://github.com/<your-username>/CiCo`. Make sure to replace `<your-username>` with your github username.

2. Navigate to the project folder. Enter `cd CiCo` on your console to shift to the current project folder.

3. Setup the virtual environment.
   Use any virtual management tool, either `conda` or the `virtualenv` package. `virtualenv` is preffered for this project. To install `virtualenv` enter
   `pip install virtualenv` on your console.

   For linux/MacOS users, add sudo behind the command
   `sudo pip install virtualenv`

   **Note**: Use `pip3` instead of `pip` if you use pip3 to install packages for your python3 installation.

4. Create a new virtual environment. To create a new environment for this project, type `virtualenv CiCo` on your console. This will create a virtual environment in python to install all our dependencies.

   You can name your environment whatever you want. However to follow along with the steps and compatibility, the name "hostel-app" is preferred.

5. Activate the environment. To activate the environment, follow the instructions:

   On windows: `/CiCo/Scripts/activate`

   On Linux/MacOs: `source CiCo/bin/activate`

   If activation is successful, you will see `(CiCo)` as a prefix to every prompt in your console.

6. Install dependencies. Installing all the dependencies is quite simple, just type `pip install -r requirements.txt` on your console. It should install all the dependencies automatically for you. Repeat this step whenever a new dependency is added/removed.

   Linux/MacOS might use `sudo pip install -r requirements.txt`

Whenever you close the current terminal window, activate the virtual environment again by following step 5.

7. To run the server locally use:
                 `python manage.py migrate --run-syncdb`
                 `python manage.py makemigrations`
                 `python manage.py runserver`
                 
   Now open the link "http://127.0.0.1:8000/" (check if its the same link listed in your terminal) in your browser.
                 
   Note: Ensure your current directory has manage.py.
         Ensure django-allauth is installed.

               `python -m pip install django-allauth`

8. For Google-Auth:

   Create superuser to access admin panel.

            `python manage.py createsuperuser`

   You’re required to provide “username”, “email” and “password” in the terminal. Once you’re done, proceed to start the server:

            `python manage.py runserver`

   Go to (http://127.0.0.1:8000/admin) to access your admin page. Make sure you provide the credentials to login.

   ADD A SITE:

   On the SITES section, click “sites” and fill out the details and click “Save”:

   Domain name: 127.0.0.1:8000
   Display name: 127.0.0.1:8000
## Team
<br/>

[Ridhima Kohli](https://github.com/RidhimaKohli)
<br/>
<br/>
[Saptashrungi Birajdar](https://github.com/Saptashrungi)



