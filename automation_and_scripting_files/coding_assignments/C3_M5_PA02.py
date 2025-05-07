"""
This is the final result of the final coding assignment for Automation and Scripting with Python course.  The content was downloaded with
permission for use as referal, and as a .py file.  If there is interest in the .jpynb (jupyter notebook), please let me know!

For this assignment, the code was originally compiled in a virtual machine using jupyter notebook, I've modified the content to remove
the jupyter markup, and to organize the content to better reflect "real" world formating.  I've kept the import order, with libraries
grouped by the order in which they were invoked in the assignment's prompts.

All included comments reflect the course prompts/instructions/comments (except where identified), and all code is my own (such as it is)
and formatted to meet the course's grader requirements (it was rather literal, and our code had to match expected input).
"""
# # Automation and scripting with Python
# In this lab, you will deepen your understanding of Python automation and scripting by integrating with an external API, automating data analysis and visualization tasks, and utilizing version control (Git) for efficient project management.

# ### Tips for completing this lab
# As you navigate this lab, keep the following tips in mind:
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task.
# - You can save your work manually by clicking the save button (floppy disk icon) on the menu bar at the top of the notebook.
# - You can also download your work locally by clicking File and then 'Download as' on the menu bar at the top of the notebook, and then specifying your preferred file format (e.g. Notebook (.ipynb)).
# 

# ## Scenario
# You are a Python developer tasked with gathering sports betting and baseball statistics. You will load a CSV file to a DataFrame, perform some analysis, and generate visualizations, as you have done in previous material. After the data is processed, you will set up SendGrid to send an email to your supervisor (using the sample code you've obtained from the SendGrid documentation). This is designed to send an alert once your analysis is done. You will add your API key and configure the message. 
# 
# You will add scheduling to a program so that the analysis is run every day and the automated email will be sent after completion of the analysis, and you will use file operations to save your DataFrame, ensuring you do not overwrite the previous set of data. As you do this, you will add logging messages where appropriate.
# 
# As you progress through this lab, you will use Git to manage your project and commit regularly.

# ## High-Level Tasks
# 1. **Set up Version Control** using Git.
# 2. **Data Handling and Preprocessing** of the sports dataset.
# 3. **Visualization Building and Evaluation** with Python libraries.
# 4. **API Integration and Error Handling** to set up alert emails and handle cases where the API integration fails.
# 5. **Scheduling** to automate sending an email on a schedule.
# 6. **File Operations  Logging** to save and rename files, and logging info-level messages.

# ### 1. Set Up Version Control
# #### Step 1.1: Initialize Git
# Initialize a local Git repository for this project where you can store versions of this notebook. This will allow you to track your progress, make commits, and revert changes when needed. 
# 
# You can download your work locally by clicking File and then 'Download as' on the menu bar at the top of the notebook, and then specifying your preferred file format (e.g. Notebook (.ipynb)).
# 
# If you have not already done so, you may also need to set up your Git environment by running:
# 
# git config --global user.email "you@example.com"
# 
# git config --global user.name "Your Name"

import pandas as pd

import matplotlib.pyplot as plt

import sendgrid
from sendgrid.helpers.mail import Mail
import logging

import schedule
import time

import os
import logging

# Load the dataset
df = pd.read_csv('sports_data_missing.csv')

# Display the first few rows
print(df.head())

# Check for missing values and data types
print(df.info())


# #### Step 2.2: Clean and Preprocess the Data
# Check for missing or invalid values, and clean the dataset as needed (e.g., fill missing values, handle data inconsistencies). In this case, drop any columns with invalid data.

# Drop rows with invalid data
df = df.dropna()

# Inspect the cleaned data
print(df.info())


