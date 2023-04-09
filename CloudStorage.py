import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJ4y_BbIWTxJs-X3gKcIfjTAZwPyQgQK1Uy8gmvig5cLy9bSIqIDz3siexWOnnT2r0E_yOiQT8EolL2inRX2q5nkt1tlxKKleHRrBfTg7x91mEqxLl-RX23PvBF9UpNS6UrusB8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : ")
    file_to = input("Enter the full path to upload to Dropbox : ")
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

main()