# streamlit
How to on using streamlit with python

This tutorial uses Docker, but if you don't like docker you can run the python directly using the command 
in the Dockerfile

docker build -t strealit:test -f Dockerfile .
docker run -it --network host strealit:test bash

then check http://localhost:8501