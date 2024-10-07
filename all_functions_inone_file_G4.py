import sys
import subprocess
 
from flask import Flask, request, jsonify

import csv

#check for Python version 

def check_python_version():
    result=subprocess.run(["powershell","python --version"], shell = True, check = True, stdout = subprocess.PIPE,
                          stderr = subprocess.STDOUT, timeout = 2)
    python_version=result.stdout.decode('utf-8').strip()

    if not '3.7.0' in python_version:
        print(f'{python_version} is not  Compartible')
        # sys.exit()
  
    
def update_version():
    try:
        
        result=subprocess.run(["powershell","python -m pip install --upgrade pip==23.0.1"], shell = True, check = True, timeout = 240)
        
    except subprocess.CalledProcessError as e:
        print(f'failed to update pip {e}')
        
def install_csv():
    try:
        print("Attempting to install csv module...")
        # Dummy subprocess call to simulate installation of csv
        result = subprocess.run(["powershell", "pip install csv"], shell=True, check=True, timeout=240)
        print("csv module installed successfully (Note: This is just a demonstration).")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install csv: {e}")


# function to   installation of serial.tools.list_ports
def install_serial_tools():
    try:
        print("Attempting to install serial.tools.list_ports...")
        # This line simulates a pip install for demonstration purposes
        result = subprocess.run(["powershell", "pip install serial"], shell=True, check=True, timeout=240)
        print("serial.tools.list_ports installed successfully (Note: This is just a demonstration).")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install serial.tools.list_ports: {e}")
        
# Function to simulate the installation of the sys module
def install_sys():
    try:
        print("Attempting to install sys module...")
        # This line simulates a pip install for demonstration purposes
        result = subprocess.run(["powershell", "pip install sys"], shell=True, check=True, timeout=240)
        print("sys module installed successfully (Note: This is just a demonstration).")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install sys: {e}")

#install_Pyserial
def install_pyserial():
    try:
        
        result=subprocess.run(["powershell","pip install pyserial==3.5"],shell=True,check=True,timeout=240)
    except subprocess.CalledProcessError as e:
        print(f'failed to install pyserial {e}')
#install_pyvisa
def install_pyvisa():
    try:
        result=subprocess.run(["powershell","pip install pyvisa==1.12.0"],shell=True,check=True,timeout=240)
    except subprocess.CalledProcessError as e:
        print(f'failed to install pyvisa {e}')
#install_PYTZ_and_Date&Time

def install_pytz_and_time():
    try:
        
        result=subprocess.run(["powershell","pip install pytz==2023.3"],shell=True,check=True,timeout=240)
    except subprocess.CalledProcessError as e:
        print(f'failed to install pytz&time {e}')
#install pandas

def install_pandas():
    try:
        
        result=subprocess.run(["pip","install","pandas"],shell=True,check=True,capture_output=True,text=True)
    except subprocess.CalledProcessError as e:
        print(f'error to install pandas {e}')

