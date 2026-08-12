![Daffodil International University](data:image/png;base64...)ffProject Report

**Medical Store Management System**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Only for course Teacher** | | | | | | |
|  | | **Needs Improvement** | **Developing** | **Sufficient** | **Above Average** | **Total Mark** |
| **Allocate mark & Percentage** | | **25%** | **50%** | **75%** | **100%** | **15** |
| **Understanding / Analysis** | **4** |  |  |  |  |  |
| **Implementation** | **5** |  |  |  |  |  |
| **Report Writing** | **6** |  |  |  |  |  |
| **Total obtained mark** | | | | | |  |
| **Comments** |  | | | | | |

**Semester: Spring 2025 Group No:- 4**

**Name: Nahid Ibn Zaman ID: 252-35-571**

**Name: Mahmuda Khanum ID: 252-35-537**

**Name: Farhan Ishraq Ifti ID: 252-35-648**

**Batch: 45 Section: F1 Course Code: SE 133**

**Course Name: Software Development Capstone Project**

**Course Teacher Name: Syeda Sumaia Sultana Designation: Lecturer**

**Submission Date: 08/03/26**

# Table of Contents

· **Introduction** (p.3)

* 1.1 Purpose
* 1.2 Scope
* 1.3 Project Overview
* 1.4 Intended Audience

· **Functional Requirements** (p.3)

* 2.1 Admin Module
* 2.2 Customer Module
* 2.3 Data Persistence (File Handling)

· **Non-Functional Requirements** (p.4)

· **Use Case Diagram** (p.5)

· **Activity Diagram** (p.6)

# 1. Introduction

## 1.1 Purpose

The purpose of this document is to present the final individual project report for the Medical Store Management System. It describes the functional and non-functional requirements, the system design, the implementation details of the C source code, and the testing carried out to verify the system behaves as intended. This report serves as a record of the work completed and the understanding gained while building the project.

## 1.2 Scope

The Medical Store Management System is a console-based application developed in the C programming language, intended to digitize the day-to-day operations of a local pharmacy. The system is divided into two primary modules: an Admin Panel used by pharmacy staff to manage medicine records, and a Customer Panel used by customers to browse medicines, build a purchase cart, and complete checkout. The system uses structures to model data, pointers for efficient data handling, and binary file handling to persistently store medicine inventory and transaction records between sessions.

## 1.3 Project Overview

Each medicine record consists of an ID, name, category, price, quantity, and expiry date, stored using a C structure. Administrative users can insert, update, delete, and search medicine records, as well as monitor near-expiry and already-expired stock. Customers can search available medicines, add items to a shopping cart, view the cart, and check out. During checkout, the system automatically calculates the subtotal, applies a fixed tax rate, deducts the purchased quantity from the stored inventory file, generates an invoice, and logs the transaction — all performed through direct binary file read, write, and seek operations.

## 1.4 Intended Audience

* Course Instructor — for evaluation of the individual project.
* Developer (myself) — as a reference for the implementation decisions made.
* End Users (hypothetical) — pharmacy admin staff and customers, as modelled by the system.

# 2. Requirement Analysis

This section documents the functional and non-functional requirements that the system was built to satisfy, forming the basis of the Understanding/Analysis component of this report.

## 2.1 Functional Requirements — Admin Module

| **ID** | **Requirement Description** |
| --- | --- |
| **FR-01** | The system shall allow the admin to add a new medicine record (ID, name, category, price, quantity, expiry date) to the inventory file. |
| **FR-02** | The system shall allow the admin to view the complete list of all medicines currently stored in the file. |
| **FR-03** | The system shall allow the admin to update the details of an existing medicine record by its ID. |
| **FR-04** | The system shall allow the admin to delete a medicine record from the inventory by its ID. |
| **FR-05** | The system shall allow the admin to search for a medicine by ID or by name. |
| **FR-06** | The system shall allow the admin to view medicines that are nearing expiry (within 30 days) or already expired, and to bulk-delete expired stock. |

## 2.2 Functional Requirements — Customer Module

