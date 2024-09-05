import import_ipynb
import matplotlib
matplotlib.use('Agg')

from main import read_data, preprocess_data, analysis_pipeline, generate_pdf_report

def main():
    while True:
        print("Enter command (run analysis, generate report, quit):")
        command = input().strip().lower()

        if command == 'quit':
            print("Exiting...")
            break
        elif command == 'run analysis':
            data_file = 'olympics2024.csv'
            target_column = 'Total'
            try:
                if not isinstance(data_file, str):
                    raise ValueError("The file path must be a string.")
                analysis_pipeline(data_file, target_column)
                print("Analysis completed.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command == 'generate report':
            report_file = 'data_analysis_report.pdf'
            plots = {
                'Descriptive Statistics Plots': 'Total_plots.png',
                'Correlation Matrix': 'correlation_matrix.png',
                'K-Means Clustering Results': 'kmeans_clusters.png',
                'PCA Results': 'pca_plot.png'
            }
            try:
                if not isinstance(report_file, str):
                    raise ValueError("The report filename must be a string.")
                generate_pdf_report(report_file, plots) 
                print("Report generated.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
