import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("COVID 19 ANALYSIS OF TOP 15 COUNTRIES")
data= pd.read_csv("covid.csv")
print(data)

# Function to display the menu and handle user input
def display_menu():
    print("COVID-19 ANALYSIS OF TOP 15 COUNTRIES")
    while True:
        print("\nMain Menu:")
        print("1. Search")
        print("2. DataFrame Attributes")
        print("3. Analysis")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            search_menu()
        elif choice == '2':
            data_frame_attributes()
        elif choice == '3':
            analysis()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display the search menu
def search_menu():
    print("\nSearch Menu:")
    print("1. Search for a Specific Country")
    print("2. Search by Column Heading")
    print("3. Back to Main Menu")
    ch = input("Enter your choice: ")
    
    if ch == '1':
        country_name = input("Enter the name of the country: ")
        search_country(country_name)
    elif ch == '2':
        column_name = input("Enter the column/heading name: ")
        search_by_column(column_name)
    elif ch == '3':
        pass
    else:
        print("Invalid choice. Please try again.")

# Function to search for a specific country
def search_country(country_name):
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        print(country_data)
    else:
        print("Country not found in the dataset.")

# Function to search by a specific column heading
def search_by_column(column_name):
    if column_name in data.columns:
        column_data = data[column_name]
        print(column_data)
    else:
        print("Column not found in the dataset.")

# Function to display DataFrame attributes
def data_frame_attributes():
    print("\nDataFrame Attributes:")
    print("1. Display Index")
    print("2. Display DataFrame as Ndarray")
    print("3. Display Shape")
    print("4. Display Number of Dimensions")
    print("5. Display Number of Elements")
    print("6. Back to Main Menu")
    
    ch = input("Enter your choice: ")
    if ch == '1':
        print(data.index)
    elif ch == '2':
        print(data.values)
    elif ch == '3':
        print(data.shape)
    elif ch == '4':
        print(data.ndim)
    elif ch == '5':
        print(data.size)
    elif ch == '6':
        pass
    else:
        print("Invalid choice. Please try again.")

# Function to perform data analysis
def analysis():
    while True:
        print("\nAnalysis of COVID-19 Data:")
        print("1. Total Cases")
        print("2. Total Deaths")
        print("3. Total Recovered Cases")
        print("4. Active Cases")
        print("5. Serious Cases")
        print("6. Total Tests Taken")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            analyze_total_cases(data)
        elif choice == '2':
            analyze_total_deaths(data)
        elif choice == '3':
            analyze_total_recovered(data)
        elif choice == '4':
            analyze_active_cases(data)
        elif choice == '5':
            analyze_serious_cases(data)
        elif choice == '6':
            analyze_total_tests(data)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def analyze_total_cases(data):
    # Analysis and visualization for Total Cases
    # ...
    # Summary statistics for Total Cases
    total_cases_sum = data["Total Cases"].sum()
    total_cases_mean = data["Total Cases"].mean()
    total_cases_min = data["Total Cases"].min()
    total_cases_max = data["Total Cases"].max()
    
    print("Analysis of Total Cases in the top 15 countries:")
    print("Total Number of Cases:", total_cases_sum)
    print("Average Cases:", total_cases_mean)
    print("Minimum Cases:", total_cases_min)
    print("Maximum Cases:", total_cases_max)
    
    # Plot Total Cases
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Total Cases", y="Country", data=data, palette="viridis")
    plt.title("Total COVID-19 Cases in Top 15 Countries")
    plt.xlabel("Total Cases")
    plt.ylabel("Country")
    plt.show()

