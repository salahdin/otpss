# online test paper sharing platform
## objectives 
- Allow sharing of past test papers in image (jpg, png) or text format (pdf, Docx, etc).
- To allow users to search test papers by the content.
- Index questions from image files using OCR technology
- Allow users to provide a solution to individual questions via text or pictures 
- Allow users to upvote test papers and answers 
- Sort test papers and answers based on the number of votes

### installation
  ```shell
   pip install requirments.txt
  ```
 change databases in setting to or install postgres db
 ```python
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
 ```
 next
 ```shell
 cd optss
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 ```

