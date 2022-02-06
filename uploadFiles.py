from shutil import move
from unicodedata import name
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BBblYNTL7cymGmTCYAlk3zSeIcltJ436HB3q-JC9OKP1mxxRptUYTpU-j7w1TDDZjiigrTnj-nsgS1Q4PXFK4FrJtR6oy42POZM6KuwJrzUwzz_o9KUVUrxUCDwSPvXrD3IApBRiuze9'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to the dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved!")

main()