# README.md for ~/GitHub/FletX

This project repo was built following the guidance provided in https://alldotpy.github.io/FletX/getting-started/installation/#option-1-manual-setup.  It works!  

The specific command sequence used here was...

```
mkdir FletX
cd FletX
code .                        <-- moved focus into VSCode where commands continue
python3.12 -m venv .venv
source .venv/bin/activate
pip install flet fletxr 
flet run main.py 
```

## building-reactive-lists.py

The `building-reactive-lists.py` code was built directly from https://medium.com/@einswilligoeh/tutorial-building-reactive-lists-with-fletx-9722c8f9d65d.  Note that the code runs, but the application window is unresponsive.   

## flet-counter-app.py

The `flet-counter-app.py` code was built directly from https://medium.com/@einswilligoeh/fletx-bring-reactive-power-to-your-python-ui-with-getx-like-simplicity-61d186ebc58a.  Note that the code runs AND appears to behave as-intended.    

## minimal-architecture-example

From https://alldotpy.github.io/FletX/getting-started/architecture/#minimal-architecture-example...  but it throws an error:  

```
Traceback (most recent call last):
  File "/Users/mcfatem/GitHub/FletX/minimal-architecture-example/main.py", line 5, in <module>
    from .pages.counter import CounterPage
ImportError: attempted relative import with no known parent package
```

The above error was fixed by removing the "." from the front of all relative path import statements, making them absolute.   

