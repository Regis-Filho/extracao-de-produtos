Kabum Web Scraper
This Python script allows you to extract information about products from the Kabum website based on a user-provided search query. It collects the product name, price, and link to the product page, saving these data in an Excel file.

Prerequisites
Make sure you have Python installed on your machine. This script requires the following Python libraries:

pandas
BeautifulSoup (bs4)
requests
re
math
You can install these libraries using pip:
pip install pandas beautifulsoup4 requests

How to Use
Run the script: Execute the script in a Python environment.
Enter the search term: When prompted, enter the search term to look for products on the Kabum website.

Wait for execution: The script will go through the results pages, collect the data, and save it in an Excel file named based on the search term.



Code Structure
Imports: Imports the necessary libraries.
Headers: Defines the headers for the HTTP request to mimic a browser.
Search term: Prompts the user for the search term.
Search URL: Formats the URL for the search on Kabum.
Request and parsing the page: Makes a request to the results page and uses BeautifulSoup to parse the HTML.
Number of products: Extracts the number of products found.
Data dictionary: Initializes a dictionary to store product data.
Page loop: Iterates over the results pages, collecting the name, price, and link of the products.
Product details request: Makes a request for each product page to get the price.
Storing the data: Stores the collected data in the dictionary.
Creating the DataFrame: Creates a pandas DataFrame with the collected data.
Saving to Excel: Saves the data to an Excel file.
Final message: Prints a message indicating completion.
Example Output
The generated Excel file will contain three columns:

Name: The name of the product.
Price: The price of the product.
Links: The link to the product page.
Notes
This script may not work correctly if the layout of the Kabum website changes.
Some product pages may fail to retrieve the price due to website restrictions or changes in the product page layout.
