from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/madlib")
def madlib():
    answers = {
        'place': request.args['place'],
        'noun': request.args['noun'],
        'verb': request.args['verb'],
        'adjective': request.args['adjective'],
        'plural_noun': request.args['plural_noun']
    }
    result = story.generate(answers)
    return render_template('madlib.html', result=result)
# @app.route("/story")
# def show_story():
#     """Show story result."""

#     text = story.generate(request.args)

#     return render_template("story.html", text=text)

if __name__ == '__main__':
    app.run(debug=True)