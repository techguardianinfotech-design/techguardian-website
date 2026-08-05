from flask import Response
from app import create_app

app = create_app()

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

if __name__ == "__main__":
    print("Starting TechGuardian Infotech server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
