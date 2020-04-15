from sys import argv
from threading import Thread
import os

if len(argv) > 3:
    FILE_PATH = argv[1]
    FILE_EXT  = argv[2]
    KEYWORD   = argv[3]
else:
    print('Usage: python path/to/script.py "path/to/directory"  "file extension (e.g. .json)" "keyword"')
    exit(0)


def findAllSubstrings(path, extension, keyword, lst):
    kwinstancesfound = lst
    folders = []
    
    for filename in os.listdir(path):
        fname = os.path.join(path, filename)
        
        if fname.lower().endswith(extension):            
            with open(f"{path}\\{filename}", 'r') as f:
                line = 1
                text = f.readline()
                while text:
                    if KEYWORD in text:
                        kwinstancesfound.append({f"{path}\\{filename} Line: {line}" : f"{text}"})

                    line += 1
                    text = f.readline()
                
        elif os.path.isdir(f"{path}\\{filename}"):
            print(f"found folder {filename}")
            folders.append(f"{path}\\{filename}")
        
    for folder in folders:
        findAllSubstrings(folder, extension, keyword, kwinstancesfound)

    return
        
if __name__ == "__main__":
    instances = []
    findAllSubstrings(FILE_PATH, FILE_EXT, KEYWORD, instances)
    
    for instance in instances:
        for key in instance:
            print(f"In {key}\n found keyword in text {instance[key]}")
            
        
