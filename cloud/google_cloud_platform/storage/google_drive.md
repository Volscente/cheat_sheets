# Introduction
## Install Library
``` bash
uv add google-api-python-client
```

# Read Folder
## Check Connection
Authentication
```bash
# Login with Service Account and read
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/cloud-platform

# Loging with Service Account and full permissions
gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive
```

Use the following script
```python
from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Variables
scopes = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/cloud-platform']
creds = None

try:
    creds, project = default(scopes=scopes)
    print(f"Successfully loaded Application Default Credentials for project: {project}")
except Exception as e:
    print(f"Error loading Application Default Credentials: {e}")
    exit(1)

# Build the Drive API service
drive_service = build('drive', 'v3', credentials=creds)

# Try to retrieve the folder metadata with support for shared drives
try:
    folder = drive_service.files().get(
        fileId="1OQaTGfTw1v0ArVTrOLUe3vkBoFiauKNN",
        fields='id, name, mimeType, driveId',
        supportsAllDrives=True  # Shared drives
    ).execute()

    if folder['mimeType'] == 'application/vnd.google-apps.folder':
        print(f"✅ Access confirmed: Folder name is '{folder['name']}' in Shared Drive ID: {folder.get('driveId')}")
    else:
        print("⚠️ The provided ID does not correspond to a folder.")
except HttpError as e:
    if e.resp.status == 404:
        print("❌ Folder not found or you do not have access.")
    elif e.resp.status == 403:
        print("❌ Access forbidden. Check if your credentials have access to this Shared Drive.")
    else:
        print(f"❌ An error occurred: {e}")
```

## Fetch folder
```python
from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Variables
scopes = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/cloud-platform']
creds = None

try:
    creds, project = default(scopes=scopes)
    print(f"Successfully loaded Application Default Credentials for project: {project}")
except Exception as e:
    print(f"Error loading Application Default Credentials: {e}")
    exit(1)

# Build the Drive API service
drive_service = build('drive', 'v3', credentials=creds)

# Retrieve language folder IDs
response = drive_service.files().list(
    q=f"'{parent_folder_id}' in parents and name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
    fields="files(id, name)",
    supportsAllDrives=True,
    includeItemsFromAllDrives=True
).execute()

# Retrieve the files
files = response.get('files', [])
if not files:
    print(f"Folder '{folder_name}' not found in the parent folder.")
    continue
```

# Utils
## google_drive_utils.py
```python
"""
This module includes utils function for interacting with Google Drive
"""

# Import Standard Libraries
import logging
from typing import List
from google.auth import default
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def get_credentials(scopes: List[str], service_name: str, version: str) -> Resource:
    """
    Gets Resource builder for a Google Drive resource

    Args:
        scopes (List[str]): List of scopes
        service_name (str): Service name
        version (str): Service version

    Returns:
        (Resource): Resource builder for Google Drive
    """

    logging.debug("get_credentials - Start")

    # Authenticate and build service
    creds, _ = default(scopes=scopes)
    service = build(service_name, version, credentials=creds)

    logging.debug("get_credentials - End")

    return service


def duplicate_file(service: Resource, file_id: str, output_file_name: str) -> str:
    """
    Duplicate a file in Google Drive

    Args:
        service (Resource): Resource builder for Google Drive
        file_id (str): File ID
        output_file_name (str): Output file name

    Returns:
        (String): Duplicate file ID
    """
    logging.debug("duplicate_file - Start")

    # Initialise an empty copied file
    copied_file = None

    try:
        # Create a copy of the file in Google Drive
        copied_file = (
            service.files()
            .copy(fileId=file_id, body={"name": output_file_name}, supportsAllDrives=True)
            .execute()
        )

        logging.info(f"File copied successfully. New file ID: {copied_file.get('id')}")

    except HttpError as error:
        logging.error(f"An error occurred: {error}")

    logging.debug("duplicate_file - End")

    return copied_file.get("id")


def write_google_sheet(
    sheet_service: Resource, file_id: str, sheet_name: str, cell_content: dict
) -> None:
    """
    Write into a Google Sheet specific cell and sheet.

    Args:
        sheet_service (Resource): Resource builder for Google Sheet
        file_id (String): File ID
        sheet_name (String): Sheet name
        cell_content (dict): Cell content

    Returns:

    """
    logging.debug("write_google_sheet - Start")

    try:
        result = (
            sheet_service.spreadsheets()
            .values()
            .update(
                spreadsheetId=file_id,
                range=sheet_name,
                valueInputOption="USER_ENTERED",
                body=cell_content,
            )
            .execute()
        )

        print(f"{result.get('updatedCells')} cell(s) updated.")

    except HttpError as error:
        print(f"An error occurred: {error}")

    logging.debug("write_google_sheet - End")

```
## Usage
```python
# Get the Google Drive service builder
drive_service = get_credentials(
    scopes=["https://www.googleapis.com/auth/drive"],
    service_name="drive",
    version="v3"
)

# Create a copy of the template
template_id = duplicate_file(drive_service, source_file_id, output_file_name='duplicate_file')

# Get credentials for Spreadsheet service build
sheet_service = get_credentials(
    scopes=["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"],
    service_name="sheets",
    version="v4"
)

# Write the "List of Menus" sheet
cell_content = {
    "values": data.loc[:, ['global_entity_id', 'lead_id']].values.tolist()
}
write_google_sheet(
    sheet_service=sheet_service,
    file_id=template_id,
    sheet_name="'List of Menus - ! No Change !'!B3",
    cell_content=cell_content
)
```
