# Basic Notes on Automation Scripts in Python ( 8 marks )

Automation scripts are used to automate repetitive tasks, making processes more efficient and less error-prone. Python is a popular language for writing automation scripts due to its simplicity and the availability of powerful libraries.

## Key Points

1. **Definition**:
   - Automation scripts are programs written to perform tasks automatically without manual intervention.
   - They can handle a wide range of tasks, such as file management, web scraping, data processing, and more.

2. **Common Libraries**:
   - **os**: Interact with the operating system, handle file operations.

     ```python
     import os
     os.rename('old_name.txt', 'new_name.txt')
     ```

   - **shutil**: High-level file operations, like copying and removing files.

     ```python
     import shutil
     shutil.copy('source.txt', 'destination.txt')
     ```

   - **subprocess**: Execute shell commands and scripts.

     ```python
     import subprocess
     subprocess.run(['ls', '-l'])
     ```

   - **requests**: Send HTTP requests to interact with web services and APIs.

     ```python
     import requests
     response = requests.get('https://api.example.com/data')
     ```

   - **selenium**: Automate web browsers for tasks like form submission and web scraping.

     ```python
     from selenium import webdriver
     driver = webdriver.Chrome()
     driver.get('https://example.com')
     ```

   - **time**: Add delays in your script.

     ```python
     import time
     time.sleep(5)
     ```

4. **Best Practices**:
   - **Error Handling**: Use try-except blocks to handle potential errors.
   - **Logging**: Implement logging to keep track of script execution and errors.
   - **Modularity**: Break down the script into functions for better readability and maintenance.
   - **Testing**: Test the script thoroughly in a controlled environment before deploying.

5. **Common Applications**:
   - **File Management**: Organizing, renaming, copying, and deleting files.
   - **Web Scraping**: Extracting data from websites.
   - **Data Processing**: Manipulating and analyzing data.
   - **Task Scheduling**: Automating tasks at specific intervals using schedulers like `cron` or `Task Scheduler`.

Automation scripts can significantly improve efficiency by reducing manual effort and ensuring consistency in repetitive tasks. Python's rich ecosystem of libraries makes it an ideal choice for writing automation scripts.
