# Bank System

A comprehensive banking system built in Python, featuring a Graphical User Interface (GUI), a robust business logic layer, a core management system for accounts, customers, and transactions, alongside utility tools for JSON data management.

This project simulates real-world banking operations, including user registration and authentication, management of three distinct account types (Checking, Savings, Loan), transaction execution (deposits, withdrawals, transfers), automated interest calculations, and centralized bank fund management.

## Project Structure

```text
BANK SYSTEM/
├── background.jpg          # Background image for the GUI
├── Code documentation/     # Project documentation files
├── core/                   # Core layer - business models
│   ├── account.py          # Account classes (Checking / Savings / Loan)
│   ├── BANK.py             # Bank funds and general interest management
│   ├── customer.py         # Customer class and data validation
│   └── transaction.py      # Transaction execution and validation (including transfers)
├── files/                  # JSON data files - accounts, customers, transactions
├── not in use/             # Deprecated or inactive files
├── utils/                  # General utility tools
│   ├── BANK_control.py     # Command Line Interface (CLI) for system management
│   ├── exceptions.py       # Custom exception definitions
│   ├── file_manager.py     # JSON file read/write/delete management
│   └── sorting.py          # Data sorting mechanisms for accounts, customers, and transactions
├── GUI.py                  # Graphical interface (customtkinter) - primary user entry point
└── logic.py                # Middleware connecting the GUI with core and utils
```

## System Architecture

The project is designed using a multi-layered architecture to ensure separation of concerns:

*   **GUI (`GUI.py`):** The front-end interface built with `customtkinter`. It handles user interactions, rendering login and registration screens, account management tabs, and action triggers.
*   **Business Logic (`logic.py`):** Acts as the middleware connecting the GUI to the underlying Core and Utils layers. It centralizes business workflows, such as customer authentication, account initialization, and transaction processing.
*   **Core (`core/`):** Contains the primary business models and internal logic. This includes customer representations, polymorphic account structures, transaction handling, and global bank fund management.
*   **Utils (`utils/`):** Provides general-purpose tools independent of specific business rules. This encompasses JSON file operations, data sorting algorithms, and an independent CLI for system administration.

## Key Features

*   **Secure Authentication:** Comprehensive customer registration and login system with strict validation for all fields (ID, email, phone, age, password).
*   **Account Variety:** Support for three distinct account types per customer (Checking, Savings, and Loan), each identified by a unique suffix (-C, -S, -L).
*   **Comprehensive Transactions:** Seamless execution of deposits, withdrawals, and transfers, both internally between a user's own accounts and externally to other clients.
*   **Rigorous Validation:** Built-in checks for transaction integrity, including credit limit verification, daily withdrawal caps, and account status validation (active, frozen, or closed).
*   **Automated Financials:** Automated calculation of monthly interest for savings accounts and dynamically adjusted interest rates for loan accounts based on credit scores.
*   **Centralized Fund Management:** System-wide tracking of collected fees and aggregated deposited or loaned funds.
*   **Automated Maintenance:** Post-operation sorting of all data files (accounts, customers, transactions) to maintain data organization.
*   **Administrative CLI:** A dedicated command-line interface (`BANK_control.py`) allowing administrators to perform file-level operations such as record deletion, editing, account freezing/unfreezing, and data visualization via text or HTML tables.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system along with the necessary dependencies:

```bash
pip install customtkinter
```

### Running the Application

To launch the Graphical User Interface:

```bash
python GUI.py
```

To utilize the Administrative Command Line Interface:

```bash
python utils/BANK_control.py [ARGUMENTS]
```

**CLI Examples:**

View the accounts data file:
```bash
python utils/BANK_control.py -v A
```

Freeze a specific account by ID:
```bash
python utils/BANK_control.py -f 356123456789
```

## Notes and Known Issues

*   **Logging:** The codebase currently utilizes print statements for debugging purposes. These should be transitioned to the standard Python `logging` module for production deployment.
*   **Error Handling:** Certain functions rely on broad `except` blocks that raise a generic `ValueError`. This practice may obscure the original stack trace and should be refined.
*   **Transaction Atomicity:** There is a known edge case regarding transaction interruption. If an unhandled exception occurs mid-transaction, it could result in partial state updates (e.g., account record deletion without transaction completion). Implementing atomicity or rollback mechanisms is recommended.
*   **Deprecated Code:** The `frame4()` function within the GUI and the contents of the `not in use/` directory are legacy artifacts and should be considered for removal.

## Technologies Used

*   **Python 3:** Core programming language.
*   **customtkinter:** For building the modern graphical user interface.
*   **argparse:** For parsing command-line arguments in the CLI module.
*   **JSON:** Utilized as the primary lightweight data storage format.
