import os
import re
import logging
import matplotlib.pyplot as plt
from datetime import datetime

# Directory containing the latency logs
log_dir = "latency_logs"

# Function to extract latency and timestamps from log files
def parse_log_file(log_file):
    # Regex to match the latency logs (e.g., "Latency for run_chat: 0.0023 seconds")
    latency_pattern = re.compile(r"Latency for (\w+): (\d+\.\d{4}) seconds")
    
    latency_data = {}

    with open(log_file, 'r') as file:
        for line in file:
            match = latency_pattern.search(line)
            if match:
                func_name = match.group(1)
                latency = float(match.group(2))
                # Store the timestamp and latency for each function
                if func_name not in latency_data:
                    latency_data[func_name] = []
                # We store the timestamp and latency
                timestamp = datetime.strptime(line.split(" - ")[0], '%Y-%m-%d %H:%M:%S')
                latency_data[func_name].append((timestamp, latency))
    
    return latency_data

# Function to analyze all log files and extract latency data
def analyze_logs():
    all_latency_data = {}
    
    # Loop through all log files in the latency_logs directory
    for log_file in os.listdir(log_dir):
        log_path = os.path.join(log_dir, log_file)
        if os.path.isfile(log_path) and log_file.endswith(".log"):
            logging.info(f"Analyzing log file: {log_path}")
            latency_data = parse_log_file(log_path)
            
            # Store latency data for each log file (for later comparison)
            for func_name, data in latency_data.items():
                if func_name not in all_latency_data:
                    all_latency_data[func_name] = []
                all_latency_data[func_name].append(data)
    
    return all_latency_data

# Function to plot the latency data for each function
def plot_latency_data(all_latency_data):
    for func_name, all_data in all_latency_data.items():
        # Prepare the data for plotting
        timestamps = []
        latencies = []
        
        # Extract timestamps and latencies for each log file run
        for data in all_data:
            for timestamp, latency in data:
                timestamps.append(timestamp)
                latencies.append(latency)
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, latencies, label=func_name, marker='o')
        plt.xlabel('Timestamp')
        plt.ylabel('Latency (seconds)')
        plt.title(f"Latency over time for function: {func_name}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()
        plt.grid(True)
        plt.show()

# Main function to run the analyzer
def main():
    # Run the analysis and get the data
    all_latency_data = analyze_logs()
    
    # Plot the latency data for each function call
    plot_latency_data(all_latency_data)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
