# Introduction
## Install Library
``` bash
uv add google-api-python-client
```

# Read Folder
## Check Connection
Authentication
```bash
# Login with Service Account and required scopes
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/cloud-platform
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
