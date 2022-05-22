
------------------------------------------------------------------------------------------------------------------
ALL THESE COMMANDS TO BE RUN IN CMD.

RUN ALL SQL FILES IN "bin" FOLDER IN "POSTGRES" FOLDER (where postgres is installed).

RUN ALL PYTHON FILES WHERE THAT python FILE IS PRESENT.

RUN THEM ALL IN ORDER YA GUYS
-------------------------------------------------------------------------------------------------------------------

psql -U postgres -f "C:\Users\Sravya Yepuri\Desktop\PESUVariance\Assignment2\final\pesuvariance_create.sql"

python user.py

Python dataset.py

psql -U postgres -f "C:\Users\Sravya Yepuri\Desktop\PESUVariance\Assignment2\final\pesuvariance_insert.sql"

python c_images.py

python p_images.py

python user_retr.py