| **ID** | **Requirement Description** |
| --- | --- |
| **FR-07** | The system shall allow the customer to browse the list of available medicines. |
| **FR-08** | The system shall allow the customer to search for a specific medicine by ID or name. |
| **FR-09** | The system shall allow the customer to add a selected medicine and quantity to a shopping cart, provided sufficient stock exists and the medicine has not expired. |
| **FR-10** | The system shall allow the customer to view the current cart contents and subtotal. |
| **FR-11** | The system shall calculate the total payable amount, including a fixed-rate tax, at checkout. |
| **FR-12** | The system shall deduct the purchased quantity from the stored inventory file upon successful checkout. |
| **FR-13** | The system shall generate an invoice and log the completed transaction to a file. |

## 2.3 Data Persistence (File Handling)

* All medicine records are stored in a binary file (medicines.dat) using C structures.
* Every completed transaction is logged to a separate text file (transactions.txt).
* Update operations use fseek() to modify a record in place without rewriting the entire file.
* Delete operations reconstruct the file by omitting the target record(s).

## 2.4 Non-Functional Requirements

| **Category** | **Requirement** |
| --- | --- |
| **Performance** | All CRUD operations and search queries complete instantly for a store-scale inventory, as records are accessed via direct binary file offsets. |
| **Reliability** | The system does not corrupt existing records if an operation is interrupted; update/delete operations use safe file-rewrite techniques. |
| **Usability** | The system provides a clear, menu-driven text interface so that both admin staff and customers can operate it without technical training. |
| **Security** | Only the Admin Panel is permitted to add, update, or delete inventory records; customers can only read and purchase. |
| **Maintainability** | The source code is modular, with separate functions for each CRUD operation, to support easy future modification. |
| **Portability** | The system is written in standard C and compiles and runs on any platform with a standard C compiler (e.g., GCC). |

# 3. System Design

## 3.1 Use Case Diagram

The diagram below illustrates the two actors of the system — Admin and Customer — and the primary use cases each actor performs within the Medical Store Management System.

![](data:image/png;base64...)

*Figure 1: Use Case Diagram — Medical Store Management System*

## 3.2 Activity Diagram

The diagram below models the workflow of a customer purchase, from browsing medicines through to checkout, including the stock-validation decision point and the file updates that occur after payment.

![](data:image/png;base64...)

*Figure 2: Activity Diagram — Customer Checkout Process*

## 3.3 Data Structures Used

Two C structures form the backbone of the system:

|  |
| --- |
| typedef struct {  int id;  char name[50];  char category[30];  float price;  int quantity;  char expiry\_date[11]; // format: YYYY-MM-DD  } Medicine;    typedef struct {  int id;  char name[50];  float price;  int qty;  } CartItem; |

The Medicine structure represents one inventory record and is written directly to and read directly from medicines.dat using fwrite()/fread(), which is why the file is opened in binary mode. The CartItem structure exists only in memory (in a fixed-size array, cart[MAX\_CART]) and represents one line of the customer's current shopping cart before checkout.

# 4. Implementation

## 4.1 Tools & Technologies

* Language: C (ISO C, compiled with GCC)
* Data storage: binary file I/O (fopen, fread, fwrite, fseek) for medicines.dat, and text file logging for transactions.txt
* Core techniques: structures, pointers, file offsets/seeking, and modular function design

## 4.2 Module Description & Source Code

The program is organized into small, single-purpose functions grouped by responsibility: utility/lookup functions, admin CRUD operations, expiry management, and customer/cart operations. Each function below is shown with a short explanation followed by the relevant source code.

### Header Files, Macros & Data Structures

*Defines the file names used for persistent storage, the tax rate, cart capacity, and the near-expiry threshold. The Medicine structure models one inventory record, and CartItem models one line item in a customer's shopping cart.*

|  |
| --- |
| #include <stdio.h>  #include <stdlib.h>  #include <string.h>  #include <time.h>    #define MED\_FILE "medicines.dat"  #define TXN\_FILE "transactions.txt"  #define TAX\_RATE 0.05 /\* 5% tax \*/  #define MAX\_CART 50  #define NEAR\_EXPIRY\_DAYS 30 /\* medicines expiring within this many days are "near expiry" \*/    // DATA STRUCTURES    typedef struct {  int id;  char name[50];  char category[30];  float price;  int quantity;  char expiry\_date[11]; // format: YYYY-MM-DD  } Medicine;    typedef struct {  int id;  char name[50];  float price;  int qty;  } CartItem; |

### getNextID() — Auto-incrementing ID Generator

*Scans the entire medicines.dat file to find the highest existing ID and returns the next available one, so every new medicine batch gets a unique ID automatically.*

|  |
| --- |
| int getNextID() {  FILE \*fp = fopen(MED\_FILE, "rb");  Medicine m;  int maxId = 0;  if (fp == NULL) return 1;  while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  if (m.id > maxId) maxId = m.id;  }  fclose(fp);  return maxId + 1;  } |

