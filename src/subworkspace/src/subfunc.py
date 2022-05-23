import os

def cetak_from_subworkspace():
    print('cetak_from_SUBworkspace')

def call_from_subfunc():
    print('call_from_subfunc')

def readjs_from_subfunc():
    path_from_this_file = '../tmp/obj.json'
    path = os.path.join( os.path.dirname(__file__), path_from_this_file )
    with open(path, 'r') as f:
        data = f.read()
        print(data)