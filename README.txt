chmod +x app/entrypoint.sh
chmod +x app/entrypoint.prod.sh

for Development

docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput


http://localhost:8000


for Production

docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

http://localhost:1337