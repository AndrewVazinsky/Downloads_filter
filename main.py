from watchdog.observers import Observer
import os
import time
# FileSystemEventHandler - class for changes tracking
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        # sort through all the files in the folder_track folder
        for filename in os.listdir(folder_track):
            extension = filename.split('.')

            photos = ['jpeg', 'jpg', 'png']
            books = ['pdf', 'epub', 'txt']
            video = ['mkv', 'avi', 'mov', 'mp4']

            def rename(x):
                file = folder_track + '/' + filename
                new_path = folder_dest + x + filename
                os.rename(file, new_path)

            if len(extension) > 1 and extension[-1].lower() in photos:
                rename('/Photos')
            elif len(extension) > 1 and extension[-1].lower() in books:
                rename('/PDFs')
            elif len(extension) > 1 and extension[-1].lower() in video:
                rename('/Video')


folder_track = '/Full_destination_to_DOWNLOADS_folder'
folder_dest = '/Full_destination_to_FILTER_folder'

# Start tracking
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

# Checking every 10 ms
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
