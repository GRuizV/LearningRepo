import json

path = r'C:\Users\USUARIO\GR\Software Development\Learning\Modules & Packages\Modules\JSON\json.json'


# with open(path, 'w') as f:

#     entry = {"contents": {"a": "a"}}    
#     json.dump(entry, f, indent=2)
#     f.close()



with open(path) as f:

    contents = json.load(f)

    # print(contents)
    # print(contents['contents']['a'])



with open(path, 'w') as f:

    contents['contents']['a'] = 'something'
    json.dump(contents,f,indent=2)
 


with open(path) as f:

    contents = json.load(f)

    print(contents)