# ### 3. Visualization Building and Evaluation
# #### Step 3.1: Create Functions for Visualizations
# Create a function to generate different visualizations based on the dataset. For example, scatter plots showing player statistics. Please note these abbreviations:
# - HR = Home Runs
# - BB = Walks (Base on Balls)
# - SO = Strikeouts
# - AB = At Bats
# 
# Some common examples of baseball metrics are a comparison of how many strikeouts (SO) vs. walks (BB), and number of at bats (AB) vs. home runs (HR). Create two scatter plots, one showing the Walk vs. Strikeout Ratio, and the second showing Home Runs vs. At Bats ratio.
# 
# Create a function called create_scatter_plot that accepts the dataframe, the x and y column names, and the chart title, and generates and displays a scatter plot.

# Function to create scatter plot
def create_scatter_plot(df, x_col, y_col, title):
    plt.figure(figsize = (10, 6))
    df.plot.scatter(x=x_col, y= y_col)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

# Example usage
create_scatter_plot(df, 'BB', 'SO', 'Walk (BB) vs Strikeout (SO) Ratio')
create_scatter_plot(df, 'HR', 'AB', 'Home Runs (HR) vs At Bats (AB) Ratio')


# #### Step 3.2:  Create a box plot
# Use Matplotlib to generate a box plot with singles, doubles, triples, and home runs. The X label should be Hits and the Y label should be Hit Type. The title should be Distribution of Hits.

# Create box plots using Matplotlib
plt.figure(figsize = (10, 6))

# Set up data to contain the Singles, Doubles, Triples, and Home Runs from the DataFrame "df"
data = df[['Singles', 'Doubles', 'Triples','HR']]

# Create the boxplot with specified options
plt.boxplot(data, vert=False, patch_artist=True)
plt.yticks(range(1, 5), ['Singles', 'Doubles', 'Triples', 'Home Runs'])
plt.xlabel('Hits')
plt.ylabel('Hit Type')
plt.title('Distribution of Hits')
plt.grid(True)
plt.show()


# #### Step 3.3:  Calculate averages and remove outliers
# Remove all players with 0 walks or 0 strikeouts, and create a new column "SO/BB" that calculates the strikeout to walk ratio. Calculate the mean singles, doubles, triples, home runs (HR), and the minimum and maximum strikeout-to-walk ratio (SO/BB) from the column created in this step.

# Remove players with 0 walks from DataFrame
df = df.drop(df[df['BB']==0].index)

# Remove players with 0 Strikeouts from DataFrame
df = df.drop(df[df['SO']==0].index)

# Create column with Strikeout/Walk Ratio %
df["SO/BB"] = df['SO'] / df['BB']

# Use DataFrame functionality to calculate the mean of the fields below
average_singles = df['Singles'].mean()
average_doubles = df['Doubles'].mean()
average_triples = df['Triples'].mean()
average_hr = df['HR'].mean()

# Use DataFrame functionality to calculate the max and min of the strikeout to walk ratio
max_SO_BB = df['SO/BB'].max()
min_SO_BB = df['SO/BB'].min()

# Checking Your Results:
print(f"Singles: {average_singles}")
print(f"Doubles: {average_doubles}")
print(f"Triples: {average_triples}")
print(f"Home Runs: {average_hr}")
print(f"Max SO/BB Ratio: {max_SO_BB}")
print(f"Min SO/BB Ratio: {min_SO_BB}")


# ### 4. API Integration and Error Handling
# Now that you have successfully set up your analysis, the next step you want to take is to email your supervisor when the analysis is complete. To do so, you have decided to use SendGrid to send the email. For now, we will use a non-functioning API key, but the steps to apply for a functional one are outlined in step 4.1.
# #### (optional) Step 4.1: Set Up SendGrid API Account
# 1. **Create a SendGrid Account:** Visit [SendGrid](https://sendgrid.com/) and create a free account by visiting the website and clicking Start for Free.
# 
# 2. **Obtain API Key:** After signing in, navigate to the API keys section in the dashboard and generate a new API key. Store this key in a secure place
# 
# #### Step 4.2: Install SendGrid library
# To ensure you have the required SendGrid library, enter the command: `pip install sendgrid`
# 
# As has been the case with other projects in the past, the installation only needs to be done once per machine.

