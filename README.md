# Sales Data Cleaner

#1. Project Title & Goal
This project processes a messy sales CSV file, cleans the data, removes duplicate records, converts prices from USD to INR, and generates a clean JSON report.

#2. Setup Instructions
1. Ensure Python 3 is installed on your system.
2. Place `main.py` and `sales.csv` in the same directory.
3. Run the script using the following command:
4. After execution, a file named `clean_sales.json` will be generated in the same directory.


#3. The Logic (How you thought)

 Why did you choose this approach?
I chose a simple and clear ETL approach using Python’s built-in libraries (`csv` and `json`) to keep the solution lightweight and fully local, as required by the problem statement.  
The process follows clear steps: reading raw data, cleaning values, removing duplicates, converting currency, and exporting the final clean data.

What was the hardest bug you faced, and how did you fix it?
The main challenge was handling duplicate records correctly. Initially, duplicates were not removed because prices were treated as strings.  
I fixed this by converting the price field to a float before using it in the deduplication logic.


#4. Output Screenshots
Below is the screenshot of the final `clean_sales.json` file showing cleaned, deduplicated data:
<img width="1919" height="1079" alt="Screenshot 2026-01-28 103706" src="https://github.com/user-attachments/assets/180efc9d-5813-43aa-8015-1ed31cd7e322" />



#5. Future Improvements
If I had more time, I would:
Add better error handling for invalid or missing data
Support configurable currency conversion rates
Generate summary statistics such as total sales per product or country