### findMedicineByID() — Locate a Record by ID

*Performs a linear scan of the binary file and returns the byte offset of the matching record (or -1 if not found). This offset is later used with fseek() so update operations can overwrite the record in place without rewriting the whole file.*

|  |
| --- |
| long findMedicineByID(int id, Medicine \*m) {  FILE \*fp = fopen(MED\_FILE, "rb");  long pos = 0;  if (fp == NULL) return -1;    while (fread(m, sizeof(Medicine), 1, fp) == 1) {  if (m->id == id) {  fclose(fp);  return pos;  }  pos += sizeof(Medicine);  }  fclose(fp);  return -1;  } |

### daysUntil() — Expiry Date Calculation

*Parses a YYYY-MM-DD string into a struct tm, converts both the expiry date and today's date to time\_t, and returns the difference in whole days. A negative result means the medicine has already expired.*

|  |
| --- |
| int daysUntil(const char \*dateStr) {  struct tm expiry = {0};  time\_t now = time(NULL);  struct tm today = \*localtime(&now);    sscanf(dateStr, "%d-%d-%d", &expiry.tm\_year, &expiry.tm\_mon, &expiry.tm\_mday);  expiry.tm\_year -= 1900;  expiry.tm\_mon -= 1;    // normalize "today" to midnight so we compare whole days only  today.tm\_hour = 0; today.tm\_min = 0; today.tm\_sec = 0;    time\_t t1 = mktime(&expiry);  time\_t t2 = mktime(&today);    return (int)(difftime(t1, t2) / (60 \* 60 \* 24));  } |

### addMedicine() — Create (Admin)

*Opens medicines.dat in append-binary mode, assigns the next ID via getNextID(), prompts the admin for the medicine's details, and writes the completed Medicine struct to the end of the file with a single fwrite() call.*

|  |
| --- |
| void addMedicine() {  Medicine m;  FILE \*fp = fopen(MED\_FILE, "ab"); // append binary  if (fp == NULL) {  printf("Error opening file.\n");  return;  }    m.id = getNextID();  printf("\n--- Add New Medicine Batch (ID: %d) ---\n", m.id);    printf("Medicine Name : ");  scanf(" %49[^\n]", m.name);  printf("Category : ");  scanf(" %29[^\n]", m.category);  printf("Price : ");  scanf("%f", &m.price);  printf("Quantity : ");  scanf("%d", &m.quantity);  printf("Expiry Date(YYYY-MM-DD): ");  scanf(" %10[^\n]", m.expiry\_date);    fwrite(&m, sizeof(Medicine), 1, fp);  fclose(fp);    printf("\nMedicine batch added successfully!\n");  } |

### viewMedicines() — Read All Records (Admin & Customer)

*Reads the file from the beginning to the end, one Medicine struct at a time, and prints a formatted table of every record currently in stock. Used by both the Admin and Customer panels.*

|  |
| --- |
| void viewMedicines() {  Medicine m;  FILE \*fp = fopen(MED\_FILE, "rb");  int found = 0;    if (fp == NULL) {  printf("\nNo records found. (File does not exist yet)\n");  return;  }    printf("\n%-5s %-20s %-15s %-10s %-10s %-12s\n", "ID", "Name", "Category", "Price", "Quantity", "Expiry");  printf("----------------------------------------------------------------------------\n");    while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  printf("%-5d %-20s %-15s %-10.2f %-10d %-12s\n", m.id, m.name, m.category, m.price, m.quantity, m.expiry\_date);  found = 1;  }  fclose(fp);    if (!found) printf("No medicines available in the store.\n");  } |

### updateMedicine() — Update (Admin)

*Looks up the record by ID using findMedicineByID() to get its file offset, displays the current values, collects new values from the admin, then reopens the file in read/write binary mode (r+b) and uses fseek() to overwrite only that record in place.*

|  |
| --- |
| void updateMedicine() {  Medicine m;  int id;  long pos;    printf("\nEnter Medicine ID to update: ");  scanf("%d", &id);    pos = findMedicineByID(id, &m);  if (pos == -1) {  printf("Medicine with ID %d not found.\n", id);  return;  }    printf("Current details -> Name: %s | Category: %s | Price: %.2f | Qty: %d | Expiry: %s\n",  m.name, m.category, m.price, m.quantity, m.expiry\_date);    printf("Enter new Name : ");  scanf(" %49[^\n]", m.name);  printf("Enter new Category : ");  scanf(" %29[^\n]", m.category);  printf("Enter new Price : ");  scanf("%f", &m.price);  printf("Enter new Quantity : ");  scanf("%d", &m.quantity);  printf("Enter new Expiry(YYYY-MM-DD): ");  scanf(" %10[^\n]", m.expiry\_date);    FILE \*fp = fopen(MED\_FILE, "r+b"); /\* read+write binary, does not truncate \*/  if (fp == NULL) {  printf("Error opening file.\n");  return;  }  fseek(fp, pos, SEEK\_SET);  fwrite(&m, sizeof(Medicine), 1, fp);  fclose(fp);    printf("Medicine updated successfully!\n");  } |

### deleteMedicine() — Delete (Admin)

*Since C's binary files cannot easily remove a record from the middle, this function rebuilds the file: it copies every record except the target ID into a temporary file, then deletes the original and renames the temporary file to replace it.*

|  |
| --- |
| void deleteMedicine() {  int id;  Medicine m;  int deleted = 0;    printf("\nEnter Medicine ID to delete: ");  scanf("%d", &id);    FILE \*fp = fopen(MED\_FILE, "rb");  FILE \*temp = fopen("temp.dat", "wb");  if (fp == NULL || temp == NULL) {  printf("Error opening file.\n");  return;  }    while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  if (m.id == id) {  deleted = 1; /\* skip writing this record -> effectively deletes it \*/  continue;  }  fwrite(&m, sizeof(Medicine), 1, temp);  }  fclose(fp);  fclose(temp);    remove(MED\_FILE);  rename("temp.dat", MED\_FILE);    if (deleted)  printf("Medicine ID %d deleted successfully.\n", id);  else  printf("Medicine ID %d not found.\n", id);  } |

