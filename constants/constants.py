# Inserted into the MAIN_PAGE_URL in 'main.py' for specific data collection
YEAR = 2022
PREVIOUS_YEAR = 2021
FISCAL_QUARTER = 2

# Reporting Period Dates
reporting_periods = {
    'Q1': [f'{PREVIOUS_YEAR}-04-01', f'{PREVIOUS_YEAR}-06-30'],
    'Q2': [f'{PREVIOUS_YEAR}-07-01', f'{PREVIOUS_YEAR}-09-30'],
    'Q3': [f'{PREVIOUS_YEAR}-10-01', f'{PREVIOUS_YEAR}-12-31'],
    'Q4': [f'{YEAR}-01-01', f'{YEAR}-03-31']
}

REPORTING_TIME_PERIOD = reporting_periods['Q2']


# URL Information
 # MP_EXPENSES_PAGE_URL needs to have /YEAR/QUARTER/ + unique href value appended to it
BASE_URL = 'https://www.ourcommons.ca'
MP_EXPENSES_PAGE_URL = f"{BASE_URL}/proactivedisclosure/en/members/{YEAR}/{FISCAL_QUARTER}/"


# Firefox/Selenium Constants
FIREFOX_BINARY = '/opt/firefox/firefox'
GECKO_DRIVER_EXECUTABLE = '/usr/local/bin/geckodriver'



# Error Messages
NO_TBODY_FOUND = 'No <tbody> element found in the HTML'


# Tbody classes
EXPENSES_MAIN_INFO = 'expenses-main-info'


# General Strings
EMPTY_STRING = ''
NOT_LISTED = 'Not Listed'



