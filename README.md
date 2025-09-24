Got it — here’s the rewritten README in proper Markdown:

````markdown
# ICS Calendar File Splitter

A small Python tool to split large `.ics` calendar files into smaller, import-friendly chunks.  
Useful when Google Calendar or other services reject large `.ics` files with errors like **“Oops, cannot import”**.

---

## 🚀 Overview
Some calendar exports (e.g., Google Takeout) can be **megabytes in size** and contain thousands of events.  
Google Calendar often fails to import these files. This script fixes the problem by splitting the calendar into multiple valid `.ics` files, each under a size limit (default: **400 KB**).

---

## ✨ Key Features
- Keeps all event details intact (no cutting events in half)  
- Preserves calendar metadata and timezone definitions  
- Splits automatically at `VEVENT` boundaries  
- Outputs multiple valid `.ics` files ready to import into Google Calendar  
- Creates a `calendar_parts/` folder with your split files  
- Prints how many events each file contains  

---

## 🔧 How It Works
1. Reads your `.ics` file  
2. Copies the calendar header and footer  
3. Groups events (`BEGIN:VEVENT ... END:VEVENT`)  
4. Fills each output file up to ~400 KB, then starts a new one  
5. Writes all parts into a `calendar_parts/` folder in the same location as your input file  

---

## 🖥️ Usage
1. Put your `.ics` file into the project folder (or note its path).  
2. Run the script in your terminal:

   ```bash
   python3 ics-splitter.py
````

> By default, it will look for `calendar-to-split.ics` in the same folder.
> You can change the filename in the last line of the script.

3. After running, check the new folder:

   ```
   calendar_parts/
   ├── calendar_part_1.ics
   ├── calendar_part_2.ics
   └── ...
   ```

4. Go to [Google Calendar](https://calendar.google.com/) → **Settings** → **Import & export** → **Import**, and import each split file one by one.

---

## 💡 When to Use

* Importing a **Google Takeout** calendar export into a new account
* Migrating between accounts where `.ics` file is too large
* Splitting any `.ics` that’s too big to be accepted by Google Calendar

---
