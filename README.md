# pyc++-compiler
This Python program, titled pyc++.py, automates the process of compiling and running C++ programs. It utilizes the Microsoft Visual Studio C++ compiler (cl.exe) to compile the provided C++ source code as an argument. After successful compilation, the program also executes the generated executable file.


Requirements:
Python: The program requires the installation of Python to run.

C++ Compiler: The Microsoft Visual Studio C++ compiler (cl.exe) must be installed on the system. Make sure to provide the correct path to the VsDevCmd.bat file in the script.

Usage:
The script can be executed from the command line with the following command:
                     python pyc++.py file_name.cpp
Where file_name.cpp is the name of the C++ file you want to compile and run.

Operation:
1-The script checks if the provided number of arguments is correct. Otherwise, it displays an error message and exits.
2-Determines the current directory and the name of the C++ file provided as an argument.
3-Generates the name of the executable file to be created by replacing the .cpp extension with .exe.
4-Sets the path to the VsDevCmd.bat file used to configure the Visual Studio C++ development environment.
5-Builds the complete command to open the development prompt and compile the C++ file.
6-Executes the compilation command and checks if the compilation was successful.
7-If the compilation was successful, displays the corresponding message and runs the generated executable file.
8-If the execution of the generated file is successful, displays a success message; otherwise, displays an error message.


Notes
Make sure to adjust the path to the VsDevCmd.bat file according to the installation of Visual Studio C++ on your system. The program currently assumes the default installation.

Author: Obentemiller

GitHub Repository: pyc++
obrigado.


