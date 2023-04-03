## Giskard Assessment Files Setup

**Frontend: Vue**
**Backend: Python**

Load Docker Images from tar archives

```
docker --input demofrontend.tar
docker --input demobackend.tar
```

Run backend and frontend

```
docker run -p 8080:8080 demobackend
docker run -p 8081:8080 demofrontend
```

or

run givemetheodds cli

or 
uvicorn odds_backend_app reload
npm run serve

