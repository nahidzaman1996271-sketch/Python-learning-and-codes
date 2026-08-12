**MEDICAL STORE MANAGEMENT SYSTEM**

**Group Task Division & Testing Script**

Nahid Ibn Zaman (252-35-571) • Mahmuda Khanum (252-35-537) • Farhan Ishraq Ifti (252-35-648)

*Course Project — SE133 — Summer 2026*

# **1. How the Work Is Split**

The C program has three natural jobs inside it: deciding things (logic), storing/retrieving things (functions & structures), and showing things correctly (output/testing). We mapped one team member to each job.

| **Member** | **Role Title** | **What They Own** |
| --- | --- | --- |
| **Nahid Ibn Zaman**  **ID: 252-35-571** | Core Logic & Business Rules Developer | Expiry-date calculations, checkout/billing math, stock deduction, cart validation rules, and the main program flow. |
| **Farhan Ishraq Ifti**  **ID: 252-35-648** | Functions & Data Structures (CRUD) Developer | Struct design, file read/write functions, and all Create / Read / Update / Delete / Search operations. |
| **Mahmuda Khanum**  **ID: 252-35-537** | Testing, QA & Output Formatting Lead | Runs every menu option as a test case, verifies results are correct, and owns the visual polish of every printed screen (tables, spacing, invoice layout). |

# **2. Nahid Ibn Zaman — Core Logic & Business Rules**

Owns every place in the code where the program makes a decision or does a calculation: is this medicine expired, is there enough stock, what's the total bill, what happens after a purchase.

| **Function / Block** | **Lines** | **What it does** |
| --- | --- | --- |
| **daysUntil()** | 72–88 | The core date-math function: works out how many days remain until a medicine's expiry date. Every expiry decision in the program calls this. |
| **addToCart() — validation logic** | 377–414 | Decides whether an item can be added: checks the medicine exists, checks it isn't expired (calls daysUntil), checks stock is enough. |
| **updateStockAfterPurchase()** | 437–449 | Business rule: after a sale, reduce the stored quantity by the amount bought. |
| **logTransaction()** | 451–461 | Decides how a completed sale is recorded to transactions.txt (one line per item, shared transaction ID). |
| **checkout() — totals logic** | 463–496 | Calculates subtotal, tax (5%) and grand total, then triggers the stock update and transaction log. |
| **checkNearExpiry() — filter rule** | 262–286 | Decision rule: which medicines count as “near expiry” (0–30 days left). |
| **checkExpiredMedicine() — filter rule** | 289–312 | Decision rule: which medicines count as already expired (days < 0). |
| **deleteExpiredMedicine() — filter rule** | 315–340 | Decision rule + control flow for wiping every expired batch in one pass. |
| **main() — program flow** | 526–549 | Top-level control flow: Admin vs Customer vs Exit. |

*Presentation angle: walk through one full purchase, explaining out loud, at each step, which rule from the table above just fired (expiry check → stock check → tax calculation → stock deduction → transaction log).*

# **3. Farhan Ishraq Ifti — Functions & Data Structures (CRUD)**

Owns the data model and every Create / Read / Update / Delete / Search function — the plumbing that reads and writes medicines.dat.

| **Function / Block** | **Lines** | **What it does** |
| --- | --- | --- |
| **struct Medicine / struct CartItem** | 14–31 | The two core data structures that hold every medicine record and every cart line. |
| **getNextID()** | 41–51 | Reads the file to work out the next free medicine ID. |
| **findMedicineByID()** | 54–68 | Shared lookup function used by nearly every other feature to find one record. |
| **addMedicine() — Create** | 94–120 | Takes admin input and appends a new medicine record to medicines.dat. |
| **viewMedicines() — Read** | 123–143 | Reads and lists every medicine record. |
| **updateMedicine() — Update** | 146–184 | Finds a record by ID, takes new values, and rewrites it in place. |
| **deleteMedicine() — Delete** | 187–219 | Removes one record by rebuilding the file without it. |
| **searchMedicine() — Search** | 222–257 | Search by ID or by (partial) name. |
| **adminMenu() / customerMenu()** | 344–373, 500–523 | The two menu functions that structure and route every feature. |

*Presentation angle: show the struct Medicine definition first, then demo Add → View → Update → Delete → Search in that order so the audience sees the full CRUD cycle acting on one record.*

# **4. Mahmuda Khanum — Testing, QA & Output Formatting**

This is a real, separate engineering role: nobody else on the team is checking that every feature actually works end-to-end, and nobody else is responsible for how the program looks on screen. Below is a ready-to-run script — no coding background needed, just follow it step by step, tick each box, and note anything that doesn't match.

## **4.1 Before you start**

* Compile the program once: gcc medical\_store\_management\_system.c -o mss (ask Nahid or Ifti to run this with you the first time).
* Run it fresh each time you start a new test so you're not carrying over cart items from a previous run.
* Keep a plain notes doc open and write down anything that looks wrong, misaligned, or confusing — that becomes your test report.

## **4.2 Admin Panel test cases**

