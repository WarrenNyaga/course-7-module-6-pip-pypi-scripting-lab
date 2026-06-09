from datetime import datetime

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be provided as a list.")
        
    # STEP 2: Generate a filename with today's date
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"
    
    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
            
    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")