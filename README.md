1. PREREQUISITES
    1.Basic knowledge of python(flask)
    2.Knowledge of HTML, and CSS.
    3.Already have python installed/downloaded.
    4.Text editor/ IDE

2. DOWNLOAD AND INSTALL DEPENDENCIES AND TOOLS
    1. XAMPP Server with MYSQL
    2. pymysql library - pip install PyMySQL 
    3. Flask - pip install flask 
    4. Flaskext - pip install Flask-MySQL

3. Create database table 
    CREATE TABLE `crud`.`accounts` (`id` INT(11) AUTO_INCREMENT , `username` VARCHAR(200) NOT NULL , `email` VARCHAR(200) NOT NULL , `password` VARCHAR(200) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

==============================================================================================================
==============================================================================================================
==============================================================================================================
==============================================================================================================

## **Libraries imported:**

Flask === We've imported the flask class here
render_template === to redirect to the template file defined in its argument after the successful execution of the function it was called in.
flaskext === to connect to MySQL database
pymysql === to perform SQL queries
session === a library that allows us to store data on the server


Initialization:
    mysql = MySQL()

Here we create an instance of the MySQL() library
    app=Flask(__name__,template_folder='templates')

This creates the flask app and tells it where our templates are
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_DB'] = 'crud'
        app.config['MYSQL_DATABASE_PASSWORD'] = ' '
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'







**_But no Mysql Libraries are working. Some missing points in versions of "flaskext"_**