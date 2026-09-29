# Project Statement: Personal Expense Tracker

## Problem Statement
Many individuals struggle to keep an accurate, real-time log of their daily expenditures, leading to poor financial awareness and budget overruns. Traditional spreadsheet methods can be tedious, and heavy mobile applications often have overwhelming interfaces. There is a need for a lightweight, straightforward tool to track money spent on the go.

## Scope of the Project
This project provides a localized, session-based CLI application that allows users to quickly input expense data, view their current list of purchases, and calculate the total money spent. The scope is strictly limited to in-memory tracking during the active application session, utilizing basic Python data structures (lists and dictionaries) and modular programming.

## Target Users
* College students managing daily allowances or pocket money.
* Individuals looking for a minimalist, distraction-free way to log daily spending.
* Beginners learning personal finance management.

## High-Level Features
1. **Expense Ingestion:** Interactive prompts for capturing item names and monetary values.
2. **Data Validation:** Built-in loops to prevent application crashes from improper user inputs (e.g., string characters in float fields).
3. **Ledger Display:** A readable iteration of the user's financial inputs.
4. **Automated Aggregation:** A running sum of all expenses added to the ledger.