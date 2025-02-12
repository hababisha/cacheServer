import socket
from urllib.request import Request, urlopen, HTTPError
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('port')
    args = parser.parse_args()

    SOCKET_HOST = '0.0.0.0'
    SOCKET_PORT = int(args.port)

    server_host = socket.socket(socker.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    server.socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(1)

    print("cache proxy is listening on port %s...." %SERVER_PORT)

    while True:
        client_connection, client_address = server_socket.accept()

        request = client_connection.recv(1024).decode()
        print(request)

        headers = request.split("\n")
        top_header = headers[0].split()
        method = top_header[0]
        filename = top_header[1]

        if filename == '/':
            filename = '/index.html'

        content = fetch_file(filename)

        if content:
            response = 'HTTP/1.0 200 OK \n\n' + content
        else:
            response = 'HTTP/1.0 404 NOT FOUND\n\n File not found'
        
        client_connection.sendall(response.encode())
        client_connection.close()
    
    server_socket.close()


def fetch_file(filename):
    file_from_cache = fetch_from_cache(filename)

    if file_from_cache:
        print('Fetched Successfully from cache.')
        return file_from_cache
    else:
        print('Not in cache. Fetching from server')

        file_from_server = fetch_from_server(filename)

        if file_from_server:
            save_in_cache(filename, file_from_server)
            return file_from_server
        else:
            return None
'''
since above on the main function it's checking on the return value from this function
to decide if we return a 200 or 404, returning None from this function will correctly 
return a 404 to the client.
'''

def fetch_from_cache(filename):
    try:
        fin = open('cache' + filename)
        content = fin.read()
        fin.close()
        return content
    except IOError:
        return None
    
def fetch_from_server(filename):
    url = 'http://127.0.0.1:8000' + filename
    q  = Request(url)

    try:
        response = urlopen(q)
        response_headers = response.info()
        content = response.read().decode('utf-8')
        return content
    except HTTPError:
        return None
    
def save_in_cache(filename, content):
    print("saving a copy of {} in the cache".format(filename))
    cached_file = open('cache' + filename, 'w')
    cached_file.write(content)
    cached_file.close()