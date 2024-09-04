import import_ipynb
import matplotlib
matplotlib.use('Agg')

from main import read_data,preprocess_data,analysis_pipeline,generate_pdf_report

def main():
    while True:
        print("Enter command (run analysis, generate report, quit):")
        command = input().strip().lower()

        if command == 'quit':
            print("Exiting...")
            break
        elif command == 'run analysis':
            data_file = 'olympics2024.csv.csv'
            target_column = 'Total'
            try:
                import pandas as pd
                data = read_data(data_file)
                analysis_pipeline(data, target_column)
                print("Analysis completed.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command == 'generate report':
            report_file = 'main.ipynb'
            plots = {
                'Descriptive Statistics': 'Gold_plots.png',
                'Correlation Matrix': 'correlation_matrix.png',
                'K-Means Clustering': 'kmeans_clusters.png'
            }
            try:
                generate_pdf_report(report_file, plots)
                print("Report generated.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
