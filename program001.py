import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import os

# Constants
SEPARATOR = "===" * 52
CSV_FILE = "top50.csv"
CHART_TITLE = "Top 50 ARTISTS OF 2024"

# Load CSV file
df = pd.read_csv(CSV_FILE)

def display_menu():
    """Display the main menu."""
    print('INDEX')
    data = [
        [1, 'TO DISPLAY THE DATA'],
        [2, 'DATAFRAMES AND ATTRIBUTES'],
        [3, 'DISPLAY RECORDS'],
        [4, 'WORKING ON RECORDS'],
        [5, 'WORKING ON COLUMNS'],
        [6, 'DATA VISUALISATON'],
        [7, "EXIT"]
    ]
    header = ['S.NO', 'FUNCTIONS']
    print(tabulate(data, headers=header, tablefmt="grid"))

def get_choice(prompt="Enter the choice: "):
    """Get a valid numeric choice from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_choice(prompt):
    """Get a valid integer choice from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

display_menu()

# Main loop for menu selection
while True:
    choice = get_choice()
    
    # Display the entire DataFrame
    if choice == 1:
        print(df)
        print(SEPARATOR)
        
    # DataFrame attributes sub-menu
    elif choice == 2:
        while True:
            print("DATAFRAME AND ATTRIBUTES")
            print("2.1. Display the Transpose")
            print("2.2. Display all column Names")
            print("2.3. Display the indexes")
            print("2.4. Display the shape")
            print("2.5. Display the Dimension")
            print("2.6. Display the datatypes of all columns")
            print("2.7. Display the size")
            print("2.8. Display the values")
            print("2.9. Display the null values")
            print("2.10. Display the count of rows")
            print("2.11. Display the count of columns")
            print("2.12. Display whether DataFrame is empty")
            print("2.13. Display both the axes (axis 0=rows, axis 1=columns)")
            print("2.14. Display the maximum values from the DataFrame")
            print("2.15. Display the minimum values from the DataFrame")
            print("2.16. Display the sum of values in the DataFrame")
            print("2.17. Exit")
            ch2 = get_choice("Enter the sub-choice: ")
                        
            if ch2 == 2.1:
                print(df.T)
                print(SEPARATOR)
            elif ch2 == 2.2:
                print(df.columns)
                print(SEPARATOR)
            elif ch2 == 2.3:
                print(df.index)
                print(SEPARATOR)
            elif ch2 == 2.4:
                print(df.shape)
                print(SEPARATOR)
            elif ch2 == 2.5:
                print(df.ndim)
                print(SEPARATOR)
            elif ch2 == 2.6:
                print(df.dtypes)
                print(SEPARATOR)
            elif ch2 == 2.7:
                print(df.size)
                print(SEPARATOR)
            elif ch2 == 2.8:
                print(tabulate(df.values , headers=header ,tablefmt="grid"))
                print(SEPARATOR)
            elif ch2 == 2.9:
                print(df.isnull())
                print(SEPARATOR)
            elif ch2 == 2.10:
                print(df.count())
                print(SEPARATOR)
            elif ch2 == 2.11:
                print(df.count(axis=1))
                print(SEPARATOR)
            elif ch2 == 2.12:
                print(df.empty)
                print(SEPARATOR)
            elif ch2 == 2.13:
                print(df.axes)
                print(SEPARATOR)
            elif ch2 == 2.14:
                print(df.max())
                print(SEPARATOR)
            elif ch2 == 2.15:
                print(df.min())
                print(SEPARATOR)
            elif ch2 == 2.16:
                print(df.sum())
                print(SEPARATOR)
            elif ch2 == 2.17:
                print(SEPARATOR)
                break

    
    # Display records sub-menu
    elif choice == 3:
        while True:
            print("DISPLAY")
            print("3.1. To display Top 5 records")
            print("3.2. To display Bottom 5 records")
            print("3.3. To display the specific number of records from the top")
            print("3.4. To display the specific number of records from the bottom")
            print("3.5. Exit")
            ch3 = get_choice("Enter the choice: ")
            
            if ch3 == 3.1:
                print(df.head())
                print(SEPARATOR)
            elif ch3 == 3.2:
                print(df.tail())
                print(SEPARATOR)
            elif ch3 == 3.3:
                n = get_int_choice("Enter the number of records to display from top: ")
                print(df.head(n))
                print(SEPARATOR)
            elif ch3 == 3.4:
                m = get_int_choice("Enter the number of records to display from bottom: ")
                print(df.tail(m))
                print(SEPARATOR)
            elif ch3 == 3.5:
                print(SEPARATOR)
                break
    
    # Working on records sub-menu
    elif choice == 4:
        while True:
            print("WORKING ON RECORDS")
            print("4.1 Insert a specific record")
            print("4.2 Exit")
            ch4 = get_choice("Enter the choice: ")
            
            if ch4 == 4.1:
                try:
                    a = input("Enter No.: ")
                    b = input("Enter the TRACK NAME: ")
                    c = input("Enter the ARTIST NAME: ")
                    d = input("Enter the GENRE: ")
                    e = int(input("Enter the BPM: "))
                    f = int(input("Enter the VALENCE: "))
                    g = int(input("Enter the ACOUSTICNESS: "))
                    h = int(input("Enter the LIVENESS: "))
                    i = int(input("Enter the POPULARITY: "))
                    new_index = len(df)
                    df.loc[new_index] = [a, b, c, d, e, f, g, h, i]
                    print(df)
                    print("Data inserted Successfully")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for numeric fields.")
            elif ch4 == 4.2:
                break
    
    # Working on columns sub-menu
    elif choice == 5:
        while True:
            print("Working on Columns menu")
            print("5.1 Insert a specific Column")
            print("5.2 Exit")
            ch5 = get_choice("Enter the choice: ")
            
            if ch5 == 5.1:
                v = input("Enter column name which needs to be inserted: ")
                if v in df.columns:
                    print("Column already exists.")
                else:
                    df[v] = np.nan  # Assuming new column with NaN values
                    print("Column successfully inserted")
            elif ch5 == 5.2:
                break
    
    # Data visualization sub-menu
    elif choice == 6:
        while True:
            print("Data Visualisation Menu")
            print("6.1 Plot line chart")
            print("6.2 Plot Vertical bar chart")
            print("6.3 Plot Horizontal bar chart")
            print("6.4  Plot Histogram chart")
            print("6.5 Plot Scatter chart")
            print("6.6 Exit")
            ch6 = get_choice("Enter input: ")
            
            if ch6 == 6.1:  # Line chart
                m = get_int_choice("How many records do you want from the bottom? ")
                df_subset = df.tail(m)
                df_subset.plot(kind="line")
                plt.title(CHART_TITLE)
                plt.xlabel("Index")
                plt.ylabel("Values")
                plt.legend()
                plt.grid(True)
                plt.show()

            elif ch6 == 6.2:  # Vertical bar chart
                m = get_int_choice("How many records do you want from the bottom? ")
                df_subset = df.tail(m)
                df_subset.plot(kind='bar')
                plt.title(CHART_TITLE)
                plt.xlabel("Index")
                plt.ylabel("Values")
                plt.legend()
                plt.grid(True)
                plt.show()

            elif ch6 == 6.3:  # Horizontal bar chart
                m = get_int_choice("How many records do you want from the bottom? ")
                df_subset = df.tail(m)
                df_subset.plot(kind="barh")
                plt.title(CHART_TITLE)
                plt.xlabel("Values")
                plt.ylabel("Index")
                plt.legend()
                plt.grid(True)
                plt.show()

            elif ch6 == 6.4:  # Histogram chart
                m = get_int_choice("How many records do you want from the top? ")
                df_subset = df.head(m)
                df_subset.plot(kind="hist")
                plt.title(CHART_TITLE)
                plt.xlabel("Values")
                plt.ylabel("Frequency")
                plt.legend()
                plt.grid(True)
                plt.show()

            elif ch6 == 6.5:  # Scatter chart
                m = get_int_choice("How many records do you want from the top? ")
                df_subset = df.head(m)
                if "SERIAL.NO" in df.columns and "LIVENESS" in df.columns and "VALENCE" in df.columns:
                    pm = df_subset["SERIAL.NO"]
                    pf = df_subset["LIVENESS"]
                    um = df_subset["VALENCE"]
                    plt.scatter(pm, pf, label="LIVENESS")
                    plt.scatter(pm, um, label="VALENCE")
                    plt.title(CHART_TITLE)
                    plt.xlabel("SERIAL.NO")
                    plt.ylabel("Values")
                    plt.legend()
                    plt.grid(True)
                    plt.show()
                else:
                    print("Required columns not found in the dataset.")
            
            elif ch6 == 6.6:  # Exit
                break
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option from the menu.")

