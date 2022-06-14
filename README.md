## About The Project

- 2022 Complete Python Bootcamp From Zero to Hero in Python
- Learn Python like a Professional Start from the basics and go all the way to creating your own applications and games
- [Original Repo: Complete-Python-3-Bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)
- [Pierian Data](https://github.com/Pierian-Data)

&nbsp;

---

&nbsp;

## Basics

|      Name      | Type  |                          Description                          |
| :------------: | :---: | :-----------------------------------------------------------: |
|    Integers    |  int  |                         Whole number                          |
| Floating Point | float |                        Decimal number                         |
|    Strings     |  str  |                             words                             |
|     Lists      | list  |       Ordered sequence of objects: [10, "hello", 200.3]       |
|  Dictionaries  | dict  | Unordered Key value pair: {"key": "value", "name:": "Python"} |
|     Tuples     |  tup  |  Ordered immutable sequence of objects: (10, "hello", 200.3)  |
|      Sets      |  set  |      Unordered collection of unique objects: {"a": "b"}       |
|    Booleans    | bool  |                         True or False                         |

- Rules for variable names
  1. Names can not start with a number.
  2. There can be no spaces in the name, use \_ instead.
  3. Can't use any of these symbols :'",<>/?|\()!@#$%^&\*~-+
  4. It's considered best practice [PEP8](https://peps.python.org/pep-0008/) that names are lowercase.
  5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
  6. Avoid using words that have special meaning in Python like "list" and "str"
- Dynamic type
- [pyformat](https://pyformat.info/)
- [input & output of files](https://docs.python.org/3/tutorial/inputoutput.html)
- [Mkyong - Python difference between r+, w+ and a+ in open()](https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/)

| Mode |                  Description                  |
| :--: | :-------------------------------------------: |
|  r   |                   read only                   |
|  w   |     write only (overwrite or create new)      |
|  a   |                  append only                  |
|  r+  |              reading and writing              |
|  w+  | writing and reading (overwrite or create new) |

- Functions & Methods
  - \*args & \*\*kwargs
  - Lambada anonymous function
  - Scope

|     |           LEGB            |                                                                                                        |
| :-: | :-----------------------: | ------------------------------------------------------------------------------------------------------ |
|  L  |           Local           | Names assigned in any way within a function (def or lambda), and not declared global in that function. |
|  E  | Enclosing function locals | Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.      |
|  G  |      Global (module)      | Names assigned at the top-level of a module file, or declared global in a def within the file.         |
|  B  |     Built-in (Python)     | Names preassigned in the built-in names module : open, range, SyntaxError,...                          |

- Object Oriented Programming (OOP)
  - Class & Attributes
  - Inheritance & Polymorphism
- <b>Modules</b> are just .py scripts that you call in another .py script
- <b>Packages</b> are a collection of modules.
- <code>\_\_name\_\_</code> == <code>'\_\_main\_\_'</code>

&nbsp;

---

&nbsp;

> Sometimes when you are importing from a module, you would like to know whether a modules function is being used as an import, or if you are using the original.py file of that module. In this case we can use the:

```py
if __name__ == "__main__":
```

> line to determine this. For example:
>
> When your script is run by passing it as a command to the Python interpreter:

```sh
python myscript.py
```

> all of the code that is at indentation level 0 gets executed. Functions and classes that are defined are, well, defined, but none of their code gets ran. Unlike other languages, there's no main() function that gets run automatically - the main() function is implicitly all the code at the top level.

> In this case, the top-level code is an if block. <code>\_\_name\_\_</code> is a built-in variable which evaluate to the name of the current module. However, if a module is being run directly (as in myscript.py above), then <code>\_\_name\_\_</code> instead is set to the string <code>'\_\_main\_\_'</code>. Thus, you can test whether your script is being run directly or being imported by something else by testing

```py
if __name__ == "__main__":
    ...
```

> If that code is being imported into another module, the various function and class definitions will be imported, but the main() code won't get run. As a basic example, consider the following two scripts:

```py
# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

and then:

# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
```

Now, if you invoke the interpreter as

```sh
python one.py
```

The output will be

```sh
top-level in one.py
```

one.py is being run directly
If you run two.py instead:

```sh
python two.py
```

You get

```sh
top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly
```

> Thus, when module one gets loaded, its <code>\_\_name\_\_</code> equals "one" instead of <code>\_\_main\_\_</code>.

&nbsp;

---

&nbsp;

> <b>Samil: </b>Purpose of <code>\_\_name\_\_</code> == <code>'\_\_main\_\_'</code>
>
> Basically you are splitting your .py scripts into two sections: i) function, class and object definitions, ii) running a series of functions and methods.
>
> Your anticipation is that if you are running the script x directly, you want to execute the functions but if you are just importing the script x, you are only interested in importing the definitions segment from script x to use with function execution in script y.

&nbsp;

---

&nbsp;

## Errors & Exceptions

- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

```sh
pylint pylint_test.py -r y
```

&nbsp;

---

&nbsp;