### searchMedicine() — Search by ID or Name (Admin & Customer)

*Offers a choice of search by exact ID (using findMedicineByID()) or by partial name match (using strstr() while scanning the file), printing every matching record.*

|  |
| --- |
| void searchMedicine() {  int choice;  Medicine m;    printf("\nSearch by:\n1. ID\n2. Name\nChoice: ");  scanf("%d", &choice);    if (choice == 1) {  int id;  printf("Enter ID: ");  scanf("%d", &id);  if (findMedicineByID(id, &m) != -1)  printf("Found -> ID:%d Name:%s Category:%s Price:%.2f Qty:%d Expiry:%s\n",  m.id, m.name, m.category, m.price, m.quantity, m.expiry\_date);  else  printf("Medicine not found.\n");  } else {  char name[50];  int found = 0;  printf("Enter Name (or part of it): ");  scanf(" %49[^\n]", name);    FILE \*fp = fopen(MED\_FILE, "rb");  if (fp == NULL) { printf("No records found.\n"); return; }    while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  if (strstr(m.name, name) != NULL) {  printf("Found -> ID:%d Name:%s Category:%s Price:%.2f Qty:%d Expiry:%s\n",  m.id, m.name, m.category, m.price, m.quantity, m.expiry\_date);  found = 1;  }  }  fclose(fp);  if (!found) printf("No matching medicine found.\n");  }  } |

### checkNearExpiry() / checkExpiredMedicine() — Expiry Reports (Admin)

