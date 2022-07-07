from flask import Flask, send_from_directory
from flask_jasmine import Jasmine
from pathlib import Path

app = Flask('Jasmine-Flask-Tests')
app.config['DEBUG'] = True

static_folder = Path('.').resolve() / 'flask_jasmine' / 'static'

# This folder contains JavaScript sources that you want to test
src_folder = static_folder / 'jasmine' / 'src'
# This folder contains the tests
spec_folder = static_folder / 'jasmine' / 'spec'

@app.route('/static/src/<path:filename>')
def static_src(filename):
    return send_from_directory(src_folder, filename)

@app.route('/static/specs/<path:filename>')
def static_specs(filename):
    return send_from_directory(spec_folder, filename)

jasmine = Jasmine(app)

jasmine.sources(
    'src/Player.js',
    'src/Song.js'
)

jasmine.specs(
    'specs/SpecHelper.js',
    'specs/PlayerSpec.js'
)

if __name__ == '__main__':
    app.run()
