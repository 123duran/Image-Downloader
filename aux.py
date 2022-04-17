from __future__ import print_function
from fileinput import filename

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload


def get_drive():
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    return DRIVE

def createRemoteFolder(folderName, parentID = None ):
    DRIVE = get_drive()
    # Create a folder on Drive, returns the newely created folders ID
    body = {
        'name': folderName,
        'mimeType': "application/vnd.google-apps.folder"
    }
    if parentID:
        body['parents'] = [{'id': parentID}]
    root_folder = DRIVE.files().create(body = body).execute()
    return root_folder['id']

def upload_photo(path, file_name ,parent_folder):
    DRIVE = get_drive()
    full_path = f"img/{path}/{file_name}"
    file_metadata = {'name': file_name, 'parents': [parent_folder]}
    media = MediaFileUpload(full_path,
                            mimetype='image/jpg')
    file = DRIVE.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return file.get('id')