*Both functions scan the file and use daysUntil() to classify each record: checkNearExpiry() lists medicines expiring within the next 30 days, while checkExpiredMedicine() lists medicines whose expiry date has already passed.*

|  |
| --- |
| void checkNearExpiry() {  Medicine m;  FILE \*fp = fopen(MED\_FILE, "rb");  int found = 0;    if (fp == NULL) {  printf("\nNo records found.\n");  return;  }    printf("\n--- Medicines Expiring Within %d Days ---\n", NEAR\_EXPIRY\_DAYS);  printf("%-5s %-20s %-10s %-12s %-10s\n", "ID", "Name", "Quantity", "Expiry", "Days Left");  printf("-----------------------------------------------------------\n");    while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  int days = daysUntil(m.expiry\_date);  if (days >= 0 && days <= NEAR\_EXPIRY\_DAYS) {  printf("%-5d %-20s %-10d %-12s %-10d\n", m.id, m.name, m.quantity, m.expiry\_date, days);  found = 1;  }  }  fclose(fp);    if (!found) printf("No medicines are nearing expiry.\n");  }    // Show medicines that have already expired  void checkExpiredMedicine() {  Medicine m;  FILE \*fp = fopen(MED\_FILE, "rb");  int found = 0;    if (fp == NULL) {  printf("\nNo records found.\n");  return;  }    printf("\n--- Expired Medicines ---\n");  printf("%-5s %-20s %-10s %-12s\n", "ID", "Name", "Quantity", "Expiry");  printf("-------------------------------------------------\n");    while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  if (daysUntil(m.expiry\_date) < 0) {  printf("%-5d %-20s %-10d %-12s\n", m.id, m.name, m.quantity, m.expiry\_date);  found = 1;  }  }  fclose(fp);    if (!found) printf("No expired medicines found.\n");  } |

### deleteExpiredMedicine() — Bulk Cleanup (Admin)

*Uses the same rebuild-the-file technique as deleteMedicine(), but removes every record whose daysUntil() value is negative in a single pass, keeping the inventory file free of expired stock.*

|  |
| --- |
| void deleteExpiredMedicine() {  Medicine m;  int deletedCount = 0;    FILE \*fp = fopen(MED\_FILE, "rb");  FILE \*temp = fopen("temp.dat", "wb");  if (fp == NULL || temp == NULL) {  printf("Error opening file.\n");  return;  }    while (fread(&m, sizeof(Medicine), 1, fp) == 1) {  if (daysUntil(m.expiry\_date) < 0) {  deletedCount++; /\* skip writing -> deletes it \*/  continue;  }  fwrite(&m, sizeof(Medicine), 1, temp);  }  fclose(fp);  fclose(temp);    remove(MED\_FILE);  rename("temp.dat", MED\_FILE);    printf("\n%d expired medicine record(s) deleted.\n", deletedCount);  } |

### adminMenu() — Admin Panel Controller

*A menu-driven loop that dispatches to each of the CRUD and expiry-management functions above based on the admin's numeric choice, looping until the admin selects "Back to Main Menu".*

|  |
| --- |
| void adminMenu() {  int choice;  do {  printf("\n===== ADMIN PANEL =====\n");  printf("1. Add Medicine Batch\n");  printf("2. View All Medicines\n");  printf("3. Update Medicine\n");  printf("4. Delete Medicine (by ID)\n");  printf("5. Search Medicine\n");  printf("6. Check Near-Expiry Medicines\n");  printf("7. Check Expired Medicines\n");  printf("8. Delete All Expired Medicines\n");  printf("9. Back to Main Menu\n");  printf("Enter choice: ");  scanf("%d", &choice);    switch (choice) {  case 1: addMedicine(); break;  case 2: viewMedicines(); break;  case 3: updateMedicine(); break;  case 4: deleteMedicine(); break;  case 5: searchMedicine(); break;  case 6: checkNearExpiry(); break;  case 7: checkExpiredMedicine(); break;  case 8: deleteExpiredMedicine(); break;  case 9: printf("Returning to main menu...\n"); break;  default: printf("Invalid choice.\n");  }  } while (choice != 9);  } |

