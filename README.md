# bookStoreApp
book management system.

Contributors: Dinusa

==Technology used for development===
Python 3.9.4
django 3.2
Firestore for store images
Database = SQLITE

== Description ==

storeapp is for book stores which customers can view books in the store and book store admins can view, edit and delete books. 
Also book store admin can view, add, edit and delete the users.Customers can register with book store app and search books. 
Also they can view their profile and edit the profile.

Major features include:

* Admin can add, view, edit, and delete users and books.
* Customers can register and view books of the store.
* Automatically check the registers customer whether adults or child by their birthday and filter the books for children.
* Every user can search books by using searching bar.
* Books filter as user type of the customer. If the user is a child, system will show only children's books and adults can view any kind of books.


===Prerequisites===
Have to install python3, pip3 and django3 on to the machine.

If not installed above 
* Download Python Executable Installer
* Run Executable Installer
* Verify Python3 has installed on your machine by run following comand on your comand prompt(cmd)
        # python
* Verify pip3 has installed on your machine
        # pip3 -V
        
        if not installed
          * $sudo apt install python3-pip
*Verify django has installed on your machine
        #python -m django --version 
        
        if not
        # pip3 install django

==Run the project==
* After checkout the project from git hub or copy the project folder to the machine, use your cmd and go to project location.(go to storeapp directory)
  eg: cd user/abc/project/bookStoreApp/storeapp
* And then you can create super user by run following comand on your cmd
      #python manage.py createsuperuser
      
      or I have already created a superuser and following are the username and password
          username :- manez
          passwaord :- manez@123
* Then run following commands to migrate database changes and to install firebase.
    #pip3 install pyrebase
    #pip3 install google.cloud
    #python manage.py makemigrations
    #python manage.py migrate
    
* Finally run the server
    #python manage.py runserver
    
* After run the server it will show you the server address and you can run it on your browser
 #eg :- Starting development server at http://127.0.0.1:8000/ , so you can copy paste "http://127.0.0.1:8000/" on your browser.
 
 
 
 





