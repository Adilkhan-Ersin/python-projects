app1=(input('File Name:'))
app=app1.lower()
if '.gif' in app:
    print('image/gif')
elif '.jpg' in app:
    print('image/jpeg')
elif '.jpeg' in app:
    print('image/jpeg')
elif '.png' in app:
    print('image/png')
elif '.pdf' in app:
    print('application/pdf')
elif '.txt' in app:
    print('text/plain')
elif '.zip' in app:
    print('application/zip')
else:
    print('application/octet-stream')