### addToCart() / viewCart() — Customer Shopping Cart

*addToCart() looks up the medicine, rejects it if expired or if the requested quantity exceeds available stock, then appends a CartItem to the in-memory cart array. viewCart() iterates the cart to print each line item along with the running subtotal.*

|  |
| --- |
| void addToCart() {  int id, qty;  Medicine m;    printf("\nEnter Medicine ID to add to cart: ");  scanf("%d", &id);    if (findMedicineByID(id, &m) == -1) {  printf("Medicine not found.\n");  return;  }    if (daysUntil(m.expiry\_date) < 0) {  printf("This medicine has expired and cannot be sold.\n");  return;  }    printf("Enter Quantity: ");  scanf("%d", &qty);    if (qty > m.quantity) {  printf("Insufficient stock! Only %d available.\n", m.quantity);  return;  }    if (cartCount >= MAX\_CART) {  printf("Cart is full.\n");  return;  }    cart[cartCount].id = m.id;  strcpy(cart[cartCount].name, m.name);  cart[cartCount].price = m.price;  cart[cartCount].qty = qty;  cartCount++;    printf("%s (x%d) added to cart.\n", m.name, qty);  }    void viewCart() {  float subtotal = 0;  if (cartCount == 0) {  printf("\nYour cart is empty.\n");  return;  }    printf("\n%-5s %-20s %-10s %-5s %-10s\n", "ID", "Name", "Price", "Qty", "Subtotal");  printf("---------------------------------------------------\n");  for (int i = 0; i < cartCount; i++) {  float line = cart[i].price \* cart[i].qty;  subtotal += line;  printf("%-5d %-20s %-10.2f %-5d %-10.2f\n",  cart[i].id, cart[i].name, cart[i].price, cart[i].qty, line);  }  printf("---------------------------------------------------\n");  printf("Subtotal: %.2f | Tax (%.0f%%): %.2f | Total: %.2f\n",  subtotal, TAX\_RATE \* 100, subtotal \* TAX\_RATE, subtotal \* (1 + TAX\_RATE));  } |

### updateStockAfterPurchase() & logTransaction()

*After a successful checkout, updateStockAfterPurchase() finds the medicine's offset and rewrites its quantity field in place. logTransaction() appends one line per purchased item to transactions.txt, all sharing the same timestamp-based transaction ID.*

|  |
| --- |
| void updateStockAfterPurchase(int id, int qtyBought) {  Medicine m;  long pos = findMedicineByID(id, &m);  if (pos == -1) return;    m.quantity -= qtyBought;    FILE \*fp = fopen(MED\_FILE, "r+b");  if (fp == NULL) return;  fseek(fp, pos, SEEK\_SET);  fwrite(&m, sizeof(Medicine), 1, fp);  fclose(fp);  }    // Logs one line per cart item, all sharing the same txnId (current timestamp),  // so a single checkout with multiple items still ties back to one transaction.  void logTransaction(long txnId) {  FILE \*fp = fopen(TXN\_FILE, "a");  if (fp == NULL) return;  for (int i = 0; i < cartCount; i++) {  fprintf(fp, "%ld|%d|%s|%d|%.2f\n",  txnId, cart[i].id, cart[i].name, cart[i].qty, cart[i].price);  }  fclose(fp);  } |

### checkout() — Finalize Purchase & Generate Invoice

*Prints an itemised invoice for everything in the cart, calculates the subtotal, tax (5%), and total, then deducts the purchased quantities from the inventory file, logs the transaction, and clears the cart.*

