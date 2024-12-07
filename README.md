# Binary Parity Checker

A Python-based application to determine the parity (even or odd) of an 8-bit binary number. This project demonstrates proficiency in logical operations, robust error handling, and user-friendly design while adhering to high-quality coding standards.

---

## Overview

The Binary Parity Checker is a lightweight program written in Python that evaluates whether the number of `1` in an 8-bit binary number is even or odd. It incorporates logical operations for efficiency and offers detailed input validation to ensure reliability.

The project is designed to serve as an educational tool for understanding binary parity and logical XOR operations, while also demonstrating professional coding practices.

---

## Features

- **Robust Input Validation**: Ensures that only valid 8-bit binary numbers are processed.
- **Error Handling**: Provides clear and informative error messages for invalid inputs.
- **Efficient Algorithm**: Utilises the XOR operation for parity checking, a foundational concept in digital logic.
- **Extensibility**: Designed with scalability in mind, can be modified to handle binary numbers of any length.
- **Console Interface**: User-friendly and interactive command-line input/output.

---

## How It Works

The core logic of the program leverages the XOR operation, which is a standard method for determining the parity of binary data. The steps are as follows:
1. Each bit in the binary number is XORed sequentially.
2. The XOR operation inherently tracks the parity:
   - If the result is `0`, the number of `1`s is even.
   - If the result is `1`, the number of `1`s is odd.
3. The program outputs the corresponding parity ("Even" or "Odd").

### Key Formula
````
result = bit1 ^ bit2 ^ ... ^ bitN
