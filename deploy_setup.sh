source ./venv/bin/activation
cd frontend
npm install && npm run build
cd ..
rm -r staticfiles
python3 manage.py collectstatic
git add .
git commit -m "added greetingkiosk.herokuapp.com to allowed_hosts"
git push heroku deploy_to_heroku:main
heroku open