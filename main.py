import uvicorn

from applications import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080, access_log=False, debug=True)
