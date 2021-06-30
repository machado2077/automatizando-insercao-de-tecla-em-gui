from src.app import App
from src.adapters import listener_adapter, response_adapter

def create_app():
    app = App()
    response_adapter.plug_app(app)
    listener_adapter.plug_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()