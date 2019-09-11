import socket
import datetime
import sys
import os

HOST = '0.0.0.0'

def get_port():
    PORT = int(sys.argv[1])
    if PORT < 1024 or PORT > 64000:
        sys.exit("ERROR: PORT NUMBER MUST BE BETWEEN 1024 AND 64000 (INCLUSIVE)")
    else:
        print('PORT IS VALID') #just to check
        return PORT

def create_and_bind(PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
    except Exception as e:
        print("Error {}".format(e))
        sys.exit("ERROR: SOCKET CREATION IS BAD")
    print("CREATE AND BIND SUCCESS") #just to check
    return s

def listen(s):
    try:
        s.listen()
    except socket.error:
        s.close()
        sys.exit("ERROR: LISTENING FAILURE")
    print("LISTENING...")  #just to check
    
    while True:
        connection_socket, address = s.accept()
        now = datetime.datetime.now()
        print(now.strftime("Time: %H:%M:%S")) #current time
        ip_address, port_number = address
        print('Connected by IP adress:{} and Port number:{}'.format(ip_address, port_number))
        
        #=========READ FIXED HEADER==============
        connection_socket.settimeout(1)
        try:
            data = connection_socket.recv(5)
        except socket.timeout:
            print("ERROR: CONNECTION TIMEOUT. RESTARTING LOOP")
            connection_socket.close()
            continue #goes back to the start of the loop
        
        #==============VALIDATING DATA============
        
        MagicNo = data[0] << 8 | data[1]
        Type = data[2]
        FilenameLen = data[3] << 8 | data[4]
        if MagicNo == 0x497E and Type == 1 and FilenameLen > 1 and FilenameLen < 1024:
            print("CONDITIONS ARE CORRECT")
            pass
        else:
            print("ERROR: FILE REQUEST IS ERRONEOUS")
            connection_socket.close()
            continue

        #========READING MORE BYTES FOR FILENAME============
        
        connection_socket.settimeout(1)
        try:
            filename_data = connection_socket.recv(FilenameLen)
        except socket.timeout:
            print("ERROR: CONNECTION TIMEOUT. RESTARTING LOOP")
            connection_socket.close()
            continue #goes back to the start of the loop
        
        #======OPEN FILE FOR READING===========
        requested_filename = filename_data.decode('utf-8')
        
        try:
            f = open(requested_filename, 'rb') #rb means to 'read bytes'
            print("FILE EXISTS AND CAN BE OPENED") #just to check
            
            MagicNo_Response = (0x497E).to_bytes(2, byteorder='big') 
            Type_Response = (2).to_bytes(1, byteorder='big')
            StatusCode = (1).to_bytes(1, byteorder='big')
            
            cwd = os.getcwd()
            DataLength = os.path.getsize(cwd + '/' + str(requested_filename))
            DataLength = DataLength.to_bytes(4, byteorder='big')
            
            header = bytearray(MagicNo_Response + Type_Response + StatusCode + DataLength)
            connection_socket.send(header)
            DataLength_sent = 0
            
        except IOError:
            MagicNo_Response = (0x497E).to_bytes(2, byteorder='big') 
            Type_Response = (2).to_bytes(1, byteorder='big')
            StatusCode = (0).to_bytes(1, byteorder='big')            
            DataLength = (0).to_bytes(0, byteorder='big')
            # StatusCode is 0 so FileData field contains no bytes.
            
            header = bytearray(MagicNo_Response + Type_Response + StatusCode + DataLength)
            connection_socket.send(header)            
            
            print("ERROR: FILE DOES NOT EXIST OR CANNOT BE OPENED")
            connection_socket.close()
            continue
        
        while True:
            f_data = f.read(4096)
            connection_socket.send(f_data)
            if len(f_data) == 0:
                break
            DataLength_sent += len(f_data)
        print("THE NUMBER OF BYTES TRANSFERED IS: {}".format(DataLength_sent))
        connection_socket.close()
        continue        
        
  
def main():
    port = get_port()
    s = create_and_bind(port)
    listen(s)
    

main()