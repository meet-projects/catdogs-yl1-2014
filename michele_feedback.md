Great job finishing your project. I hope you all are proud of what you accomplished, because it was a hard problem that was hard to solve. I have some feedback for you: 

* Your main code is in the `button.py` file instead of `main.py`, which is deceptive and not good coding practices. When I download all of your files and want to run your game, I naturally look for `main.py`. 
* The program window is too big - I can't play it on my laptop in the way you have it now (most screens don't fit more than 600 x 600 if you want it to be square). 
* Below the pictures of MALE / FEMALE and the two breeds of catdogs, it would have been nice to include a label saying what it is.
* The button class has no erase method, and it could have helped you a lot.
* The "clear window" function is a fantastic example of when and where to use a function. 
* In the `Label` class, the `orderlabel` and `label` variables should be made in the constructor - the reason is that they need to be created when you first create the label. 
* Fantastic use of if statements and functions - every statement had a purpose and every function had a purpose that was reusable.
* Small detail, but `Button` and `Label` classes should have been in separate files (and maybe even have been subclasses, since they share a lot of the same code)
* One clever way you could have used the `CatDog` classes more effectively was to encode a picture inside the `CatDog` class, so you don't need the large if statement at the end of your main loop to figure out which picture to draw at the end. This can be done with a system for naming files, etc.
* One code design suggestion: in general, it is better to create all the variables /  objects that you need inside your `main` method, then use those variables / objects in functions outside the `main` method. When you change the objects inside the functions, THEN you use the `global` keyword to change. This is where the classes become important, because when you create an object is not necessarily when you draw it on the screen, so you need to make sure that you have a separate DRAW method that can be called from a function that uses those objects you created in the `main` method.
* I think your group could have improved communication and separation of responsibilities between yourselves, maybe by having a meeting at the start of each session to figure out who is doing what. 
* The `Button` could have had a variable that is a function, which you can then set inside your `main` method, to do an action once a button is pressed using a common interface without the need for a complicated if statement and function logic.
* Ask yourselves: what did you do well in this project, what could you have done better as a group?
