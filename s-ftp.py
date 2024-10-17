from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define the FTP server class
def start_ftp_server():
    # Create a dummy authorizer with user permissions
    authorizer = DummyAuthorizer()
    
    # Add a user with read and write permissions
    authorizer.add_user("user", "password", ".", perm="elradfmw")
    
    # Set up anonymous access (optional)
    # authorizer.add_anonymous("/path/to/anonymous/folder")

    # Create the FTP handler and attach the authorizer
    handler = FTPHandler
    handler.authorizer = authorizer
    
    # Create and start the FTP server on a specific address and port
    server = FTPServer(("0.0.0.0", 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()
