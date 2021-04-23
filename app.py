"""Main application file"""
2	from flask import Flask
3	app = Flask(__name__)
4	
5	@app.route('/<random_string>')
6	def returnBackwardsString(random_string):
7	    """Reverse and return the provided URI"""
8	    return "".join(reversed(random_string))
9	
10	if __name__ == '__main__':
11	    app.run(host='0.0.0.0', port=8080)
