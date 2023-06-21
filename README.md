Ejercicio de fastapi con templates y bootstrap, del canal de OpenSessions:
https://youtu.be/wPJ7q2V4s3Y


Pasos para poder subirlo a AWS:

pip install mangum

in the main.py file add handler after app creation:

from mangum import Mangum

app=FastAPI()
handler=Mangum(app)

-------------
create folder 'dep' with modules inside:
pip install -t dep -r requirements.txt

create a zip file. It has the content of 'dep' folder, the main.py and the folders needed, for example:

cd dep; zip ../lambda_todo.zip -r . ; cd .. ;  zip -u lambda_todo.zip main.py ;  zip -u -r lambda_todo.zip templates

---------------
Upload this file to lambda function

Be sure to enable "Function URL"
set it to NONE for authN for testing

change lambda handler to  'main.handler'