#pip install sendgrid - commented out by me for this file


# #### Step 4.3 Use the SendGrid API to Send Alerts
# Once you have your SendGrid API key, integrate it into your Python script to send email alerts. Here, you will need to bring in your API key. You are using the basic email code snippet provided by SendGrid. The main things you will need to change are bringing in your API key and configuring the message. 
# 
# For the purposes of this exercise, you will be provided with a (non-functioning) SendGrid API key. In general, API keys are alphanumeric strings ranging from 20 to 128 characters and are case sensitive. The ones provided by SendGrid are 69 characters.
# 
# Assume for this exercise your API key is: `fake_api_key`
# 
# The email should have the following characteristics.
# - Your email: `admin@example.com`
# - Supervisor's email: `rshah@example.com`
# - Subject: `Analysis completed for today`
# - Message (plain text): `Baseball analysis is completed for today. Please view the statistics_CURRENT.csv to review details.`
# 
# Insert your API key in the code below, and adjust the code to set up the email message. You will schedule the email in a future step. Ensure the arguments in the mail generation are separated by commas.

# Set up SendGrid API credentials
SENDGRID_API_KEY = 'fake_api_key'

sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

message = Mail(
    from_email = 'admin@example.com',
    to_emails = 'rshah@example.com',
    subject = 'Analysis completed for today',
    plain_text_content = 'Baseball analysis is completed for today. Please view the statistics_CURRENT.csv to review details.'
)

# Checking Your Results


# #### Step 4.4: Log success or failure
# Now that you have set up the email using SendGrid, you want to send the message. SendGrid will respond with a successful status code or an exception. Here, add an logging info message saying `Email Sent Successfully` when the message is sent. If there is an exception, add a logging info message saying `Email Message Failure`.
# 
# Assume the logging library is imported and you can reference the method by using `logging.info`.
# 
# Given you are using a non-functioning API key, running this code should result in an failure message.

try:
    response = sg.send(message)
    logging.info('Email Sent Successfully')
    
except Exception as e:
    logging.info('Email Message Failure')

# Checking Your Results


# ### 5. Scheduling
# #### Step 5.1: Automate Tasks with a Schedule
# Use the `schedule` library to automate tasks like updating data, generating visualizations, and sending alerts. Assume you have an `email_message` function designed. Your task is to schedule the task to run every day at 9 AM. 

# pip install schedule - commented out by me for this file

# Mock function for emailing a message. Call this function using schedule below.
def email_message():
    pass

# Schedule the job to run every day at 9 AM
schedule.every().day.at('09:00').do(email_message)


# Checking Your Results


# ### 6. File Operations and Logging 
# Managing files on storage is important, whether it is in a database or in a file. In some cases, you may need to move files around. In your example, instead of overwriting a file, you will want to make a backup of the previous file. Here, you will want to keep two versions of your file, the current version and the previous version, and log any file operations.
# #### Step 6.1: Manipulate project files
# Your next task is to save your data and also log the results. Here is your plan.
# 1. You want to see if statistics_CURRENT.csv exists. If it does:
# 
#     a. If it exists, delete the file statistics_OLD.csv (and log an info message that you have done it)
#     
#     b. Rename statistics_CURRENT.CSV to statistics_OLD.csv (and log an info message that you have done it)
#     
#     
# 2. Convert the data frame to a CSV and save it as statistics_CURRENT.csv (and log an info message that you have done it).

# File names
current_file = 'statistics_CURRENT.csv'
old_file = 'statistics_OLD.csv'

# Check if the file exists
if os.path.exists('statistics_CURRENT.csv'):
    # Delete the old file
    if os.path.exists('statistics_OLD.csv'):
        os.remove('statistics_OLD.csv')
        print('Deleted old backup')
        
    # Rename the current file to old
    os.rename(current_file, old_file)
    print('Backed up current file')
    
# Save the DataFrame to the new CSV file
df.to_csv(current_file, index=False)
print('Statistics written to file')