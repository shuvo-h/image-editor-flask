from src.modules.blueprints import version_one_blueprints



    # loop blueprintList and register with app
def register_blueprints(app):
    all_bluprints = [
        *version_one_blueprints.blueprint_list,         # spread version one bluprints
    ]

    for blueprint_info in all_bluprints:
        bluePrintInstance = blueprint_info['bluePrint']
        path = blueprint_info['path']
        app.register_blueprint(bluePrintInstance,url_prefix=path)
