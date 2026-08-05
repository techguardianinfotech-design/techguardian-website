from flask import Flask, Response
from .config import Config
import os

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "..", "templates"),
        static_folder=os.path.join(base_dir, "..", "static"),
    )

    app.config.from_object(Config)

    from .routes import main
    app.register_blueprint(main)

    @app.route('/sitemap.xml')
    def sitemap():
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.techguardianinfotech.com/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.techguardianinfotech.com/services</loc>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://www.techguardianinfotech.com/website-development</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.techguardianinfotech.com/custom-software</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.techguardianinfotech.com/cloud-solutions</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.techguardianinfotech.com/digital-security</loc>
    <priority>0.8</priority>
  </url>
</urlset>'''
        return Response(xml, mimetype='application/xml')

    return app
