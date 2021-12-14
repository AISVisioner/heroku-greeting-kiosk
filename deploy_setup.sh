#!/bin/bash
source ./venv/bin/activate
cd frontend
npm install && npm run build
cd ..
rm -r staticfiles
python3 manage.py collectstatic
git add .
git commit -m "changed webpack path from static/dist/ to static/"
git push heroku deploy_to_heroku:main
heroku open