def analyze_total_deaths(data):
    # Analysis and visualization for Total Deaths
    # ...
        # Summary statistics for Total Deaths
    total_deaths_sum = data["Total Death"].sum()
    total_deaths_mean = data["Total Death"].mean()
    total_deaths_min = data["Total Death"].min()
    total_deaths_max = data["Total Death"].max()
    
    print("\nAnalysis of Total Deaths in the top 15 countries:")
    print("Total Number of Deaths:", total_deaths_sum)
    print("Average Deaths:", total_deaths_mean)
    print("Minimum Deaths:", total_deaths_min)
    print("Maximum Deaths:", total_deaths_max)
    
    # Plot Total Deaths as a bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Total Death", y="Country", data=data, palette="magma")
    plt.title("Total COVID-19 Deaths in Top 15 Countries")
    plt.xlabel("Total Deaths")
    plt.ylabel("Country")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def analyze_total_recovered(data):
    # Analysis and visualization for Total Recovered Cases
    # ...
        # Summary statistics for Total Recovered Cases
    total_recovered_sum = data["Total Recovered"].sum()
    total_recovered_mean = data["Total Recovered"].mean()
    total_recovered_min = data["Total Recovered"].min()
    total_recovered_max = data["Total Recovered"].max()
    
    print("\nAnalysis of Total Recovered Cases in the top 15 countries:")
    print("Total Number of Recovered Cases:", total_recovered_sum)
    print("Average Recovered Cases:", total_recovered_mean)
    print("Minimum Recovered Cases:", total_recovered_min)
    print("Maximum Recovered Cases:", total_recovered_max)
    
    # Plot Total Recovered Cases as a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(data["Total Recovered"], labels=data["Country"], autopct='%1.1f%%', startangle=140)
    plt.title("Total COVID-19 Recovered Cases in Top 15 Countries")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    plt.show()

def analyze_active_cases(data):
    # Check if the column name exists in the dataset
    column_name = "Active Cases"  # Replace with the actual column name
    if column_name in data.columns:
        active_cases_sum = data[column_name].sum()
        active_cases_mean = data[column_name].mean()
        active_cases_min = data[column_name].min()
        active_cases_max = data[column_name].max()

        print("\nAnalysis of Active Cases in the top 15 countries:")
        print("Total Number of Active Cases:", active_cases_sum)
        print("Average Active Cases:", active_cases_mean)
        print("Minimum Active Cases:", active_cases_min)
        print("Maximum Active Cases:", active_cases_max)

        # Plot Active Cases as a scatter plot
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x="Country", y=column_name, data=data, color="red")
        plt.title("Active COVID-19 Cases in Top 15 Countries")
        plt.xlabel("Country")
        plt.ylabel("Active Cases")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print(f"\nThe '{column_name}' column does not exist in the dataset.")


def analyze_serious_cases(data):
    # Analysis and visualization for Serious Cases
    # ...
        # Summary statistics for Serious Cases
    serious_cases_sum = data["Serious Cases"].sum()
    serious_cases_mean = data["Serious Cases"].mean()
    serious_cases_min = data["Serious Cases"].min()
    serious_cases_max = data["Serious Cases"].max()
    
    print("\nAnalysis of Serious/Critical Cases in the top 15 countries:")
    print("Total Number of Serious Cases:", serious_cases_sum)
    print("Average Serious Cases:", serious_cases_mean)
    print("Minimum Serious Cases:", serious_cases_min)
    print("Maximum Serious Cases:", serious_cases_max)
    
    # Plot Serious Cases as a line plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Country", y="Serious Cases", data=data, marker="o", color="blue")
    plt.title("Serious/Critical COVID-19 Cases in Top 15 Countries")
    plt.xlabel("Country")
    plt.ylabel("Serious Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def analyze_total_tests(data):
    # Analysis and visualization for Total Tests Taken
    # ...
        # Summary statistics for Total Tests
    total_tests_sum = data["Total Tests"].sum()
    total_tests_mean = data["Total Tests"].mean()
    total_tests_min = data["Total Tests"].min()
    total_tests_max = data["Total Tests"].max()
    
    print("\nAnalysis of Total Tests Taken in the top 15 countries:")
    print("Total Number of Tests Taken:", total_tests_sum)
    print("Average Tests Taken:", total_tests_mean)
    print("Minimum Tests Taken:", total_tests_min)
    print("Maximum Tests Taken:", total_tests_max)
    
    # Plot Total Tests Taken as a bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Total Tests", y="Country", data=data, palette="magma")
    plt.title("Total COVID-19 Tests Taken in Top 15 Countries")
    plt.xlabel("Total Tests Taken")
    plt.ylabel("Country")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    
input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    display_menu()
