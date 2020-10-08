states_and_capitals = {
  'Alabama': 'Montgomery',
  'Alaska': 'Juneau',
  'Arizona':'Phoenix',
  'Arkansas':'Little Rock',
  'California': 'Sacramento',
  'Colorado':'Denver',
  'Connecticut':'Hartford',
  'Delaware':'Dover',
  'Florida': 'Tallahassee',
  'Georgia': 'Atlanta',
  'Hawaii': 'Honolulu',
  'Idaho': 'Boise',
  'Illinios': 'Springfield',
  'Indiana': 'Indianapolis',
  'Iowa': 'Des Monies',
  'Kansas': 'Topeka',
  'Kentucky': 'Frankfort',
  'Louisiana': 'Baton Rouge',
  'Maine': 'Augusta',
  'Maryland': 'Annapolis',
  'Massachusetts': 'Boston',
  'Michigan': 'Lansing',
  'Minnesota': 'St. Paul',
  'Mississippi': 'Jackson',
  'Missouri': 'Jefferson City',
  'Montana': 'Helena',
  'Nebraska': 'Lincoln',
  'Neveda': 'Carson City',
  'New Hampshire': 'Concord',
  'New Jersey': 'Trenton',
  'New Mexico': 'Santa Fe',
  'New York': 'Albany',
  'North Carolina': 'Raleigh',
  'North Dakota': 'Bismarck',
  'Ohio': 'Columbus',
  'Oklahoma': 'Oklahoma City',
  'Oregon': 'Salem',
  'Pennsylvania': 'Harrisburg',
  'Rhoda Island': 'Providence',
  'South Carolina': 'Columbia',
  'South Dakoda': 'Pierre',
  'Tennessee': 'Nashville',
  'Texas': 'Austin',
  'Utah': 'Salt Lake City',
  'Vermont': 'Montpelier',
  'Virginia': 'Richmond',
  'Washington': 'Olympia',
  'West Virginia': 'Charleston',
  'Wisconsin': 'Madison',
  'Wyoming': 'Cheyenne'
}

import random

states = list(states_and_capitals.keys())
score = 0
number_of_questions = 0
while True:
  state = random.choice(states)
  capital = states_and_capitals[state]
  capital_guess = input('What is the capital of ' + state + '?: ')
  if capital_guess == capital:
    print('Good Job! Here comes the next one!')
    score += 1
    number_of_questions += 1
  elif capital_guess == 'quit':
    number_of_questions += 1
    letter_grade = ''
    if score == 0:
      letter_grade = 'F'
      print('Your score was: ' + '0' + '/' + '0' + ' which is also ' + '0' + '%! That gives you this letter grade: ' + letter_grade + '! Also it means you failed!')
    else:
      percentage = (score/number_of_questions) * 100
      if percentage == 100:
        letter_grade = 'A+'
      elif percentage < 100 and percentage >= 95:
        letter_grade = 'A'
      elif percentage < 95 and percentage >= 90:
        letter_grade = 'A-'
      elif percentage < 90 and percentage > 85:
        letter_grade = 'B+'
      elif percentage == 85:
        letter_grade = 'B'
      elif percentage < 85 and percentage >= 80:
        letter_grade = 'B-'
      else:
        letter_grade = 'C or below'
      print('Your score was: ' + str(score) + '/' + str(number_of_questions) + ' which is also ' + str(percentage) + '%! That gives you this letter grade: ' + letter_grade + '!')
    print('Come Back Again!')
    
    break
  else:
    print("That's Incorrect! The capital of " + state + "is actually " + capital + ".")
    number_of_questions += 1