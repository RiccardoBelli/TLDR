import base64
import os
import pickle
import quopri
from email.parser import BytesParser
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def create_gmail_api_client():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)


def download_emails_from_folder(folder_name):
    service = create_gmail_api_client()
    query = f'label:{folder_name}'
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    with open('emails.txt', 'w', encoding='utf-8') as file:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
            msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
            parsed_msg = BytesParser().parsebytes(msg_str)

            body = None

            if parsed_msg.is_multipart():
                for part in parsed_msg.walk():
                    if part.get_content_type() == 'text/plain':
                        try:
                            decoded_text = quopri.decodestring(part.get_payload()).decode(part.get_content_charset())
                        except ValueError:
                            decoded_text = part.get_payload()
                        body = decoded_text
                        break
            else:
                try:
                    decoded_text = quopri.decodestring(parsed_msg.get_payload()).decode(parsed_msg.get_content_charset())
                except ValueError:
                    decoded_text = parsed_msg.get_payload()
                body = decoded_text

            if body:
                file.write(f'---\nMessage ID: {message["id"]}\n{body}\n')


if __name__ == '__main__':
    folder_name = 'TLDR'
    download_emails_from_folder(folder_name)
