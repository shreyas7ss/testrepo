import data_loader
import calculator
from utils import print_result

def run_pipeline():
    print("Starting data processing...")

    data = data_loader.load_data("input.csv")

    results = calculator.calculate_stats(data)

    print_result(results)

if __name__ == "__main__":
    run_pipeline()
    print("Pipeline finished.")