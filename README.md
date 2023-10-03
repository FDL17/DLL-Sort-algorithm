# Sorting Algorithm DLL (Dynamic Link Library)

This repository contains a dynamic link library (.DLL) file that implements a sorting algorithm using the C programming language as its base.

STATUS REPOSITORY : On Going 

## Table of Contents
- [Author](#author)
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
## Author
Nickname : Sudo Coa

Github : FDL17

## Introduction

This project provides a reusable sorting algorithm in the form of a dynamic link library (.DLL). The sorting algorithm is implemented in C, making it efficient and versatile. You can easily integrate this library into your C/C++ projects to perform sorting operations on various data sets.

## Features

- Implements a versatile sorting algorithm in C.
- Provides a dynamic link library (.DLL) for easy integration into projects.
- Supports sorting of various data types.

## Usage

To use this sorting algorithm DLL in your project, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/FDL17/DLL-Sort-algorithm
    ```
2. Create your main program and import the DLL files into your program (using various programming languages' import methods). For Python examples:
   ```py

    from ctypes import *
    def sort_list(input_list):
        mydll = CDLL("./hasil/mys-sort.dll")
        mydll.run.argtypes = POINTER(c_double), c_int
        mydll.run.restype = None
        my_list = (c_double * len(input_list))(*input_list)
        length = len(my_list)
        mydll.run(my_list, length)
        return [my_list[i] for i in range(length)]
    input_list = [7,12,1,2,9.99,9.89,2,12,3,2]
    sorted_list = sort_list(input_list)
    for item in sorted_list:
        print(item)
   ```
3. Use ".run(list, length_of_list)" to Execute the Program
   ```bash
    function.run(list, length_of_list)
   ```
