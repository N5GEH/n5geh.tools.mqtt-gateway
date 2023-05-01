# IoT Gateway

## Overview
This is a project for my Bachelor's thesis. It is a simple software-based IoT Gateway that allows to control devices connected to it via a web interface. The gateway is written in Python and uses the [FastAPI](https://fastapi.tiangolo.com/) framework. The frontend is written in [Svelte](https://svelte.dev/).


## Installation
### Backend
The backend is written in Python 3.10. It uses the [FastAPI](https://fastapi.tiangolo.com/) framework and the [uvicorn](https://www.uvicorn.org/) server. The easiest way to install the backend is to use pip. A Dockerfile is in the works.

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# runs in port 8000
```

### Frontend
The frontend is written in [Svelte](https://svelte.dev/). It uses [Rollup](https://rollupjs.org/guide/en/) as a bundler. The easiest way to install the frontend is to use [npm](https://www.npmjs.com/). A Dockerfile is equally in the works.

```bash
cd frontend
npm install
npm run dev
# runs in port 5173
```



## Preview
![Frontend](frontend/preview/preview_v0.1.png)