#install Flask
def install_flask():
    try:
        result=subprocess.run(["pip","install","flask"],shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # Print the output of the installation command
        print("Flask installed successfully.")
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Failed to install Flask.")
        print(e.stderr.decode('utf-8'))

#install git using commend

def install_gitpython():
    try:
        print("******************Attempting to install GitPython...**************")
        result = subprocess.run(["powershell", "-Command", "pip install GitPython"], shell=True, check=True, timeout=240)
        print("************GitPython installed successfully.****************")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install GitPython: {e}")
        





import serial   # type: ignore
import serial.tools.list_ports as p # type: ignore
import subprocess  # for subprocess error handling

# Function to list available COM ports
def list_aviable_com_ports():
    ports_list = []
    try:
        ports = p.comports()
        for port in ports:
            ports_list.append(port.device)
            print(port)
        return ports_list
    except subprocess.SubprocessError as e:
        print(f"Error occurred while listing ports: {e}")
        return []

# Function to communicate through a serial port
def read_and_write_Serialport():
    # List all available ports first
    available_ports = list_aviable_com_ports()
    if not available_ports:
        print("No available COM ports found. Please check the connection.")
        return
    
    # Prompt user to select a port, or use the first available port automatically
    selected_port = available_ports[0]  # Automatically use the first available port

    try:
        # Try to open the selected serial port
        ser = serial.Serial(selected_port, 115200, timeout=2)
        print(f"Connected to {ser.port}")

        # Read and write data through the serial port
        count = 5
        while count > 0:
            ser.write("I am Sending a Message to Docklight".encode('utf-8'))
            response = ser.readline().decode('utf-8').strip()
            
            if response !="":
                print(f"Response from device: {response}")
                count -= 1

    except serial.SerialException as e:
        print(f"Failed to open the serial port {selected_port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



#creating CSV file
data=[{"name":"arun","roll":"5b3","phoneNUmber":7989759695},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300},{"name":"kiran","roll":"5A3","phoneNUmber":9951686300}]

def creating_CSV_File():
    try:
        
        with open(r"C:\Users\aruns\Desktop\allinonefunctions\allprogramcsv.csv","w") as csvfile:
            
            fieldnames=["name","roll","phoneNUmber"]
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Data Written Sucessfully")
    except Exception as e:
        print(f'a arror occured {e}')



# Get user input and convert it to bytes
n = input("Enter a string or number to calculate CRC: ")
#Cycle Redundancy Check
def calculate_crc16(data: bytes) -> int:
    # Convert user input to bytes
    """
    Calculate the CRC-16 checksum of a data input.
    This uses the CRC-16-IBM/Modbus polynomial: 0x8005.

    Args:
        data (bytes): The data for which to calculate the CRC.

    Returns:
        int: The calculated 16-bit CRC value.
    """
    # Define the CRC-16-IBM polynomial and initial value
    poly = 0xA001  # CRC-16-IBM reverse polynomial 0x8005 (reflected)
    crc = 0xFFFF  # Initial CRC value

    # Iterate over each byte in the input data
    for byte in data:
        crc ^= byte  # XOR byte with the current CRC
        for _ in range(8):  # Perform 8 shifts
            if crc & 0x0001:  # Check if the rightmost bit is set
                crc = (crc >> 1) ^ poly  # Right shift and XOR with polynomial
            else:
                crc >>= 1  # Right shift without XOR

    return crc & 0xFFFF  # Ensure the result is 16-bit
   
data_bytes = n.encode('utf-8')   # Convert string to bytes using utf-8 encoding

#delete files in folder

def delete_all_files_in_folder():
    #iam using shutil becouse its manuplicate the system to delete in side folders
    try:
        import shutil
        path=r"C:\Users\aruns\Desktop\vaddi"
        shutil.rmtree(path)
    except Exception as e:
        print(f"error Occured {e}")
        
   
#open Any App Automatically

def auto_open_apps():
    import subprocess
    subprocess.call(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


# #Create_APi_using_python


# app = Flask(__name__)

# # Store the data in memory (in a dictionary or a list)
# data_store = []

# # Define a route to accept POST requests and add data to the store
# @app.route('/', methods=['POST'])
# def add_data():
#     # Get the JSON data from the POST request
    
#     new_data = request.json
    
#     # Append the new data to the data store
#     data_store.append(new_data)
    
    
#     # Return a response indicating the data was added
#     return jsonify({'message': 'Data added successfully', 'data': new_data}), 201

# # Define a route to view the stored data
# @app.route('/', methods=['GET'])
# def view_data():
#     # Return the stored data as a JSON response
#     return jsonify(data_store), 200

# Define a home route
# @app.route('/')
# def home():
#     print("Welcome to the Flask API. Use /add_data to POST data and /view_data to GET data.")


 #post data to give end point api 
def post_api():
    
    import requests
    from datetime import datetime

    # Define the URL to which the request will be sent  the above create api is commented becouse it can done in single open terminal we can open another terminal for creating api
    url = 'https://jsonplaceholder.typicode.com/posts'
    # Generate current date in the desired format
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the data to be sent (usually as a dictionary)
    data = { "Device_id":"899999999",
    "session_key":"ahvggjhsvdhgavsjgavsj",
    "imei":"-8907087969",
    "Product_code":"768guugvguv",
    "timestamp":current_date}

    try:
        # Send a POST request with the data as JSON
        response = requests.post(url, json=data)

        # Check the status of the request
        if response.status_code == 201:
            print('Data sent successfully:', response.status_code,response.json())
        else:
            print(f'Failed to send data: Status Code {response.status_code}')
            print('Response Text:', response.text)
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)

#git CLone Process Starts Here
import os
import shutil
from git import Repo, GitCommandError

# Define the path to the directory where the repository will be cloned
inputfile_path = r'C:\Users\aruns\Desktop\gitpath'
git_user_name = ""
commit_id = ""

# Function to get the Git username and commit ID from the user
def fetch_git_username_and_commit_id():
    global git_user_name
    global commit_id

    # Keep asking for the username until a non-empty string is entered
    while not git_user_name:
        git_user_name = input("Enter a Bitbucket Username: ")

    # Keep asking for the commit ID until a non-empty string is entered
    while not commit_id:
        commit_id = input("Enter a Commit ID: ")

# Custom error handler to change file permissions and retry removal
def on_rm_error(func, path, exc_info):
    # This function will be called if shutil.rmtree encounters an error
    import stat  # Import the stat module for file permission operations
    os.chmod(path, stat.S_IWRITE)  # Set the file to writable
    try:
        func(path)  # Retry the removal
    except Exception as e:
        print(f"Failed to remove {path}: {e}")

# Function to remove all contents of the directory
def remove_all_contents():
    directory = os.path.join(inputfile_path, "firmware")  # Correctly join path components

    # If the directory doesn't exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        # If the directory exists, remove all its contents
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                # Set permissions to writable before attempting to delete
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path, onerror=on_rm_error)  # Remove directory and its contents with custom error handler
                else:
                    os.chmod(item_path, 0o777)  # Set the file to be writable
                    os.remove(item_path)  # Remove file
                print(f"Removed successfully: {item_path}")
            except Exception as e:
                print(f"Error removing {item_path}: {e}")

