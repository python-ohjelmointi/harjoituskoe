def get_mime_type(filename: str) -> str:
    mime_types = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }
    
    if '.' in filename:
        extension = filename.split('.')[-1].lower()
        return mime_types.get(extension, 'application/octet-stream')
    else:
        return 'application/octet-stream'


if __name__ == "__main__":
    filename = input("File name: ")
    mime_type = get_mime_type(filename)
    print(mime_type)
