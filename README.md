# Notes
#### Video Demo:  <URL https://drive.google.com/file/d/1nYDTrda-4XRGKjIhGdiWQTLE0o3dN3_f/view?usp=share_link>
#### Description:
For my final project I set out to create a webapp for keeping notes. My goals were to have a pretty, minimalistic design as to not overwhelm the user and to make the UI as intuitive as possible. I think I succeeded. Every little design choice, from the spacing between divs, to the color of certain elements was chosen to meet these goals.

##Login Page:
Because the webapp requires you to be logged in at all times, the first page a new user will likely see is the login page. There isn't much happening here: two input fields and a button, evenly spread apart. The input fields have placeholder text, therefor the user will always know which credentials to input. Now, because a new user doesn't have an account, there's a conveniently placed link placed underneath the login button, which will get the user to a registration page.

##Registration Page:
On the registration page there isn't much going on either. There's three input fields and a button. In the input fields there's conveniently placed placeholders so that, again, the user always knows what to input in which field. When pressing the Register button, the user will be taken to his Home Page.

##Home Page:
A new user will find himself in an empty Home Page after registering for his/her account. There's a plus icon in the top right corner of the screen, indicating the possibility to add something. Very intuitive. When clicking the plus icon, the user will see a pop-up appear. This pop-up contains a couple of input fields. Two text fields and a save button. The top input field had a placeholder which says "title". This slightly hints at the possibility that the title for the note he or she is about to create goes there. Under that, the user will find another text field. This has a placeholder which says "text". The text of your note goes there. When the user is satisfied with his note, he/she can press the save button to save the note. The newly created note will now appear on their Home Page.
In this newly created note, the user will see the title, text and an Edit button. By pressing the edit button the user will be taken to yet another popup in which he/she will again be prompted to change the title and text. The title and the text will already be present in the textboxes, so as to make editing the notes easier. Under these text fields there's a dropdown menu for advanced option: set reminder and print. These can be modified if more advanced options are needed further on. Under this menu is a "Save changes" button, self-explanatory. You may notice that for this amount of functionality, the UI isn't cramped at all.
On the footer of the home page are three links: Export notes, Import notes and Logout. The first two give the user the ability to download and upload their notes by clicking the links. The export button triggers a download of a csv file, which can later be uploaded through the upload function. The upload function takes the user to a page, prompting them to upload a csv file. When the file is submitted, the script checks for duplicate notes. duplicate ones will not be added to the database. The ones left will be added. The Logout link logs the user out and therefore reroutes them to the login page, because no content can be accessed without a login.

##And that's it!