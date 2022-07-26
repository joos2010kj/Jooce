# jooce

Ever felt tired of reusing the same, tedious code over and over again? Well, at least I did run into this a lot while working on research projects! 

For example, I was tired of re-writing the same code for:
- Reading / Writing files
- Crawling across the directory files, in certain specific pattern
- Writing the same mathematical expressions in NumPy / PyTorch code for different projects

Therefore, I decided to create some Juuuuicy program that allows you to *save* your own code and reuse it very easily in an import style.
I also included compartmentalization to let you organize functions based on projects.

You can always easily remove and add new functions and compartments, so why not try using this!

---

## How to Use

Jooce has the following static methods usable at class-level:
- state()
  - Use this to see what project's configuration you are using, and the methods you have stored in the project.

- list()
  - Lists out all the projects you have created.

- create_storage(name)
  - Create a new project config.

- select(name)
  - Set the current project to *name*.  You do not need to run *select* each time you start a new code. 
  Whichever you picked last by running *select* will be maintained until it is run again.

- remove_storage(name)
  - Discard one project config

- save(function)
  - Save one function under the current project config

- remove_function(function_name)
  - Remove one function from the current project config

- transcribe()
  - Transcribe the saved config into a runnable python code.  Make sure to run this after running *save*!
  
---

## Sample Runs

### File1.py:
```
from jooce import Jooce

Jooce.create_storage("temp")
Jooce.select("temp")

def openfile(f):
    from pathlib import Path

    with Path(f).open("r") as fp:
        return fp.readlines()

Jooce.save(openfile, transcribe=False)

def writefile(f, content):
    from pathlib import Path

    with Path(f).open("w") as fp:
        fp.writelines(content)

Jooce.save(openfile, transcribe=False)

Jooce.transcribe()
```


### File2.py:
```
from jooce import temp

res = utils.openfile("hello.txt")
print(res)
```
