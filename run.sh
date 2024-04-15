docker run -it\
 -p 5000:5000\
 -v "$(pwd):/home/app"\
 -e PORT=5000\
myappbox python test.py