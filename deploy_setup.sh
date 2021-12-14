#!/bin/bash
source ./venv/bin/activate
cd frontend
npm install && npm run build
cd ..
rm -r staticfiles
python3 manage.py collectstatic
git add .
git commit -m "imported dj_database_url in django settings"
git push heroku deploy_to_heroku:main
heroku open