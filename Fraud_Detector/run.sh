docker build . -t myapp

docker run -it \
-v "$(pwd):/home/app" \
-p 8501:8501 \
-p 4000:4000 \
-e PORT=4000 myapp