# MP Lookup Dict
MP_LOOKUP = {
    'Ziad Aboultaif': 1,
    'Scott Aitchison': 2,
    'Dan Albas': 3,
    'Omar Alghabra': 4,
    'Leona Alleslev': 5,
    'Dean Allison': 6,
    'William Amos': 7,
    'Anita Anand': 8,
    'Gary Anandasangaree': 9,
    'Charlie Angus': 10,
    'Mel Arnold': 11,
    'René Arseneault': 12,
    'Chandra Arya': 13,
    'Niki Ashton': 14,
    'Jenica Atwin': 15,
    'Taylor Bachrach': 16,
    'Vance Badawey': 17,
    'Larry Bagnell': 18,
    'Navdeep Bains': 19,
    'Yvan Baker': 20,
    'Tony Baldinelli': 21,
    'John Barlow': 22,
    'Michael Barrett': 23,
    'Xavier Barsalou-Duval': 24,
    'Jaime Battiste': 25,
    'Mario Beaulieu': 26,
    'Terry Beech': 27,
    'Rachel Bendayan': 28,
    'Carolyn Bennett': 29,
    'Bob Benzen': 30,
    'Candice Bergen': 31,
    'Stéphane Bergeron': 32,
    'Luc Berthold': 33,
    'Sylvie Bérubé': 34,
    'Lyne Bessette': 35,
    'James Bezan': 36,
    'Marie-Claude Bibeau': 37,
    'Chris Bittle': 38,
    'Daniel Blaikie': 39,
    'Bill Blair': 40,
    'Yves-François Blanchet': 41,
    'Maxime Blanchette-Joncas': 42,
    'Rachel Blaney': 43,
    'Steven Blaney': 44,
    'Kelly Block': 45,
    'Kody Blois': 46,
    'Michel Boudrias': 47,
    'Alexandre Boulerice': 48,
    'Richard Bragdon': 49,
    'John Brassard': 50,
    'Bob Bratina': 51,
    'Élisabeth Brière': 52,
    'Alexis Brunelle-Duceppe': 53,
    'Celina Caesar-Chavannes': 54,
    'Blaine Calkins': 55,
    'Richard Cannings': 56,
    'Jim Carr': 57,
    'Colin Carrie': 58,
    'Sean Casey': 59,
    'Louise Chabot': 60,
    'Bardish Chagger': 61,
    'François-Philippe Champagne': 62,
    'Martin Champoux': 63,
    'Louise Charbonneau': 64,
    'Shaun Chen': 65,
    'Kenny Chiu': 66,
    'Michael Chong': 67,
    'Laurel Collins': 68,
    'Michael Cooper': 69,
    'Serge Cormier': 70,
    'James Cumming': 71,
    "Chris d'Entremont": 72,
    'Julie Dabrusin': 73,
    'Marc Dalton': 74,
    'Pam Damoff': 75,
    'Raquel Dancho': 76,
    'Scot Davidson': 77,
    'Don Davies': 78,
    'Claude DeBellefeuille': 79,
    'Gérard Deltell': 80,
    'Caroline Desbiens': 81,
    'Luc Desilets': 82,
    'Sukh Dhaliwal': 83,
    'Anju Dhillon': 84,
    'Kerry Diotte': 85,
    'Todd Doherty': 86,
    'Han Dong': 87,
    'Fin Donnelly': 88,
    'Terry Dowdall': 89,
    'Earl Dreeshen': 90,
    'Francis Drouin': 91,
    'Emmanuel Dubourg': 92,
    'Jean-Yves Duclos': 93,
    'Terry Duguid': 94,
    'Eric Duncan': 95,
    'Kirsty Duncan': 96,
    'Scott Duvall': 97,
    'Julie Dzerowicz': 98,
    'Wayne Easter': 99,
    'Ali Ehsassi': 100,
    'Fayçal El-Khoury': 101,
    'Neil Ellis': 102,
    'Dave Epp': 103,
    'Nathaniel Erskine-Smith': 104,
    'Rosemarie Falk': 105,
    'Ted Falk': 106,
    'Ed Fast': 107,
    'Greg Fergus': 108,
    'Andy Fillmore': 109,
    'Kerry-Lynne Findlay': 110,
    'Diane Finley': 111,
    'Pat Finnigan': 112,
    'Darren Fisher': 113,
    'Peter Fonseca': 114,
    'Mona Fortier': 115,
    'Rhéal Fortin': 116,
    'Peter Fragiskatos': 117,
    'Sean Fraser': 118,
    'Chrystia Freeland': 119,
    'Hedy Fry': 120,
    'Cheryl Gallant': 121,
    'Marc Garneau': 122,
    'Randall Garrison': 123,
    'Marie-Hélène Gaudreau': 124,
    'Leah Gazan': 125,
    'Bernard Généreux': 126,
    'Garnett Genuis': 127,
    'Mark Gerretsen': 128,
    'Marilène Gill': 129,
    'Marilyn Gladu': 130,
    'Joël Godin': 131,
    'Karina Gould': 132,
    'Jacques Gourde': 133,
    'Tracy Gray': 134,
    'Matthew Green': 135,
    'Steven Guilbeault': 136,
    'Patty Hajdu': 137,
    'Jasraj Singh Hallan': 138,
    'Rachael Harder': 139,
    'Ken Hardie': 140,
    'Jack Harris': 141,
    'Randy Hoback': 142,
    'Mark Holland': 143,
    'Anthony Housefather': 144,
    'Carol Hughes': 145,
    'Ahmed Hussen': 146,
    'Gudie Hutchings': 147,
    'Angelo Iacono': 148,
    'Helena Jaczek': 149,
    'Tamara Jansen': 150,
    'Matt Jeneroux': 151,
    'Gord Johns': 152,
    'Mélanie Joly': 153,
    'Yvonne Jones': 154,
    'Bernadette Jordan': 155,
    'Majid Jowhari': 156,
    'Peter Julian': 157,
    'Mike Kelloway': 158,
    'Pat Kelly': 159,
    'Peter Kent': 160,
    'Iqra Khalid': 161,
    'Kamal Khera': 162,
    'Robert Kitchen': 163,
    'Tom Kmiec': 164,
    'Annie Koutrakis': 165,
    'Michael Kram': 166,
    'Damien Kurek': 167,
    'Stephanie Kusie': 168,
    'Irek Kusmierczyk': 169,
    'Jenny Kwan': 170,
    'Mike Lake': 171,
    'Marie-France Lalonde': 172,
    'Emmanuella Lambropoulos': 173,
    'David Lametti': 174,
    'Kevin Lamoureux': 175,
    'Andréanne Larouche': 176,
    'Patricia Lattanzio': 177,
    'Stéphane Lauzon': 178,
    'Philip Lawrence': 179,
    'Dominic LeBlanc': 180,
    'Diane Lebouthillier': 181,
    'Paul Lefebvre': 182,
    'Richard Lehoux': 183,
    'Sébastien Lemire': 184,
    'Michael Levitt': 185,
    'Chris Lewis': 186,
    'Ron Liepert': 187,
    'Joël Lightbound': 188,
    'Dane Lloyd': 189,
    'Ben Lobb': 190,
    'Wayne Long': 191,
    'Lloyd Longfield': 192,
    'Tim Louis': 193,
    'Tom Lukiwski': 194,
    'Lawrence MacAulay': 195,
    'Alistair MacGregor': 196,
    'Dave MacKenzie': 197,
    'Steven MacKinnon': 198,
    'Larry Maguire': 199,
    'James Maloney': 200,
    'Paul Manly': 201,
    'Simon Marcil': 202,
    'Richard Martel': 203,
    'Soraya Martinez Ferrada': 204,
    'Brian Masse': 205,
    'Lindsay Mathyssen': 206,
    'Bryan May': 207,
    'Elizabeth May': 208,
    'Dan Mazier': 209,
    'Kelly McCauley': 210,
    'Phil McColeman': 211,
    'Karen McCrimmon': 212,
    'Ken McDonald': 213,
    'David McGuinty': 214,
    'John McKay': 215,
    'Catherine McKenna': 216,
    'Ron McKinnon': 217,
    'Greg McLean': 218,
    'Cathy McLeod': 219,
    'Michael McLeod': 220,
    'Heather McPherson': 221,
    'Eric Melillo': 222,
    'Alexandra Mendès': 223,
    'Marco Mendicino': 224,
    'Kristina Michaud': 225,
    'Marc Miller': 226,
    'Maryam Monsef': 227,
    'Christine Moore': 228,
    'Rob Moore': 229,
    'Marty Morantz': 230,
    'Bill Morneau': 231,
    'Rob Morrison': 232,
    'Robert Morrissey': 233,
    'Glen Motz': 234,
    'Joyce Murray': 235,
    'Eva Nassif': 236,
    'John Nater': 237,
    'Mary Ng': 238,
    'Christine Normandin': 239,
    "Jennifer O'Connell": 240,
    "Seamus O'Regan": 241,
    "Erin O'Toole": 242,
    'Robert Oliphant': 243,
    'Robert-Falcon Ouellette': 244,
    'Jeremy Patzer': 245,
    'Pierre Paul-Hus': 246,
    'Monique Pauzé': 247,
    'Yves Perron': 248,
    'Ginette Petitpas Taylor': 249,
    'Louis Plamondon': 250,
    'Pierre Poilievre': 251,
    'Marcus Powlowski': 252,
    'Mumilaaq Qaqqaq': 253,
    'Carla Qualtrough': 254,
    'Tracey Ramsey': 255,
    'Yasmin Ratansi': 256,
    'Alain Rayes': 257,
    'Brad Redekopp': 258,
    'Geoff Regan': 259,
    'Scott Reid': 260,
    'Michelle Rempel Garner': 261,
    'Blake Richards': 262,
    'Yves Robillard': 263,
    'Pablo Rodriguez': 264,
    'Churence Rogers': 265,
    'Sherry Romanado': 266,
    'Lianne Rood': 267,
    'Anthony Rota': 268,
    'Alex Ruff': 269,
    'Dan Ruimy': 270,
    'Jag Sahota': 271,
    'Ruby Sahota': 272,
    'Raj Saini': 273,
    'Harjit S. Sajjan': 274,
    'Darrell Samson': 275,
    'Ramesh Sangha': 276,
    'Randeep Sarai': 277,
    'Bob Saroya': 278,
    'Simon-Pierre Savard-Tremblay': 279,
    'Francis Scarpaleggia': 280,
    'Andrew Scheer': 281,
    'Peter Schiefke': 282,
    'Jamie Schmale': 283,
    'Deb Schulte': 284,
    'Kyle Seeback': 285,
    'Marc Serré': 286,
    'Judy A. Sgro': 287,
    'Brenda Shanahan': 288,
    'Terry Sheehan': 289,
    'Martin Shields': 290,
    'Nelly Shin': 291,
    'Doug Shipley': 292,
    'Maninder Sidhu': 293,
    'Sonia Sidhu': 294,
    'Gagan Sikand': 295,
    'Mario Simard': 296,
    'Scott Simms': 297,
    'Jagmeet Singh': 298,
    'Derek Sloan': 299,
    'Francesco Sorbara': 300,
    'Gerald Soroka': 301,
    'Sven Spengemann': 302,
    'Bruce Stanton': 303,
    'Gabriel Ste-Marie': 304,
    'Warren Steinley': 305,
    'Wayne Stetski': 306,
    'Mark Strahl': 307,
    'Shannon Stubbs': 308,
    'David Sweet': 309,
    'Marwan Tabbara': 310,
    'Geng Tan': 311,
    'Filomena Tassi': 312,
    'Luc Thériault': 313,
    'Alain Therrien': 314,
    'Corey Tochor': 315,
    'Hunter Tootoo': 316,
    'Right Justin Trudeau': 317,
    'Denis Trudel': 318,
    'Ryan Turnbull': 319,
    'Tim Uppal': 320,
    'Vacant Vacant20/q2': 321,
    'Tony Van Bynen': 322,
    'Adam van Koeverden': 323,
    'Tako Van Popta': 324,
    'Dan Vandal': 325,
    'Anita Vandenbeld': 326,
    'Adam Vaughan': 327,
    'Karen Vecchio': 328,
    'Gary Vidal': 329,
    'Arnold Viersen': 330,
    'Julie Vignola': 331,
    'Arif Virani': 332,
    'Brad Vis': 333,
    'Cathay Wagantall': 334,
    'Chris Warkentin': 335,
    'Kevin Waugh': 336,
    'Len Webber': 337,
    'Patrick Weiler': 338,
    'Jonathan Wilkinson': 339,
    'John Williamson': 340,
    'Jody Wilson-Raybould': 341,
    'Alice Wong': 342,
    'Jean Yip': 343,
    'Kate Young': 344,
    'David Yurdiga': 345,
    'Salma Zahid': 346,
    'Sameer Zuberi': 347,
    'Bob Zimmer': 348,
    'Marci Ien': 349,
    'Alaina Lockhart': 350,
    'Lisa Raitt': 351,
    'Murray Rankin': 352,
    "Ya'ara Saks": 353,
    'Brigitte Sansoucy': 354,
    'Vacant Vacant20/q3': 355,
    'Lenore Zann': 356,
    'Gordie Hogg': 357,
    'Linda Lapointe': 358,
    'Hélène Laverdière': 359,
    'Amarjeet Sohi': 360,
    'Karine Trudel': 361,
    'Vacant Vacant20/q4': 362,
    'Brad Trost': 363,
    'Vacant Vacant22/q1': 364,

}


