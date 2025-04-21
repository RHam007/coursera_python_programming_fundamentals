import onedrivesdk #depending on version of OneDrive SDK installed, you may need to use pip install onedrivesdk_fork in the terminal

# Replace with real key. API Key provided by Azure/OneDrive Developer account
API_KEY = 'Your API key'

client = onedrivesdk.get_default_client(client_id=API_KEY)
client.auth_provider.authenticate()

"""
Uploads a file to a specific folder in OneDrive.  Args:
file_path: Path of file to upload
folder_id: The ID of target folder on OneDrive
"""
def upload_file(file_path, folder_id):
    try:
        item = client.item(drive='me', id=folder_id).children[file_path].upload(file_path)
        print(f"File '{file_path}' upload successfully to folder ID '{folder_id}'")
    except Exception as e:
        print(f"Error uploading file: {e}")


# Replace with actual file information
file_path = 'path/to/your/file.txt'
folder_id = 'Your_Folder_ID'
upload_file(file_path, folder_id)