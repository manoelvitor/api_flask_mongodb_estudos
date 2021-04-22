from src.server.instance import server
from src.controller.pessoa_controller import*

#blueprints
from src.controller.pessoa_controller import controller_bp
from src.data_base.db import data_base_bp
from src.model.pessoa import model_bp
from src.service.pessoa_service import service_bp
from src.server.instance import server_bp


server.app.register_blueprint(controller_bp)
server.app.register_blueprint(data_base_bp)
server.app.register_blueprint(model_bp)
server.app.register_blueprint(service_bp)
server.app.register_blueprint(server_bp)





server.run()