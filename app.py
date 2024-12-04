from flask import Flask, jsonify, render_template, request
from randomizer import LO_1_question_generator,LO_2_question_generator,LO_3_question_generator,LO_4_question_generator,mdf_concept_question_set_generator
import json

app = Flask(__name__)
questions_data = [] 
def generate_questions(option_type, number_of_question):
    generated_questions_data = []
    
    if option_type == "LO_1":
        generated_questions_data = json.loads(LO_1_question_generator(number_of_question))
    elif option_type == "LO_2":
        generated_questions_data = json.loads(LO_2_question_generator(number_of_question))
    elif option_type == "LO_3":
        generated_questions_data = json.loads(LO_3_question_generator(number_of_question))
    elif option_type == "LO_4":
        generated_questions_data = json.loads(LO_4_question_generator(number_of_question))

    for index, question in enumerate(generated_questions_data):
        question['question_number'] = index + 1
    
    return generated_questions_data

@app.route('/', methods=["GET", "POST"])
def index():
    global questions_data
    
    default_number_of_question = 10
    default_option_type = "LO_1"
    
    if request.method == "POST":
        number_of_question = int(request.form.get("number_of_question", default_number_of_question))
        option_type = request.form.get("option-type", default_option_type)
        
        questions_data = generate_questions(option_type, number_of_question)
        
        return render_template('questions_template.html', questions=questions_data,
                               number_of_question=number_of_question, option_type=option_type)
    
    return render_template('questions_template.html', questions=questions_data,
                           number_of_question=default_number_of_question, option_type=default_option_type)

@app.route('/api/generate_questions', methods=['POST'])
def generate_questions_endpoint():
    global questions_data
    if request.method == "POST":
        data = request.get_json()

        if data is not None:
            number_of_question = int(data.get("number_of_question"))
            option_type = data.get("option-type")
            questions_data = mdf_concept_question_set_generator(number_of_question)
            with open('questions_data.json', 'w') as json_file:
                json.dump(questions_data, json_file)
            for d in questions_data:
                if "correct_choice" in d:
                    del d["correct_choice"]

    return jsonify(questions_data)

@app.route('/api/check_answers', methods=['POST'])
def check_answers():
    # Load the saved questions data from the JSON file
    questions = []
    with open('questions_data.json', 'r') as json_file:
        questions = json.load(json_file)
    questions_list = json.loads(questions)
    user_answers = request.get_json()  # Get user answers from the request

    correct_answers = 0
    total_questions = len(questions_list)

    for question in questions_list:
        question_id = question['question_number']
        correct_choice = question['correct_choice']
        
        # Get the answer for the current question from user_answers
        user_answer = user_answers.get("q"+str(+question_id))  # Assumes user answers are passed as a dictionary

        if user_answer == correct_choice:
            correct_answers += 1

    # Return the result
    return jsonify({
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'score': (correct_answers / total_questions) * 100
    })

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/api/check_answers', methods=['POST'])
# def check_answers():
#     user_answers = request.json.get('answers', {})
    
#     correct_answers = {}
#     for question in questions_data:
#         correct_answers[question['question_number']] = question['correct_choice']

#     results = {}
#     for question_number, user_answer in user_answers.items():
#         correct_answer = correct_answers.get(int(question_number))
#         is_correct = user_answer == correct_answer
#         results[question_number] = is_correct

#     return jsonify(results)

