This is my Introduction to Programmming final term project from the Spring 2015 semester at Carnegie Mellon University.

Overall, this project is a proof of concept for an authentication system which allows entry based on the rhythm and gait with which a user enters their password. This was inspired from Professor Roy Maxion's existing research. No code was taken from Professor Maxion's existing research, but the idea for creating this proof of concept for an introductory term project was from his existing proof of concepts. Find more at https://www.cs.cmu.edu/~maxion/pubs/KillourhyMaxion09.pdf

The project has three modules:
The first module will collect 50 examples of a user inputting one password. It will take timing data points from the entry of each of those attempts and create one data file. Every time a user elects to enter more password attempts, it will add to that file.

The second module allows any user to enter the common password and run a k-nearest-neighbor algorithm on the existing data to attempt to match the user with an existing profile based on password-entry gait.

The third module allows you to look at all existing users, select one, and view all their data points. Clicking on one data point will align all other common data points to view relative trends from one data point to the next.
