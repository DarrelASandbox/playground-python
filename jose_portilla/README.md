<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#basics">Basics</a></li>
    <li><a href="#errors--exceptions">Errors & Exceptions</a></li>
    <li><a href="#decorators--generators">Decorators & Generators</a></li>
    <li><a href="#advance-python-modules">Advance Python Modules</a></li>
      <ol>
        <li><a href="#collections">Collections</a></li>
        <li><a href="#opening-and-reading-files-folders">Opening and Reading Files Folders</a></li>
        <li><a href="#datetime">Datetime</a></li>
        <li><a href="#python-debugger">Python Debugger</a></li>
        <li><a href="#overview-of-regular-expressions">Overview of Regular Expressions</a></li>
        <li><a href="#timing-your-code---timeit">Timing your code - timeit</a></li>
        <li><a href="#unzipping-and-zipping-files">Unzipping and Zipping Files</a></li>
      </ol>
    </li>
    <li><a href="#web-scraping">Web Scraping</a></li>
  </ol>
</details>

&nbsp;

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

## Decorators & Generators

- Decorators can be thought of as functions which modify the functionality of another function. They help to make your code shorter and more "Pythonic".
  - Scenario: Imagine you have a simple function and you want to add more functionality to it
    - Option 1: Add that extra code to your old function
    - Option 2: Create a brand new function that contains the old code, and then add new code to that
  - But what if you then want to remove that extra functionality?
    - You would need to delete it manually, or make sure to have the old function

```py
@some_decorator
def simple_func():
    # Do simple stuff
    return something
```

- Generators allow us to write a function that can send back a value and then later resume to pick up where it left off.
- Allows us to generate a sequence of values over time.
- The main difference in syntax will be the use of a [yield](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do) statement.
- When a generator is complied they become an object that supports an iteration protocol.
- That means when they are called in your code they don't actually return a value and then exit.
- Generator will automatically suspend and resume their execution and state around the last point of value generation.
- The main advantage here is that instead of having to compute an entire series of values up front, the generator computes one value and then suspends its activity awaiting the next instruction. This feature is known as state suspension.
- Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time.
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [How exactly does a generator comprehension work?](https://stackoverflow.com/questions/364802/how-exactly-does-a-generator-comprehension-work)

&nbsp;

---

&nbsp;

## Advance Python Modules

### Collections

```py
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
```

### Opening and Reading Files Folders

- Open files programatically
- <code>os.unlink(path)</code> which deletes a file at the path provided
- <code>os.rmdir(path)</code> which deletes a folder (folder must be empty) at the path provided
- <code>shutil.rmtree(path)</code> this is the most dangerous, as it will remove all files and folders contained in the path. All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.

### Datetime

- Time values are represented with the time class. Times have attributes for hour, minute, second, and microsecond. They can also include time zone information.

### Math and Random

- [numpy](https://numpy.org/)
- [Python 3.x rounding behavior](https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior)

### Python Debugger

- The pdb module implements an interactive debugging environment for Python programs. It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.

### Overview of Regular Expressions

- Regular expressions have to be able to filter out any string pattern you can imagine, which is why they have a complex string pattern format.

| Character |   Description    | Pattern Code |  Match  |
| :-------: | :--------------: | :----------: | :-----: |
|    \d     |     A digit      |  file\_\d\d  | file_25 |
|    \w     |   Alphanumeric   |  \w-\w\w\w   |  A-b_1  |
|    \s     |   White space    |   a\sb\sc    |  a b c  |
|    \D     |   A non digit    |    \D\D\D    |   ABC   |
|    \W     | Non-alphanumeric |  \W\W\W\W\W  | \*-+=)  |
|    \S     |  Non-whitespace  |   \S\S\S\S   |  Yoyo   |

| Character |        Description        |  Pattern Code  |     Match      |
| :-------: | :-----------------------: | :------------: | :------------: |
|     +     | Occurs one or more times  | Version \w-\w+ | Version A-b1_1 |
|    {3}    |  Occurs exactly 3 times   |     \D{3}      |      abc       |
|   {2,4}   |    Occurs 2 to 4 times    |    \d{2,4}     |      123       |
|   {3,}    |     Occurs 3 or more      |     \w{3,}     | anycharacters  |
|    \*     | Occurs zero or more times |   A\*B\*C\*    |     AAACC      |
|     ?     |       Once or none        |    plurals?    |     plural     |

### Timing your code - timeit

- Python has a built-in timing modules (time & timeit) to do this.

### Unzipping and Zipping Files

- zipfile library
- shutil library

&nbsp;

---

&nbsp;

## Web Scraping

- Rules:
  1. Always be respectful and try to get premission to scrape, do not bombard a website with scraping requests, otherwise your IP address may be blocked!
  2. Be aware that websites change often, meaning your code could go from working to totally broken from one day to the next.
  3. Pretty much every web scraping project of interest is a unique and custom job, so try your best to generalize the skills learned here.
- Limitations:
  - In general every website is unique, which means every web scraping script is unique
  - A slight change or update to a website may completely break your script

| Syntax to pass to the .select() method |                                                                   Match Results                                                                   |
| :------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------: |
|           soup.select('div')           |                                                All elements with the <code>&lt;div&gt;</code> tag                                                 |
|        soup.select('#some_id')         |                                 The HTML element containing the <code>id</code> attribute of <code>some_id</code>                                 |
|         soup.select('.notice')         |                                        All the HTML elements with the CSS <code>class</code> named notice                                         |
|        soup.select('div span')         |                      Any elements named <code>&lt;span&gt;</code> that are within an element named <code>&lt;div&gt; </code>                      |
|       soup.select('div > span')        | Any elements named <code>&lt;span&gt;</code> that are directly within an element named <code>&lt;div&gt;</code>, with no other element in between |

&nbsp;

---

&nbsp;
