import web
import json
data = [{'votes': 6, 'value': 494549.5, 'abbreviation': 'MS', 'state': 'Mississippi', 'pop': 2967297, 'worth': 1.1604024767672698}, {'votes': 7, 'value': 535907.2857142857, 'abbreviation': 'OK', 'state': 'Oklahoma', 'pop': 3751351, 'worth': 1.0708502757508174}, {'votes': 3, 'value': 299311.3333333333, 'abbreviation': 'DE', 'state': 'Delaware', 'pop': 897934, 'worth': 1.917322870112998}, {'votes': 10, 'value': 530392.5, 'abbreviation': 'MN', 'state': 'Minnesota', 'pop': 5303925, 'worth': 1.081984501447541}, {'votes': 20, 'value': 641531.6, 'abbreviation': 'IL', 'state': 'Illinois', 'pop': 12830632, 'worth': 0.8945412270946823}, {'votes': 6, 'value': 485986.3333333333, 'abbreviation': 'AR', 'state': 'Arkansas', 'pop': 2915918, 'worth': 1.1808489772703106}, {'votes': 5, 'value': 411835.8, 'abbreviation': 'NM', 'state': 'New Mexico', 'pop': 2059179, 'worth': 1.3934593949433607}, {'votes': 11, 'value': 589436.5454545454, 'abbreviation': 'IN', 'state': 'Indiana', 'pop': 6483802, 'worth': 0.973601771233015}, {'votes': 10, 'value': 577355.2, 'abbreviation': 'MD', 'state': 'Maryland', 'pop': 5773552, 'worth': 0.9939747051451429}, {'votes': 8, 'value': 566671.5, 'abbreviation': 'LA', 'state': 'Louisiana', 'pop': 4533372, 'worth': 1.0127145351125209}, {'votes': 4, 'value': 391895.5, 'abbreviation': 'ID', 'state': 'Idaho', 'pop': 1567582, 'worth': 1.4643609449049935}, {'votes': 3, 'value': 224197.0, 'abbreviation': 'ND', 'state': 'North Dakota', 'pop': 672591, 'worth': 2.559697340660289}, {'votes': 3, 'value': 187875.33333333334, 'abbreviation': 'WY', 'state': 'Wyoming', 'pop': 563626, 'worth': 3.0545599281297253}, {'votes': 11, 'value': 576918.6363636364, 'abbreviation': 'TN', 'state': 'Tennessee', 'pop': 6346105, 'worth': 0.9947268618348049}, {'votes': 11, 'value': 581092.4545454546, 'abbreviation': 'AZ', 'state': 'Arizona', 'pop': 6392017, 'worth': 0.9875820279458211}, {'votes': 6, 'value': 507725.8333333333, 'abbreviation': 'IA', 'state': 'Iowa', 'pop': 3046355, 'worth': 1.1302880944945974}, {'votes': 16, 'value': 617727.5, 'abbreviation': 'MI', 'state': 'Michigan', 'pop': 9883640, 'worth': 0.9290123309776801}, {'votes': 6, 'value': 475519.6666666667, 'abbreviation': 'KS', 'state': 'Kansas', 'pop': 2853118, 'worth': 1.2068406522632746}, {'votes': 6, 'value': 460647.5, 'abbreviation': 'UT', 'state': 'Utah', 'pop': 2763885, 'worth': 1.2458039274803725}, {'votes': 13, 'value': 615463.3846153846, 'abbreviation': 'VA', 'state': 'Virginia', 'pop': 8001024, 'worth': 0.9324299040838014}, {'votes': 7, 'value': 547296.2857142857, 'abbreviation': 'OR', 'state': 'Oregon', 'pop': 3831074, 'worth': 1.0485663426987066}, {'votes': 7, 'value': 510585.28571428574, 'abbreviation': 'CT', 'state': 'Connecticut', 'pop': 3574097, 'worth': 1.1239580942509686}, {'votes': 3, 'value': 329805.0, 'abbreviation': 'MT', 'state': 'Montana', 'pop': 989415, 'worth': 1.7400478000152058}, {'votes': 55, 'value': 677344.6545454545, 'abbreviation': 'CA', 'state': 'California', 'pop': 37253956, 'worth': 0.8472443988933905}, {'votes': 11, 'value': 595239.0, 'abbreviation': 'MA', 'state': 'Massachusetts', 'pop': 6547629, 'worth': 0.9641109952204323}, {'votes': 5, 'value': 370598.8, 'abbreviation': 'WV', 'state': 'West Virginia', 'pop': 1852994, 'worth': 1.5485113947590088}, {'votes': 9, 'value': 513929.3333333333, 'abbreviation': 'SC', 'state': 'South Carolina', 'pop': 4625364, 'worth': 1.1166446969700405}, {'votes': 4, 'value': 329117.5, 'abbreviation': 'NH', 'state': 'New Hampshire', 'pop': 1316470, 'worth': 1.7436826199883473}, {'votes': 10, 'value': 568698.6, 'abbreviation': 'WI', 'state': 'Wisconsin', 'pop': 5686986, 'worth': 1.0091047607362054}, {'votes': 3, 'value': 208580.33333333334, 'abbreviation': 'VT', 'state': 'Vermont', 'pop': 625741, 'worth': 2.7513450358088165}, {'votes': 16, 'value': 605478.3125, 'abbreviation': 'GA', 'state': 'Georgia', 'pop': 9687653, 'worth': 0.9478068046970962}, {'votes': 3, 'value': 200574.33333333334, 'abbreviation': 'DC', 'state': 'D.C.', 'pop': 601723, 'worth': 2.86116600836605}, {'votes': 20, 'value': 635118.95, 'abbreviation': 'PA', 'state': 'Pennsylvania', 'pop': 12702379, 'worth': 0.9035732041753989}, {'votes': 29, 'value': 648321.0344827586, 'abbreviation': 'FL', 'state': 'Florida', 'pop': 18801310, 'worth': 0.8851732924905995}, {'votes': 3, 'value': 236743.66666666666, 'abbreviation': 'AK', 'state': 'Alaska', 'pop': 710231, 'worth': 2.4240414654556686}, {'votes': 8, 'value': 542420.875, 'abbreviation': 'KY', 'state': 'Kentucky', 'pop': 4339367, 'worth': 1.0579911119460785}, {'votes': 4, 'value': 340075.25, 'abbreviation': 'HI', 'state': 'Hawaii', 'pop': 1360301, 'worth': 1.6874984718353214}, {'votes': 5, 'value': 365268.2, 'abbreviation': 'NE', 'state': 'Nebraska', 'pop': 1826341, 'worth': 1.571109843901043}, {'votes': 10, 'value': 598892.7, 'abbreviation': 'MO', 'state': 'Missouri', 'pop': 5988927, 'worth': 0.9582291864369276}, {'votes': 18, 'value': 640916.8888888889, 'abbreviation': 'OH', 'state': 'Ohio', 'pop': 11536504, 'worth': 0.8953991923647119}, {'votes': 9, 'value': 531081.7777777778, 'abbreviation': 'AL', 'state': 'Alabama', 'pop': 4779736, 'worth': 1.0805802207812596}, {'votes': 4, 'value': 263141.75, 'abbreviation': 'RI', 'state': 'Rhode Island', 'pop': 1052567, 'worth': 2.180864361827855}, {'votes': 3, 'value': 271393.3333333333, 'abbreviation': 'SD', 'state': 'South Dakota', 'pop': 814180, 'worth': 2.1145562333292944}, {'votes': 9, 'value': 558799.5555555555, 'abbreviation': 'CO', 'state': 'Colorado', 'pop': 5029196, 'worth': 1.0269808896205546}, {'votes': 14, 'value': 627992.4285714285, 'abbreviation': 'NJ', 'state': 'New Jersey', 'pop': 8791894, 'worth': 0.9138270440449133}, {'votes': 12, 'value': 560378.3333333334, 'abbreviation': 'WA', 'state': 'Washington', 'pop': 6724540, 'worth': 1.024087532561064}, {'votes': 15, 'value': 635698.8666666667, 'abbreviation': 'NC', 'state': 'North Carolina', 'pop': 9535483, 'worth': 0.9027489189860884}, {'votes': 29, 'value': 668210.4137931034, 'abbreviation': 'NY', 'state': 'New York', 'pop': 19378102, 'worth': 0.8588259818137212}, {'votes': 38, 'value': 661725.2894736842, 'abbreviation': 'TX', 'state': 'Texas', 'pop': 25145561, 'worth': 0.8672427573993107}, {'votes': 6, 'value': 450091.8333333333, 'abbreviation': 'NV', 'state': 'Nevada', 'pop': 2700551, 'worth': 1.2750208339350337}, {'votes': 4, 'value': 332090.25, 'abbreviation': 'ME', 'state': 'Maine', 'pop': 1328361, 'worth': 1.7280738133203697}] 

