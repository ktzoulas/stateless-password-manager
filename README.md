# Stateless Password Manager

Generate strong and secure passwords that can be accessed anytime, anywhere. This app is not just a
common password manager; the generated passwords are not stored in the database.

### How it works

User creates password matrices containing the algorithm used to create the password, the number of
characters, if it is going to contain digits/symbols/uppercase or lowercase letters. Then, if the
users want to access their passwords, they must provide their secret key to create the password in
real-time based on the password matrices that they have already created.

Users can use the same secret key for all their passwords, as the generated password will be different
for each matrix, because in every matrix it is stored a salt that makes the search space larger in
the case of brute forcing. Moreover, salt makes the generated password unique.

### Remember one secret key to access all your passwords, anytime and anywhere

![One to rule them all](project/static/images/lordoftherings.jpg)
