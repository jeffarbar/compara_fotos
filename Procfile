heroku ps:scale web=1
web: uvicorn api:app --host=0.0.0.0 --port=${PORT:-5000}
