cd frontend
npm run build
cd ..
rm -r staticfiles
python3 manage.py collectstatic
git add .
git commit -m "improved the manager page and several errors"
git push heroku deploy_to_heroku:main
heroku open