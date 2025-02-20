{
    "name": "PyCharm Debug Server",
    "summary": "Debug with PyCharm using the 'Python Debug Server' configuration",
    "version": "16.0.0.0.2",
    "category": "Extra Tools",
    "images": [ "static/description/banner.png" ],
    "website": "https://angelvil.dev",
    "author": "Angel Vilaplana",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": ["pydevd-pycharm"]
    },
    "depends": [
        "base",
    ],
    "post_load": "post_load"
}