urls = (
    '/fips.js', 'fips',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

render = web.template.render('templates')

class hello:
	def GET(self, name):
		return render.hello(data)

class fips:
	def GET(self):
		enc = json.JSONEncoder()
		new = {}
		electoral = {}
		pop = {}
		rep = {}
		count = 0
		for item in data:
			count += 1
			electoral[item['state']] = str(item['votes'])
			pop[item['state']] = "{:,}".format(item['pop']/1000)
			new[item['state']] = int(item['worth']*100)
			rep[item['state']] = (item['pop']/item['votes'])/1000

			
		#enc.encode(data)
		value = """var fips = {
  "Alabama": "01",
  "Alaska": "02",
  "Arizona": "04",
  "Arkansas": "05",
  "California": "06",
  "Colorado": "08",
  "Connecticut": "09",
  "Delaware": "10",
  "D.C.": "11",
  "Florida": "12",
  "Georgia": "13",
  "Hawaii": "15",
  "Idaho": "16",
  "Illinois": "17",
  "Indiana": "18",
  "Iowa": "19",
  "Kansas": "20",
  "Kentucky": "21",
  "Louisiana": "22",
  "Maine": "23",
  "Maryland": "24",
  "Massachusetts": "25",
  "Michigan": "26",
  "Minnesota": "27",
  "Mississippi": "28",
  "Missouri": "29",
  "Montana": "30",
  "Nebraska": "31",
  "Nevada": "32",
  "New Hampshire": "33",
  "New Jersey": "34",
  "New Mexico": "35",
  "New York": "36",
  "North Carolina": "37",
  "North Dakota": "38",
  "Ohio": "39",
  "Oklahoma": "40",
  "Oregon": "41",
  "Pennsylvania": "42",
  "Rhode Island": "44",
  "South Carolina": "45",
  "South Dakota": "46",
  "Tennessee": "47",
  "Texas": "48",
  "Utah": "49",
  "Vermont": "50",
  "Virginia": "51",
  "Washington": "53",
  "West Virginia": "54",
  "Wisconsin": "55",
  "Wyoming": "56"
};
		var statehood = %s;
		var electoral = %s;
		var pop = %s;
		var rep = %s;
		// Parse dates and convert to FIPS codes.
		var states = {};
		for (var state in statehood) {
		  states[fips[state]] = statehood[state];
		}
		"""
		web.header('Content-Type', 'application/json')
		return value % (enc.encode(new), enc.encode(electoral), enc.encode(pop), enc.encode(rep))

if __name__ == "__main__":
	app.cgirun()