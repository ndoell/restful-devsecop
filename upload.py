from bottle import post, get, run, response, request
import os
import uuid

save_path = "uploaded_files"

@post('/post_upload')
def do_upload():
    response.content_type = 'application/json'
    file = request.json['file']
    print(file)

@post('/upload')
def do_upload():
    file = request.files.get('file')
    print(file.filename)
    name, ext = os.path.splitext(file.filename) 
    
    if ext not in ('.txt'):
        return "File extenstion not allowed."

    #Create a unique scan file using uuid to save.
    uniqfile = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext='.scan')
    print(uniqfile)


    #When scan begings we will need a status for the client. <uuid.status>
    name, ext = os.path.splitext(uniqfile)
    statusfile = '{uuid}{ext}'.format(uuid=name, ext='.status')
    print(statusfile)
    status_file = open(save_path+ "/" +statusfile, "w")
    status_file.write("Starting Scan")
    status_file.close()

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file.save(save_path+ "/" +uniqfile, overwrite=True)
    return 'OK'

run(host='localhost', port=8080, debug=True)
