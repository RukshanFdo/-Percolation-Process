# Percolation-Process
This Python program simulates a simple percolation process, allowing users to generate dynamic grids and determine if percolation is possible for each column.

<h3>Problem Statement</h3>
In this coursework, the objective is to develop a Python program that generates a dynamic grid based on user input. The grid consists of random 2-digit numbers with randomly placed empty slots. The program then checks each column for possible percolation, indicating whether it's possible for liquid to pass through the filter in each column.

<h3>Tasks to Complete</h3>

1. Utilize proper Python 3.x program constructs such as packages, modules, functions, variables, and data structures.

2. Accept grid size dynamically as a command-line argument, defaulting to 5x5 if no dimensions are provided. Grid size must be between 3x3 and 9x9.
   
3. Automatically populate the grid with 2-digit random numbers and randomly placed empty slots.
  
4. Display the percolation status at the end of each column, indicating whether percolation is possible or not.
   
5. Avoid using NumPy for grid generation.
   
6. Optionally, use the PrettyTable module for enhancing the grid appearance.
   
7. Save the results to text files, with each result going to a separate file.
   
8. Optionally, challenge activity includes generating an HTML file for viewing the results in a web browser.
   
<h3>Solution Outline</h3>

1. Prompt the user to enter the size of the grid.

2. Validate user input to ensure it falls within the specified range (3x3 to 9x9).
   
3. Generate a dynamic grid with random 2-digit numbers and randomly placed empty slots.
   
4. Check each column of the grid for percolation, indicating the status at the bottom of each column.
   
5. Print the grid with percolation statuses to the command prompt and save the results to text files.
   
6. Convert the text files to HTML format for viewing in a web browser.
<h3>Python Codes</h3>

1. <strong>perc.py:</strong> Main program file responsible for accepting user input and triggering grid generation and percolation checks.

2. <strong>algorithm.py:</strong> Module containing functions for generating the grid and checking percolation.
   
3. <strong>sheet.py:</strong> Module for displaying the grid, writing results to text files, and updating file numbers.
   
4. <strong>html.py:</strong> Module for converting text files to HTML format for web viewing.

<h3>Usage</h3>
Run perc.py with optional command-line arguments specifying the grid size. 

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/RukshanFdo/Percolation-Process.git
   ```

2. Navigate to the directory.
 ```bash
 cd Percolation-Process
```

3. Run the Python program.
 ```bash
   python perc.py 4x6
```

4. If no dimensions are provided, a default 5x5 grid will be generated.

5. View the results in the command prompt and access the HTML files in the <b>'htmlcode/record'</b> directory for web viewing.
