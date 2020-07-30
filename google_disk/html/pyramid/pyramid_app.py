from flask import Flask, render_template, flash, request, jsonify, Markup
import matplotlib
import matplotlib.pyplot as plt
import io, os, base64
import numpy as np
import pandas as pd

# global variables
app = Flask(__name__)
pop_df = None
location_list = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

urldata="https://geografieliberec.cz/data/official/WPP2019_PopulationByAgeSex.csv"

@app.before_first_request
def startup():
	global pop_df, location_list

	# load and prepare the data
	#pop_df = pd.read_csv(BASE_DIR + '/WPP2019_PopulationByAgeSex.csv')
	pop_df = pd.read_csv(urldata)
	location_list = sorted(list(set(pop_df['Location'])))

def get_poulation_pyramid(country, year):
	pop_df_tmp = pop_df[(pop_df['Location']==country) & (pop_df['Time']==year)].copy()
	pop_df_tmp = pop_df_tmp.sort_values('AgeGrpStart',ascending=True)
	return(pop_df_tmp)

@app.route("/", methods=['POST', 'GET'])
def build_pyramid():
	plot_to_show = ''
	selected_country = ''
	country_list = ''
	selected_year = ''

	if request.method == 'POST':
		selected_country = request.form['selected_country']
		selected_year = int(request.form['selected_year'])

		pop_df_tmp = get_poulation_pyramid(selected_country, selected_year)

		y = range(0, len(pop_df_tmp))
		x_male = pop_df_tmp['PopMale']
		x_female = pop_df_tmp['PopFemale']

		# max xlim
		max_x_scale = max(max(x_female), max(x_male))

		fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(12, 10))

		fig.patch.set_facecolor('xkcd:Beige')
		#plt.figtext(.5,.9,selected_country + ": " +  str(selected_year), fontsize=15, ha='center')
		plt.figtext(.5,.95,selected_country + " " + str(selected_year), fontsize=14, ha='center')
		
		### DELETE SPACES BETWEEN
		plt.subplots_adjust(wspace=0, hspace=0)

		axes[0].barh(y, x_male, align='center', color='lightblue')
		axes[0].set(title='muži')
		axes[0].set(xlim=[0,max_x_scale])
		axes[1].barh(y, x_female, align='center', color='pink')
		axes[1].set(title='ženy')
		axes[1].set(xlim=[0,max_x_scale])
		#axes[1].grid()
		axes[0].set(yticks=y, yticklabels=pop_df_tmp['AgeGrp'])
		axes[0].invert_xaxis()
		#axes[0].grid()
		### ADDED STEPI
		axes[0].set_xlabel('počet ob. v tis.')
		axes[1].set_xlabel('počet ob. v tis.')

		img = io.BytesIO()
		plt.savefig(img, format='png', quality=100, dpi=300)
		img.seek(0)
		plot_url = base64.b64encode(img.getvalue()).decode()
		plot_to_show = Markup('<img src="data:image/png;base64,{}" style="display: block;margin-left: auto;margin-right: auto;width: 50%;">'.format(plot_url))

	return render_template('build-a-pyramid.html',
						plot_to_show = plot_to_show,
						selected_country = selected_country,
						location_list = location_list,
						selected_year = selected_year)



if __name__=='__main__':
    app.run(ssl_context=('/etc/letsencrypt/live/geografieliberec.cz/cert.pem', '/etc/letsencrypt/live/geografieliberec.cz/privkey.pem'), host="0.0.0.0", port=5000)