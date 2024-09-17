from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user-input']

        # Store the input in a file
        with open('user_input.txt', 'a') as file:
            file.write(user_input + '\n')

        return redirect(url_for('index'))  # Redirect to the form page after submission

    return '''
        <form method="post">
            <label for="user-input">Enter something:</label>
            <input type="text" id="user-input" name="user-input" required>
            <button type="submit">Submit</button>
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
