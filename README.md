# random-password
This is a pseudo random password generator.

## Download, Install, and Use
1. Download from this project's repository
2. Install:
    - Install using pip:
    ```
       pip install <path-to-downloaded-project> 
    ```
    - or Install using python setup install:
    ```
       cd <path-to-downloaded-project>
       python -m setup install
    ```
3. Use the Module using:
```
   import password
```


## Instructions
Import the module and use the function 'generate_random_password'
Options for generating the password:
- length (int)
    - Character length of the password
- uppercase (boolean)
    - Whether to use uppercase letters (A-Z)
- lowercase (boolean)
    - Whether to use lowercase letters (a-z)
- numbers (boolean)
    - Whether to use digits (0-9)
- symbols (boolean)
    - Whether to use symbols contained in python's string.symbols
- save_preference (boolean)
    - Whether to save the above preferences (such as if generating multiple passwords)
```
    from password import generate_random_password as genpass
    pw = genpass(length=20, 
                 uppercase=True, 
                 lowercase=True, 
                 numbers=True, 
                 symbols=False)
```
