"""
With a minimal example under our belt, we can start to explore why cred’s flexibility
makes it so powerful. First, what if instead of using the toy in-memory checker we
wanted to check the username and password against a file-based username and pass‐
word database?
Twisted comes with a FilePasswordDB checker, so all we have to do is create a credentials
file containing some usernames and passwords and swap in this FilePasswordDB
checker:
-checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
-checker.addUser("user", "pass")
+checker = checkers.FilePasswordDB("passwords.txt")
FilePasswordDB ’s line format is customizable and defaults to username:password . Try
running echo_cred.py with these changes and a test passwords.txt.
What if we wanted to use hashed passwords in our password file instead?
FilePasswordDB takes an optional hash argument that it will apply to a password before
comparing it to the hash stored on disk. To augment Example 9-1 to support hashed
passwords, swap in:


import hashlib
def hash(username, password, passwordHash):
    return hashlib.md5(password).hexdigest()

realm = Realm()
myPortal = portal.Portal(realm)
checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("user", "pass")
checker = checkers.FilePasswordDB("passwords.txt", hash=hash)

"""