|  |
| --- |
| void checkout() {  float subtotal = 0, total;    if (cartCount == 0) {  printf("\nCart is empty. Nothing to checkout.\n");  return;  }    printf("\n========== INVOICE ==========\n");  printf("%-5s %-20s %-10s %-5s %-10s\n", "ID", "Name", "Price", "Qty", "Subtotal");  for (int i = 0; i < cartCount; i++) {  float line = cart[i].price \* cart[i].qty;  subtotal += line;  printf("%-5d %-20s %-10.2f %-5d %-10.2f\n",  cart[i].id, cart[i].name, cart[i].price, cart[i].qty, line);  }    total = subtotal \* (1 + TAX\_RATE);  printf("------------------------------\n");  printf("Subtotal : %.2f\n", subtotal);  printf("Tax (%.0f%%): %.2f\n", TAX\_RATE \* 100, subtotal \* TAX\_RATE);  printf("TOTAL : %.2f\n", total);  printf("==============================\n");    /\* Update stock levels for each purchased medicine \*/  for (int i = 0; i < cartCount; i++) {  updateStockAfterPurchase(cart[i].id, cart[i].qty);  }    logTransaction((long)time(NULL));    printf("\nPayment successful! Thank you for your purchase.\n");  cartCount = 0; /\* clear cart \*/  } |

### customerMenu() & main() — Program Entry Point

*customerMenu() drives the customer-facing options (browse, search, add to cart, view cart, checkout). main() displays the welcome banner and routes the user to either the Admin Panel or Customer Panel until they choose to exit.*

|  |
| --- |
| void customerMenu() {  int choice;  do {  printf("\n===== CUSTOMER PANEL =====\n");  printf("1. View Available Medicines\n");  printf("2. Search Medicine\n");  printf("3. Add to Cart\n");  printf("4. View Cart\n");  printf("5. Checkout\n");  printf("6. Back to Main Menu\n");  printf("Enter choice: ");  scanf("%d", &choice);    switch (choice) {  case 1: viewMedicines(); break;  case 2: searchMedicine(); break;  case 3: addToCart(); break;  case 4: viewCart(); break;  case 5: checkout(); break;  case 6: printf("Returning to main menu...\n"); break;  default: printf("Invalid choice.\n");  }  } while (choice != 6);  }    // MAIN MENU  int main() {  int choice;    printf("=====================================================\n");  printf(" MEDICAL STORE MANAGEMENT SYSTEM (C Language)\n");  printf("=====================================================\n");    do {  printf("\n1. Admin Panel\n");  printf("2. Customer Panel\n");  printf("3. Exit\n");  printf("Enter choice: ");  scanf("%d", &choice);    switch (choice) {  case 1: adminMenu(); break;  case 2: customerMenu(); break;  case 3: printf("\nExiting... Thank you!\n"); break;  default: printf("Invalid choice. Try again.\n");  }  } while (choice != 3);    return 0;  } |

# 5. Testing / Sample Output

The program was compiled with GCC and run from the console to verify each requirement in Section 2. The following scenarios were exercised manually:

* Admin: adding a new medicine batch and confirming it appears in "View All Medicines".
* Admin: updating an existing record by ID and re-viewing the list to confirm the change was saved in place.
* Admin: deleting a record by ID and confirming it no longer appears, while other records remain intact.
* Admin: checking near-expiry and expired medicine reports against sample expiry dates.
* Customer: searching for a medicine by name, adding it to the cart, and viewing the cart subtotal.
* Customer: attempting to add more quantity than available in stock, and confirming the system rejects it.
* Customer: completing checkout and confirming the invoice total (subtotal + 5% tax), the stock deduction in medicines.dat, and the new line in transactions.txt.

# Key features:![](data:image/png;base64...)

# Medincine Batches Update:

# ![](data:image/png;base64...)

# Adding to cart in customer panel:

![](data:image/png;base64...)

# Total invoice after tax calculation:

![](data:image/png;base64...)

# Payment successful:

![](data:image/png;base64...)

# Checks the quantity after buying medicines:

![](data:image/png;base64...)

# 6. Conclusion & Future Scope

## 6.1 Conclusion

The Medical Store Management System successfully implements all planned CRUD operations for inventory management, along with a complete customer purchase flow backed by binary file persistence. Building the project reinforced practical use of C structures, file handling with fseek()-based in-place updates, and modular program design, while the expiry-tracking features added a layer of real-world business logic beyond the basic CRUD requirements.

## 6.2 Future Scope

* Add user authentication so the Admin and Customer panels require a login.
* Replace the flat binary/text files with a lightweight database (e.g., SQLite) for better scalability and querying.
* Add low-stock alerts and simple sales reporting/analytics from the transaction log.
* Build a graphical (GUI) front-end in place of the current console menu interface.