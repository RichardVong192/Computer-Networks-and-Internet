import socket
import datetime
import sys
import os
from os import path

def less_than_three():
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        sys.exit("ERROR: LESS OR MORE THAN THREE PARAMETERS")
    else:
        pass
    
def get_ip():
    address = str(sys.argv[1])
    try:
        ip_address = socket.gethostbyname(address)
    except socket.gaierror:
        sys.exit("ERROR: HOST NAME DOES NOT EXIST OR IP IS NOT WELL-FORMATTED")
    print("IP IS VALID") #just to check
    return address

def get_port():
    port = int(sys.argv[2])
    if port < 1024 or port > 64000:
        sys.exit("ERROR: PORT NUMBER MUST BE BETWEEN 1024 AND 64000 (INCLUSIVE)")
    else:
        print("PORT IS VALID") #just to check
    return port

def name_of_file():
    filename = str(sys.argv[3])
    if path.exists(filename):
        sys.exit("ERROR: FILE ALREADY EXISTS LOCALLY")
    else:
        print("FILE DOES NOT EXIST") #just to check
        return filename

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INT is adress for IPV4, #SOCK_STREAM is socket type for TCP
    except socket.error:
        sys.exit("ERROR: FAILED TO CREATE SOCKET")
    print("SOCKET CREATION SUCCESS") #just to check
    return s

def connect(s, HOST, PORT):
    try:
        s.connect((HOST, PORT))
    except socket.error:
        s.close()
        sys.exit("ERROR: CONNECT FAILURE")
    print("CONNECTION SUCCESS") #just to check

def file_request(filename):
    file = bytearray()
    MagicNo = (0x497E).to_bytes(2, byteorder='big') #equivalent to 0x497E
    Type = (1).to_bytes(1, byteorder='big')
    FilenameLen = (len(filename)).to_bytes(2, byteorder='big')
    Encoded_filename = filename.encode('utf-8') #returns utf-8 encoded version of the string
    
    return bytearray(MagicNo + Type + FilenameLen + Encoded_filename)

def recieve_data(s):
    recieved_data = s.recv(4096)
    return recieved_data

def read_fixed_header(s, filename):
    s.settimeout(1)
    try:
        data = s.recv(8)
    except socket.timeout:
        print("ERROR: CONNECTION TIMEOUT")
        s.close()
        sys.exit()
    
    MagicNo = (int).from_bytes(data[0:2], "big")
    Type = data[2]
    StatusCode = data[3]
    DataLength = (int).from_bytes(data[4:], "big")
    
    FixedHeader = MagicNo + Type + StatusCode + DataLength
    
    if MagicNo == 0x497E and Type == 2 and (StatusCode == 1 or StatusCode == 0):
        print("CONDITIONS ARE CORRECT")
        pass
    else:
        print("ERROR: FILE REQUEST IS ERRONEOUS")
        s.close()
    
    if StatusCode == 0:
        print("ERROR: FILE DOES NOT EXIST ON SERVER SIDE")
        s.close()
        sys.exit()
    else:
        try:
            f = open(filename, "wb+") # wb+  =  create write bytes
        except IOError:
            print("ERROR: FILE CANNOT BE OPENED FOR WRITING")
            s.close()
            sys.exit()
        
        DataLength_recieved = 0 #initialise
        while True:
            try:
                f_data = s.recv(4096) #buffer
            except IOError:
                print("ERROR: FIXED HEADER IS ERRONEOUS, CONNECTION TIMEOUT")
                s.close()
                f.close()
                sys.exit()
            except socket.error:
                print("ERROR: FILE DATA CANNOT BE RECIEVED FROM SERVER")
                s.close()
                f.close()
                sys.exit()                 
            byte_array = bytearray(f_data)
            try:
                f.write(f_data)
            except IOError:
                print("ERROR WRITING TO FILE")
                s.close()
                f.close()
                sys.exit()
            if not f_data:
                break
            DataLength_recieved += len(f_data)
        if DataLength_recieved != DataLength:
            print("ERROR: DATA BYTES VALID")
            s.close()
            sys.exit()
            
        print("FILE RECIEVED")
        print("THE NUMBER OF BYTES RECIEVED IS: {}".format(DataLength_recieved))
        f.close()
        sys.exit()

    
def main():
    less_than_three()
    address = get_ip()
    port = get_port()
    filename = name_of_file()
    s = create_socket()
    connect(s, address, port)
    fileRequest = file_request(filename)
    s.sendall(fileRequest)
    read_fixed_header(s, filename)
    recieve_data(s)
    
main()