# Function to clone the repository and check out a specific commit
def clone_repository_and_checkout():
    global git_user_name, commit_id

    repo_url = f"http://{git_user_name}@bitbucket.org/gndsolutions/iot_card_ccd.git"
    local_dir = os.path.join(inputfile_path,'firmware')  # Correctly join path components

    # Remove all contents of the directory before cloning
    remove_all_contents()

    try:
        # Clone the repository into the specified local directory
        repo = Repo.clone_from(repo_url, local_dir)
        print(f"Cloned repository into {local_dir}")

        # Attempt to check out the specified commit ID
        repo.git.checkout(commit_id)
        print("Checkout successful!")
    except GitCommandError as git_error:
        print(f"Git command error: {git_error}")
        # Provide specific error messages based on common issues
        if "128" in str(git_error):
            print("Exit code 128 indicates a problem with the repository, path, or credentials.")
        if "authentication" in str(git_error).lower():
            print("Check if your username and credentials are correct.")
    except Exception as e:
        print(f"Error during clone or checkout: {e}")



    


if __name__=="__main__":
    print('********************* Welocme to Python Script for Automation*********************')

    print('********************* Installing Required Dependencies*********************')
    check_python_version()
    update_version()
    install_pyserial()
    install_sys()
    install_serial_tools()
    install_csv()
    install_pytz_and_time()
    install_pyvisa()
    install_pandas()
    install_gitpython()
    print("*******************AvaliblePorts*********************")
    list_aviable_com_ports()
    print("****************Getting Response From ComPort****************************")
    read_and_write_Serialport()
    print("Creating CSV FIle and Writing Some Data")
    creating_CSV_File()
    print("**********printing CRC VALUE***********************")
    # Calculate the CRC value
    crc_value = calculate_crc16(data_bytes)
    print(f"CRC-16 value: {crc_value:04X}")
    print("*********************DELETED HIDDEN FILES IN FOLDER*******************************")
    delete_all_files_in_folder()       
    # app.run(debug=True)
    #send data to api using end point
    post_api()
    print("**************auto Opens Chrome App****************")
    auto_open_apps()
    print("**************Git-Clone******************")
    # Execute the script
    fetch_git_username_and_commit_id()
    clone_repository_and_checkout()
    
    