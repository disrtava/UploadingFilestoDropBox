import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadingFiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_to, 'rb') as a:
            dbx.files_upload(a.read(),file_to) 

def main():
    access_token = 'sl.BH3jyEJaAwTLjDzi6LU_zV6y1r4nslhqZgds5MkG6KpelzSfQ8rcBr4WGuNxP1GUzH6Tyc5wq6QSideAw_8xQup743GKvr4itxqEJblvGiK06ii5r8ecQ7cEXU3K32jV349CmPE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file you want to upload")
    file_to = input("Enter the full path to enter the dropbox")

    transferData.uploadingFiles(file_from,file_to)

if __name__ == '__main__' :
    main()