# Strategy-Pattern-in-python
Strategy pattern in Python

Hi Folks,
This repository contains a concept of a low-level design pattern known as a Strategy Pattern .
I have implemented this in python 

How to read the code :
00. Example_code.py is the example code

01. code_modification.py
      1. Used inheritance here to solve the duplicate. But inheritance cannot solve this issue.

02. code_modification.py- some methods are added to the subclass
02. code_modification.md - understanding our code with matrix

03. code_modification.py- Added another attendant class . The job_title is also Station Attendant but this attendant makes "oil changes ".
03. code_modification.md - Showed how more methods and classes can be added and make the scene worse.

04. code_modification.py - Added another employee type that creates even more duplicate code
04. code_modification.md - With the help of a matrix, I tried to show how adding a lot of attributes can impact the code and how this can make the code grow exponentially.

05. strategy_pattern.py - Here we showed how strategy pattern really gives us the flexibility to combine algorithms at runtime. without adding any employee subclass, we can now create employee types at run-time.
05. strategy_pattern.md - Tried to show what is an algorithm in strategy pattern and how are we using it in a separate class.
