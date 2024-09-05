# AI Employee Prototype for Data Analysis

AI Employee Prototype is a Python-based tool designed to automate data analysis and report generation. This system processes input data, applies statistical and machine-learning techniques, and generates detailed PDF reports with visualizations. All code is contained within a Jupyter Notebook (`main.ipynb`).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

```bash
pip install -r requirements.txt
```
## Usage
To use the AI Employee Prototype, you can either:

Run the main.ipynb Jupyter Notebook to execute the functions step by step.

Interact with the system via the command-line interface (CLI) provided by cli.py.

## Running the CLI
bash
```
python cli.py
```
## Commands
```
run analysis: Runs the analysis pipeline (PCA, K-Means, Linear Regression).
generate report: Generates a PDF report with visualizations.
quit: Exits the CLI.
```
Example Usage
bash
```
Enter command (run analysis, generate report, quit): run analysis

Example Dataset
Your dataset should be in CSV format with columns like:

Rank	Country	 Country Code	Gold	Silver	 Bronze	 Total
1	     USA	     US	         40	      44	  42	  126
2	     China	     CHN	     40	      27	  24	  91
3	     Japan	     JPN	     20	      12	  13	  45
```
## Testing
Since all functions are in main.ipynb, you can run tests directly in the notebook. For more complex testing, consider using tools like unittest or pytest in the future to write test cases for critical functions.

Example Test:
Inside the notebook, you can manually test each function by running individual cells. 

For example:
```
# Test the preprocess_data function
data = pd.read_csv('olympics2024.csv.csv')
preprocessed_data = preprocess_data(data)
print(preprocessed_data.head())
```
## 
Contributing Pull requests are welcome. For major changes, please open an issue first to discuss the changes you'd like to make.











