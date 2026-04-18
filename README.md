# Shoe Inventory Management System

This repository contains a Python program developed as part of a boot camp task to practice object‑oriented programming, file handling, error trapping, and menu‑driven application design.  
The system manages a shoe inventory stored in `inventory.txt` and allows the user to perform various operations such as searching, restocking, viewing all items, and calculating stock value.
AUTHOR
Derek Smith
derek@deeztec.com
---

## 📦 Project Overview

The program uses a `Shoe` class to represent each item in the inventory and provides a set of functions to:

- Read shoe data from a text file  
- Add new shoes to the inventory  
- Display all shoes in a formatted table  
- Search for a shoe by product code  
- Restock the shoe with the lowest quantity  
- Calculate the total value per item  
- Identify the shoe with the highest quantity  
- Update the inventory file after changes  

The system runs through a simple menu interface, making it easy to interact with the inventory.

---

## 🧰 Features

- **Object‑Oriented Design**  
  Uses a `Shoe` class with attributes such as country, code, product, cost, and quantity.

- **File Handling**  
  Reads and writes to `inventory.txt` with error trapping for missing or malformed files.

- **User Input Validation**  
  Ensures clean, safe input for new shoe entries.

- **Menu‑Driven Interface**  
  Allows users to choose actions repeatedly until they exit.

- **Automatic Inventory Updates**  
  After restocking or adding items, the file is rewritten to keep data consistent.

---

## 📁 File Structure
example-repo/
│
├── inventory.txt        # Data file containing shoe inventory
├── shoe_inventory.py    # Main program file
└── README.md            # Project documentation