| **#** | **Test Case (what to do)** | **What “PASS” looks like** |
| --- | --- | --- |
| 1 | Admin Panel → option 1 (Add Medicine Batch). Add a real medicine, e.g. “Napa”, category “Painkiller”, price 5, qty 100, expiry a future date. | Program prints “Medicine batch added successfully!” and assigns an ID. |
| 2 | Admin Panel → option 2 (View All Medicines). | Table header (ID / Name / Category / Price / Quantity / Expiry) lines up in neat columns — line 133. |
| 3 | Admin Panel → option 3 (Update Medicine) using the ID from Test 1. | “Current details” line prints correctly, then “Medicine updated successfully!” shows. |
| 4 | Admin Panel → option 5 (Search Medicine) by Name, type part of “Napa”. | Matching record(s) print with the “Found →” format — line 249. |
| 5 | Admin Panel → option 6 (Check Near-Expiry). Add one medicine expiring within 30 days first. | It appears in the near-expiry table with correct “Days Left” count — line 279. |
| 6 | Admin Panel → option 7 (Check Expired Medicines). Add one medicine with a past expiry date first. | It appears in the expired list — line 305. |
| 7 | Admin Panel → option 8 (Delete All Expired), then option 7 again. | Deletion count prints, and the expired list is now empty. |
| 8 | Admin Panel → option 4 (Delete Medicine) with a valid ID, then an ID that doesn't exist. | First shows “deleted successfully”, second shows “not found” — lines 216–218. |

## **4.3 Customer Panel test cases**

| **#** | **Test Case (what to do)** | **What “PASS” looks like** |
| --- | --- | --- |
| 9 | Customer Panel → option 1 (View Available Medicines). | Same neat table as the admin view. |
| 10 | Customer Panel → option 3 (Add to Cart) with a valid ID and a quantity less than stock. | “<name> (x<qty>) added to cart.” prints — line 413. |
| 11 | Add to Cart again, this time typing a quantity bigger than the stock on hand. | “Insufficient stock! Only X available.” prints and nothing is added — line 398. |
| 12 | Try to Add to Cart a medicine whose expiry date is in the past. | “This medicine has expired and cannot be sold.” prints — line 390. |
| 13 | Customer Panel → option 4 (View Cart). | Table lines up (ID / Name / Price / Qty / Subtotal), and Subtotal / Tax(5%) / Total match your own hand-calculation — line 432. |
| 14 | Customer Panel → option 5 (Checkout). | Invoice box prints between the “======” borders, totals match View Cart, and “Payment successful!” shows — lines 471–494. |
| 15 | Immediately View All Medicines again (Admin → option 2). | The stock quantity for the purchased item has dropped by exactly the amount bought. |
| 16 | Type a letter instead of a number at any “Enter choice” prompt. | Note down exactly what happens — this is a real weak spot to mention in the presentation. |

## **4.4 Output formatting review — make the prints beautiful**

This is the part that's fully yours to shape. Every table in the program is built with printf's %-Ns column codes (the number is how many characters wide that column is). Go through each one below, run the matching menu option, and check the columns actually line up on screen — especially with a long medicine name.

| **Screen** | **Line(s)** | **Format string** | **Check** |
| --- | --- | --- | --- |
| **Main table header** | 133 | printf("\n%-5s %-20s %-15s %-10s %-10s %-12s\n", ...) | ID / Name / Category / Price / Quantity / Expiry columns. |
| **Medicine data rows** | 137 | printf("%-5d %-20s %-15s %-10.2f %-10d %-12s\n", ...) | Must line up under the header above. |
| **Near-expiry table** | 273, 279 | printf("%-5s %-20s %-10s %-12s %-10s\n", ...) | Header and rows have 5 columns here, not 6 — check they still line up. |
| **Expired table** | 300, 305 | printf("%-5s %-20s %-10s %-12s\n", ...) | 4-column table. |
| **Cart table** | 423, 428 | printf("%-5s %-20s %-10s %-5s %-10s\n", ...) | Watch the “Qty” column — it's narrower (%-5s) than the others. |
| **Checkout invoice** | 471–485 | printf("========== INVOICE ==========\n") ... | The border line length should match the box contents. |
| **Admin / Customer menus** | 347–357, 503–510 | printf("1. Add Medicine Batch\n") ... | Numbered list — check spacing and wording is consistent across both menus. |

*If a column looks too narrow or too wide once you test it with real data (e.g. a long medicine name spills into the next column), note the exact line number and the new width you'd suggest, e.g. “line 133/137: change %-20s to %-25s for Name.” Hand that note to Ifti or Nahid — or, if you're comfortable, you can edit that one number yourself directly in the file; it's just text, not logic.*

## **4.5 What to say in the presentation (your 8 minutes)**

* Introduce your role: “I was responsible for testing every feature and for the visual presentation of the output.”
* Show 2–3 test cases live (pick one that passes cleanly and one edge case, e.g. Test 11 or 12, to show you tried to break it on purpose).
* Point out one formatting detail you checked or improved (e.g. the invoice box borders, or the Qty column width) and why it matters for a real user.
* Close with your overall verdict: does the program behave correctly across the Admin and Customer panels, and where would you send it back for more work?

# **5. Quick Reference — Whole-Program Map**

For anyone's own reference while presenting, here is the file end-to-end at a glance:

Lines 1–10 Includes, constants (file names, tax rate, cart size, near-expiry window)

Lines 12–31 Data structures — Ifti

Lines 33–68 Utility functions (ID lookup, record lookup) — Ifti

Lines 70–88 Date/expiry math — Nahid

Lines 90–219 Admin CRUD: Add / View / Update / Delete — Ifti

Lines 222–257 Search — Ifti

Lines 259–340 Expiry rules: near-expiry / expired / cleanup — Nahid

Lines 342–373 Admin menu — Ifti (structure) / all test — Mahmuda

Lines 375–461 Cart, stock update, transaction log — Nahid

Lines 463–496 Checkout / invoice / totals — Nahid

Lines 498–523 Customer menu — Ifti (structure) / all test — Mahmuda

Lines 526–549 main() program entry — Nahid

*Every screen the program ever prints is fair game for Mahmuda's formatting pass — that spans the whole file, which is why her role sits on top of both other roles rather than in one block of lines.*