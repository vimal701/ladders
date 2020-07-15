from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

from temp_database import numbers_list


@app.route('/', methods=['GET','POST'])
def home():
	if request.method == 'POST':
		number = request.form['input_number']

		#code your logic here..if the number isn't in the range then simply skip otherwise append or whatever
		numbers_list.append(int(number)) # change this to whatever type you want
        
		return render_template('index.html',numbers_list=numbers_list)
	
	return render_template('index.html',numbers_list=numbers_list)



@app.route('/clear_list',methods=['GET','POSt'])
def clear_list():

	if request.method == 'GET':
		numbers_list.clear()
		return redirect(url_for('home'))
	else:
		return render_template('index.html',numbers_list=numbers_list)



if __name__ == '__main__':
	app.run(debug=True)