from ftplib import FTP

def ftp_demo():
    ftp = FTP("ftp.dlptest.com")  # Public test FTP
    ftp.login(user="dlpuser", passwd="rNrKYTX9g7z3RgJRmxWuGHbeu")

    print("Directory listing:")
    ftp.retrlines("LIST")

    # Upload test.txt
    with open("test.txt", "w") as f:
        f.write("Hello FTP from CN Lab!")
    with open("test.txt", "rb") as f:
        ftp.storbinary("STOR test.txt", f)

    print("File uploaded successfully.")

    # Download
    with open("downloaded.txt", "wb") as f:
        ftp.retrbinary("RETR test.txt", f.write)
    print("File downloaded successfully.")

    ftp.quit()

ftp_demo()
