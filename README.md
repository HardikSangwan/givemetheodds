# givemetheodds
 Path Finding Problem (Interview Assessment). Python BackEnd Vue FrontEnd.


<img src="https://raw.githubusercontent.com/HardikSangwan/givemetheodds/main/backend/resources/Frontend_Screenshot.jpg">


<ins>On the Backend:</ins>

cd backend

pip install -r requirements.txt

python odds_backend.py examples/example1/millennium-falcon.json

The command initializes the millennium-falcon data and then starts up the API Server

- Pathfinding using networkx
- API using FastAPI, uvicorn
- Database connection through sqlite3
- Some basic data operations using pandas and json and math libraries
- CLI using Typer

- For a command line interface, run the script or the executable


python givemetheodds.py examples/example1/millennium-falcon.json examples/example1/empire.json

./givemetheodds example1/millennium-falcon.json example1/empire.json

<ins>On the Frontend:</ins>

cd frontend

npm install

npm run serve

- moving stars implemented by following this article: https://betterprogramming.pub/fun-with-html-canvas-lets-create-a-star-field-a46b0fed5002

- Logo Image/font from https://www.dafont.com/mandalore.font

- Giskard favicon from giskard