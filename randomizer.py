import random
import json
import math
import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
# All units in SI system - kg, m/s, m, s etc
# Definition of inanimate objects with their properties
inanimate_objects = {
    "objects": {
        "stone": {"mass": (0.3, 1), "density": (1, 2), "throwable": 1, "throwable_distance": 20, "speed": (5, 25)},
        "rock": {"mass": (10, 500), "density": (2, 3), "throwable": 0, "throwable_distance": 0, "speed": (0, 0)},
        "metal ball": {"mass": (2, 50), "density": (5, 10), "throwable": 1, "throwable_distance": 15, "speed": (3, 20)},
        "wood": {"mass": (0.5, 10), "density": (0.2, 1), "throwable": 0, "throwable_distance": 25, "speed": (6, 30)},
        "glass": {"mass": (0.2, 5), "density": (2, 4), "throwable": 0, "throwable_distance": 10, "speed": (4, 15)},
        "paper": {"mass": (0.01, 0.5), "density": (0.1, 0.5), "throwable": 0, "throwable_distance": 0, "speed": (0, 0)},
        "box": {"mass": (0.1, 2), "density": (1, 3), "throwable": 1, "throwable_distance": 18, "speed": (5, 22)},
        "clay brick": {"mass": (0.5, 5), "density": (1, 2), "throwable": 0, "throwable_distance": 22, "speed": (4, 18)},
        "marble": {"mass": (5, 100), "density": (2, 4), "throwable": 0, "throwable_distance": 0, "speed": (0, 0)},
        "brick": {"mass": (2, 30), "density": (3, 5), "throwable": 0, "throwable_distance": 0, "speed": (0, 0)}
    },
    "shape": ["irregular", "cylindrical", "rectangular", "round", "flat"]
}

def random_object_properties():
    """
    Randomly pick an object and fetch its corresponding properties.
    """
    random_object = random.choice(list(inanimate_objects["objects"].keys()))
    object_properties = inanimate_objects["objects"][random_object]

    properties = {
        "object": random_object,
        "mass": random.uniform(*object_properties["mass"]),
        "density": random.uniform(*object_properties["density"]),
        "shape": random.choice(inanimate_objects["shape"]),
        "throwable": object_properties["throwable"],
        "throwable_distance": object_properties["throwable_distance"]
    }
    return properties

def fetch_properties(object_name):
    """
    Fetch properties of a specific object by matching its name.
    """
    if object_name in inanimate_objects["objects"]:
        object_properties = inanimate_objects["objects"][object_name]
        properties = {
            "object": object_name,
            "mass": random.uniform(*object_properties["mass"]),
            "density": random.uniform(*object_properties["density"]),
            "shape": random.choice(inanimate_objects["shape"]),
            "throwable": object_properties["throwable"],
            "throwable_distance": object_properties["throwable_distance"]
        }
        return properties
    else:
        return None

# Man Made Structures
man_made_structures = {
    'structures': [
        {'name': 'house', 'height_range': (10, 20, 1), 'base': ['tub of water', 'concrete floor']},
        {'name': 'building', 'height_range': (15, 30, 1), 'base': ['swimming pool', 'concrete floor']},
        {'name': '3-storeyed building', 'height_range': (10, 35, 5), 'base': ['parking lot', 'concrete floor']},
        {'name': 'tower', 'height_range': (50, 100, 5), 'base': ['moat', 'landscaped area']},
        {'name': 'skyscraper', 'height_range': (100, 300, 10), 'base': ['lobby', 'underground parking']},
        {'name': 'bungalow', 'height_range': (5, 15, 2), 'base': ['pond', 'gravel path']},
        {'name': 'villa', 'height_range': (10, 20, 2), 'base': ['private pool', 'patio']},
        {'name': 'cottage', 'height_range': (5, 15, 1), 'base': ['wooden deck', 'stone path']},
        {'name': 'apartment complex', 'height_range': (15, 50, 5), 'base': ['common pool', 'playground']},
        {'name': 'lighthouse', 'height_range': (30, 70, 5), 'base': ['rocky shore', 'dock']}
    ]
}

def pick_random_structure():
    """
    Randomly select a structure and generate its characteristics.
    """
    structure = random.choice(man_made_structures['structures'])
    height = random.randrange(*structure['height_range'])
    base = random.choice(structure['base'])
    return structure['name'], height, base

sound_phrases = {
    'tub of water': ['splash'],
    'concrete floor': ['thud', 'clink'],
    'parking lot': ['thud', 'clatter'],
    'moat': ['splash', 'plop'],
    'landscaped area': ['thud', 'rustle'],
    'lobby': ['echo', 'clack'],
    'underground parking': ['echo', 'bang'],
    'pond': ['splash', 'plop'],
    'gravel path': ['crunch', 'scatter'],
    'private pool': ['splash', 'dive'],
    'patio': ['clack', 'tap'],
    'wooden deck': ['thud', 'clack'],
    'stone path': ['clack', 'crunch'],
    'common pool': ['splash', 'dive'],
    'playground': ['thud', 'clang'],
    'rocky shore': ['splash', 'clatter'],
    'dock': ['thud', 'splash']
}

def get_random_sound(base):
    """
    Get a random sound based on the base of a structure.
    """
    sounds = sound_phrases.get(base, [])
    if sounds:
        return random.choice(sounds)
    else:
        return "No sound available"

# Dictionary with vehicles and their properties
vehicles = {
    "Truck": {"mass_range": (7000, 30000), "speed_range": (10, 80)},
    "Car": {"mass_range": (1000, 3000), "speed_range": (0, 200)},
    "Bicycle": {"mass_range": (5, 15), "speed_range": (0, 30)},
    "Motorcycle": {"mass_range": (100, 400), "speed_range": (0, 130)},
    "Bus": {"mass_range": (8000, 30000), "speed_range": (10, 100)},
    "Van": {"mass_range": (2000, 5000), "speed_range": (0, 160)},
    "Automobile": {"mass_range": (1000, 3000), "speed_range": (0, 200)}
}

# Expanded list of dictionaries for phrases related to acceleration or deceleration with variations
phrase_vehicle_acceleration = [
    {"vehicle": "Truck", "phrase": "rolls down a hill", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Truck", "phrase": "moves down the hill", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Car", "phrase": "speeds along the highway", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Car", "phrase": "accelerates on the freeway", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Bicycle", "phrase": "glides down the slope", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Bicycle", "phrase": "rushes downhill", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Motorcycle", "phrase": "accelerates on the open road", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Motorcycle", "phrase": "picks up speed quickly", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Bus", "phrase": "gains speed on the freeway", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Bus", "phrase": "accelerates as it leaves the stop", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Van", "phrase": "picks up pace on the road", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Van", "phrase": "gathers speed on the highway", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Automobile", "phrase": "accelerates past the crowd", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Automobile", "phrase": "speeds up along the coast", "direction": "acceleration", "magnitude": 1},
    {"vehicle": "Truck", "phrase": "moves up a hill", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Truck", "phrase": "slows as it climbs", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Car", "phrase": "comes to a stop at the light", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Car", "phrase": "gradually slows in traffic", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Bicycle", "phrase": "slows down at the intersection", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Bicycle", "phrase": "comes to a gentle stop", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Motorcycle", "phrase": "decelerates to navigate a turn", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Motorcycle", "phrase": "eases off the throttle", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Bus", "phrase": "slows for the bus stop", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Bus", "phrase": "reduces speed for passengers", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Van", "phrase": "reduces speed for parking", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Van", "phrase": "slows to a stop for delivery", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Automobile", "phrase": "decelerates to a halt", "direction": "deceleration", "magnitude": -1},
    {"vehicle": "Automobile", "phrase": "slows as it approaches the garage", "direction": "deceleration", "magnitude": -1}
]

# Function to randomly pick a vehicle and assign a random mass within its mass range
def pick_vehicle():
    vehicle_name = random.choice(list(vehicles.keys()))
    vehicle = vehicles[vehicle_name]
    mass_in_kg = random.randint(vehicle['mass_range'][0], vehicle['mass_range'][1])
    return {"name": vehicle_name, "mass_in_kg": mass_in_kg}

# Function to pick a phrase from the phrase_vehicle_acceleration depending on the selected vehicle
def pick_phrase(vehicle_name):
    phrases = [phrase for phrase in phrase_vehicle_acceleration if phrase['vehicle'] == vehicle_name]
    phrase_set = random.choice(phrases)
    return phrase_set

motion_phrases = {
    "objects": [
        ("stone", "ice"),  # stone gliding on ice
        # ("metal", "magnet"),  # metal attracted to a magnet
        ("metal ball", "water"),  # wood floating on water
        ("paper", "wind"),  # paper carried by the wind
        ("box", "conveyer belt"),  # plastic thrown into a recycling bin
        ("clay brick", "wall"),  # clay brick used in a wall
        ("marble", "floor"),  # marble rolling on the floor
    ],
    "phrases": [
        ["thrown", "across the frozen surface of a lake"],
        # ["attracted", "towards each other"],
        ["thrown", "inside a rive against the direction of the flow"],
        ["being", "whisked away by a gust"],
        ["pushed", "by a robotic arm"],
        ["gliding", "down a slanted wall of a building"],
        ["rolling", "smoothly"],
    ]
}

racing_phrases = {
    "racer": {
        "description": "athlete",
        "scenarios": [
            {"activity": "sprinting", "location": "of a circular track", "distance_type": "diameter", "distance_range": (100, 500), "lap_type": "circuit", "speed_range": (6, 10)},
            {"activity": "jogging", "location": "along a scenic trail",  "distance_type": "length", "distance_range": (200, 800), "lap_type": "trail", "speed_range": (3, 6)},
            {"activity": "racing", "location": "through the city streets",  "distance_type": "length", "distance_range": (50, 300), "lap_type": "street", "speed_range": (7, 12)},
            # {"activity": "running", "location": "on the treadmill",  "distance_type": "diameter", "distance_range": (10, 50), "lap_type": "session", "speed_range": (4, 8)},
            {"activity": "dashing", "location": "across a sandy beach",  "distance_type": "length", "distance_range": (80, 400), "lap_type": "stretch", "speed_range": (5, 10)}
            # Additional scenarios for "racer" can be added here
        ]
    },
    "cyclist": {
        "description": "athlete on two wheels",
        "scenarios": [
            {"activity": "cycling", "location": "on the mountain path",  "distance_type": "length","distance_range": (100, 1000), "lap_type": "round", "speed_range": (5, 15)},
            {"activity": "cycling", "location": "through the city bike lanes",  "distance_type": "length", "distance_range": (50, 300), "lap_type": "pass", "speed_range": (10, 20)}
            # Additional scenarios for "cyclist" can be added here
        ]
    },
    # "driver": {
    #     "description": "athlete in a car",
    #     "scenarios": [
    #         {"activity": "driving", "location": "on the racing circuit", "distance_type": "diameter", "distance_range": (1000, 2500), "lap_type": "lap", "speed_range": (30, 60)},
    #         {"activity": "driving", "location": "through rally stages",  "distance_type": "diameter", "distance_range": (10, 50), "lap_type": "stage", "speed_range": (30, 60)}
    #         # Additional scenarios for "driver" can be added here
    #     ]
    # },
    "swimmer": {
        "description": "athlete in water",
        "scenarios": [
            {"activity": "swimming", "location": "across the lake", "distance_type": "length", "distance_range": (500, 1500), "lap_type": "section", "speed_range": (1, 3)},
            {"activity": "swimming", "location": "in the Olympic pool",  "distance_type": "length", "distance_range": (100, 200), "lap_type": "lane", "speed_range": (2, 4)}
            # Additional scenarios for "swimmer" can be added here
        ]
    }
    # Add other roles with similar structure if needed
}

# Helper function to convert numbers to words
def number_to_words(number):
    num_to_word = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        # Extend this dictionary as needed
    }
    return num_to_word.get(number, str(number))

def pluralize_lap_type(lap_type, lap):
    if lap == 1:
        return lap_type
    else:
        return pluralize_noun(lap_type)

def pick_racing_phrase():
    # Pick a random role
    role = random.choice(list(racing_phrases.keys()))
    role_info = racing_phrases[role]
    scenario = random.choice(role_info["scenarios"])
    activity = scenario["activity"]
    location = scenario["location"]
    lap_length = random.randint(*scenario["distance_range"])
    laps = random.randint(1,10)
    lap_type = pluralize_lap_type(scenario["lap_type"], laps)
    lap_length_type = scenario["distance_type"]
    speed = random.randint(*scenario["speed_range"])
    lap_as_word = number_to_words(laps)

    # Return information as a dictionary
    return {
        "role": role,
        "activity": activity,
        "lap_length": lap_length,
        "lap_type": lap_type,
        "location": location,
        "speed": speed,
        "laps": laps,
        "lap_as_word": lap_as_word,
        "lap_length_type": lap_length_type
    }

# Dictionary containing lists of proper nouns with names from across the globe and genders
proper_nouns = {
    "combinations": [
        ["Liam", "Smith", "male"],
        ["Emma", "García", "female"],
        ["Santiago", "Patel", "male"],
        ["Yuki", "Kim", "female"],
        ["Aarav", "Ivanov", "male"],
        ["Chen", "Chen", "male"],
        ["Olivia", "Müller", "female"],
        ["Mohammed", "Rossi", "male"],
        ["Ivan", "Dubois", "male"],
        ["Sophia", "Silva", "female"]
    ]
}

def generate_random_name():
    """
    Generates a random name and gender from the proper_nouns dictionary.

    Returns:
        A dictionary containing a first name, last name, and a gender.
    """
    # Randomly pick a combination
    chosen_combination = random.choice(proper_nouns["combinations"])

    # Extract the first name, last name, and gender from the chosen combination
    first_name, last_name, gender = chosen_combination

    return {'first_name': first_name, 'last_name': last_name, 'gender': gender}

import nltk

# nltk.download('punkt')

def get_article(word):
    # Function to determine the appropriate article 'a' or 'an' based on the word's pronunciation
    tokens = nltk.word_tokenize(word)
    first_letter = tokens[0][0].lower()

    return 'an' if first_letter in ['a', 'e', 'i', 'o', 'u'] else 'a'

# Get Plural of words
import inflect

def pluralize_noun(noun):
    p = inflect.engine()
    # plurals = [p.plural(noun) for noun in nouns]
    return p.plural(noun)

def question_template_LO1_1(article_object, object_name, article_struct_obj, structure_name, height, article_base, base, sound):
    return f"{article_object.capitalize()} {object_name} is dropped from the top of {article_struct_obj} {structure_name} {height} m high into {article_base} {base} at the base of the {structure_name}. When is the {sound} heard at the top? Given, g = 10 m/s^2 and speed of sound, v = 340 m/s."

def question_template_LO1_2(article_object, object_name, article_struct_obj, structure_name, height, article_base, base, sound):
    person = generate_random_name()['first_name']
    return f"{person.capitalize()} drops {article_object} {object_name} from the top of {article_struct_obj} {structure_name} {height} m high into {article_base} {base} at the base of the {structure_name}. When does {person.capitalize()} hear the {sound} at the top? Given, g = 10 m/s^2 and speed of sound, v = 340 m/s."

def question_template_LO1_3(article_object, object_name, article_struct_obj, structure_name, height, article_base, base, sound):
    person = generate_random_name()['first_name']
    return f"{person.capitalize()} drops {article_object} {object_name} from the top of {article_struct_obj} {structure_name} {height} m high into {article_base} {base} at the base of the {structure_name}. How much time does it take for the {sound} to reach back to {person.capitalize()}? Given, g = 10 m/s^2 and speed of sound, v = 340 m/s."

def LO_1_question_generator(num_of_questions=1):
    questions = []

    for _ in range(num_of_questions):
        objects = {key: value for key, value in inanimate_objects["objects"].items() if value["throwable"] == 1}
        object_name = random.choice(list(objects.keys()))
        article_object = get_article(object_name)

        structure_obj = random.choice(man_made_structures['structures'])
        structure_name = structure_obj['name']
        article_struct_obj = get_article(structure_name)
        height = random.randrange(*structure_obj['height_range'])

        base = random.choice(structure_obj['base'])
        article_base = get_article(base)
        sound = random.choice(sound_phrases.get(base, ["splash"]))

        question_templates = [question_template_LO1_1, question_template_LO1_2, question_template_LO1_3]
        template_func = random.choice(question_templates)
        question_text = template_func(article_object, object_name, article_struct_obj, structure_name, height, article_base, base, sound)

        ans_unit = 's'
        choices = [
            round(math.sqrt((2 * height / 10) + (height / 340)), 2),  # Initially the correct choice
            round(math.sqrt((2 * height / 10)), 2),
            round(2*math.sqrt((2 * height / 10)),2),
            round(2*math.sqrt((2 * height / 10) + (height / 340)), 2)
        ]

        # Shuffling choices except the correct one
        correct_choice = choices[0]  # The correct choice before shuffling
        choices_without_correct = choices[1:]
        random.shuffle(choices_without_correct)
        correct_position = random.randint(0, len(choices_without_correct))
        shuffled_choices = choices_without_correct[:correct_position] + [correct_choice] + choices_without_correct[correct_position:]

        # Finding the correct choice index after shuffling
        correct_index = chr(ord('A') + shuffled_choices.index(correct_choice))

        # Append 's' unit and format for JSON output
        formatted_choices = {chr(65 + i): f"{value} {ans_unit}" for i, value in enumerate(shuffled_choices)}

        question_data = {
            "question": question_text,
            "choices": formatted_choices,
            "correct_choice": correct_index
            
        }

        questions.append(question_data)

    return json.dumps(questions, indent=4)

# Example usage
# print(LO_1_question_generator())

def question_template_LO2_1(vehicle_article, vehicle_name, acceleration_phrase, distance, time, vehicle_mass, unit_for_mass):
    return f"{vehicle_article.capitalize()} {vehicle_name} starts from rest and {acceleration_phrase} with constant acceleration. It travels a distance of {distance} m in {time} s. Find the force acting on it if its mass is {vehicle_mass} {unit_for_mass}."

def question_template_LO2_2(vehicle_article, vehicle_name, acceleration_phrase, distance, time, vehicle_mass, unit_for_mass):
    person = generate_random_name()['first_name']
    return f"{person} starts {vehicle_article} {vehicle_name} from rest and {acceleration_phrase} with constant acceleration. It travels a distance of {distance} m in {time} s. Find the force acting on the {vehicle_name} if its mass is {vehicle_mass} {unit_for_mass}."

def LO_2_question_generator(num_of_questions=1):
    questions = []

    for _ in range(num_of_questions):
        # Pick a random vehicle
        vehicle_name = random.choice(list(vehicles.keys()))
        vehicle = vehicles[vehicle_name]
        vehicle_mass_in_kg = random.randint(vehicle['mass_range'][0], vehicle['mass_range'][1])
        vehicle_article = get_article(vehicle_name)

        # Pick a phrase for acceleration
        acceleration_phrases = [phrase for phrase in phrase_vehicle_acceleration if phrase['vehicle'] == vehicle_name and phrase['direction'] == "acceleration"]
        acceleration_phrase = random.choice(acceleration_phrases)['phrase']

        # Select time, distance
        distance = random.randrange(350, 1501, 50)
        time = random.randrange(15, 31)

        # Determine unit for mass
        if vehicle_mass_in_kg >= 1000:
            unit_for_mass = 'tonnes' if round(vehicle_mass_in_kg / 1000, 1) > 1 else 'tonne'
            vehicle_mass = round(vehicle_mass_in_kg / 1000, 1)  # Convert to tonnes, round to one decimal place
        elif 500 < vehicle_mass_in_kg < 1000:
            unit_for_mass = random.choice(['tonnes', 'kg'])
            vehicle_mass = round(vehicle_mass_in_kg / 1000, 1) if unit_for_mass == 'tonnes' else vehicle_mass_in_kg
        else:
            unit_for_mass = 'kg'
            vehicle_mass = vehicle_mass_in_kg

        # Randomly choose one of the two question templates
        question_template_functions = [question_template_LO2_1, question_template_LO2_2]
        question_template = random.choice(question_template_functions)

        question_text = question_template(vehicle_article, vehicle_name, acceleration_phrase, distance, time, vehicle_mass, unit_for_mass)

        # Formula is F = m*((2*s)/t^2)), prepare choices
        correct_force = round(vehicle_mass_in_kg * ((2 * distance) / (time**2)), -2)  # Correct choice calculated with mass in kg for consistency
        # choices = [
        #     f"{correct_force} N",
        #     f"{round(vehicle_mass * ((2 * distance) / time**2), 0)} N",
        #     f"{round(vehicle_mass * 100 * ((2 * distance) / time**2), 0)} N",
        #     f"{round(vehicle_mass * ((distance) / time**2), 0)} N"
        # ]
        choices = [
            f"{correct_force} N",
            f"{correct_force + 500} N",
            f"{correct_force + 1000} N",
            f"{correct_force + 1500} N"
        ]

        # Shuffling choices while keeping track of the correct one
        correct_choice = choices[0]  # Correct answer before shuffling
        choices_without_correct = choices[1:]
        random.shuffle(choices_without_correct)
        correct_position = random.randint(0, len(choices_without_correct))
        shuffled_choices = choices_without_correct[:correct_position] + [correct_choice] + choices_without_correct[correct_position:]
        correct_index = chr(ord('A') + shuffled_choices.index(correct_choice))

        # Storing the question and choices in a JSON structure
        question_data_json = json.dumps({
            "question": question_text,
            "choices": {chr(65 + i): choice for i, choice in enumerate(shuffled_choices)},
            "correct_choice": correct_index
        }, indent=4)

        # Construct the question data dictionary
        question_data = {
            "question": question_text,
            "choices": {chr(65 + i): f"{choice}" for i, choice in enumerate(shuffled_choices)},
            "correct_choice": correct_index
        }

        questions.append(question_data)

    return json.dumps(questions, indent=4)

# Example usage
# print(LO_2_question_generator())

# Define Question templates
def question_template_LO3_1(article, object_name, mass, velocity, verb, phrase, distance):
    return f"{article.capitalize()} {object_name} of {mass} kg is {verb} with a velocity of {velocity} m/s {phrase} and comes to rest after travelling a distance of {distance} m. What is the force of friction between the {object_name} and the surface?"

def question_template_LO3_2(article, object_name, mass, velocity, verb, phrase, distance):
    person = generate_random_name()
    pronoun = "he" if person['gender'] == "male" else "she"
    return f"{article.capitalize()} {object_name} of {mass} kg is {verb} with a velocity of {velocity} m/s {phrase} and the {object_name} comes to rest after travelling a distance of {distance} m. {person['first_name']} correctly calculates the force of friction between the {object_name} and the surface. What is the value {pronoun} gets?"

def LO_3_question_generator(num_of_questions=1):
    questions = []

    for _ in range(num_of_questions):
        # Corrections applied here for random velocity selection
        throwable_objects = {name: props for name, props in inanimate_objects["objects"].items() if props['throwable'] == 1}
        object_name, object_props = random.choice(list(throwable_objects.items()))
        article = get_article(object_name)

        object_mass_in_kg = random.uniform(*object_props['mass'])
        object_velocity_in_ms = random.randint(*object_props['speed'])  # Corrected for uniform distribution

        time = random.randint(3, 10)
        distance_travelled = object_velocity_in_ms * time

        interacting_with = next((item for item in motion_phrases["objects"] if item[0] == object_name), None)

        if interacting_with:
            index = motion_phrases["objects"].index(interacting_with)
            interacting_verb, interacting_phrase = motion_phrases["phrases"][index]

            question_template = random.choice([question_template_LO3_1, question_template_LO3_2])
            question_text = question_template(article, object_name, round(object_mass_in_kg, 2), object_velocity_in_ms, interacting_verb, interacting_phrase, distance_travelled)

            correct_force = round(object_mass_in_kg * (-object_velocity_in_ms ** 2) / (2 * distance_travelled), 2)
            choices = [
                f"{correct_force} N",
                f"{round(correct_force + 1, 2)} N",
                f"{round(correct_force + 2, 2)} N",
                f"{round(correct_force + 3, 2)} N"
            ]

            question_data = {
                "question": question_text,
                "choices": {chr(65 + i): choice for i, choice in enumerate(choices)},
                "correct_choice": 'A'
            }

            questions.append(question_data)

    return json.dumps(questions, indent=4)

# Example usage (This line is just for demonstration and should be uncommented in an actual Python environment)
# Since some of the objects does not have corersponding interaction objects, sometimes this function might return null
# print(LO_3_question_generator())
import random
import json
import math

def question_template_LO4_1(racer_article, racer, lap_as_word, lap_type, location, lap_length_type, lap_length, n_laps_time_conv, end_time):
    return f"{racer_article.capitalize()} {racer} completes {lap_as_word} {lap_type} {location} of {lap_length_type} {lap_length} m in {n_laps_time_conv}. What will be the distance covered at the end of {end_time[0]} minutes {end_time[1]} s?"

def question_template_LO4_2(racer_article, racer, lap_as_word, lap_type, location, lap_length_type, lap_length, n_laps_time_conv, end_time):
    person = generate_random_name()
    return f"{person['first_name'].capitalize()} completes {lap_as_word} {lap_type} {location} of {lap_length_type} {lap_length} m in {n_laps_time_conv}. What will be the distance covered at the end of {end_time[0]} minutes {end_time[1]} s?"

def LO_4_question_generator(num_of_questions=1):
    questions = []

    for _ in range(num_of_questions):
        race_instance = pick_racing_phrase()
        racer = race_instance['role']
        racer_article = get_article(racer)
        lap_as_word = race_instance['lap_as_word']
        lap_type = race_instance['lap_type']
        location = race_instance['location']
        lap_length_type = race_instance['lap_length_type']
        lap_length = race_instance['lap_length']
        speed = race_instance['speed']
        laps = race_instance['laps']

        run_distance_per_lap = round(math.pi*lap_length, 0) if lap_type == 'diameter' else lap_length
        run_distance_n_laps = run_distance_per_lap*laps
        n_laps_time = int(round(run_distance_n_laps/speed, 0))

        # Logic to convert n_laps_time based on its value
        if n_laps_time < 60:
            n_laps_time_conv = f"{n_laps_time} s"
        elif n_laps_time == 60:
            n_laps_time_conv = "1 minute"
        else:
            minutes = n_laps_time // 60
            seconds = n_laps_time % 60
            n_laps_time_conv = f"{minutes} minutes {seconds} s"

        end_time = [random.randint(2, 20), random.randint(2, 59)]
        total_distance = round(speed*(end_time[0]*60+end_time[1]),0)

        question_templates = [question_template_LO4_1, question_template_LO4_2]
        template_func = random.choice(question_templates)
        question_text = template_func(racer_article, racer, lap_as_word, lap_type, location, lap_length_type, lap_length, n_laps_time_conv, end_time)

        choices = [
            f"{total_distance} m",  # Correct choice
            f"{round(lap_length/n_laps_time*(end_time[0]*60+end_time[1]),0)} m",
            f"{total_distance + 20} m",
            f"{round(lap_length/n_laps_time*(end_time[0]*60+end_time[1]/10),0)} m"
        ]

        random.shuffle(choices)
        correct_index = chr(ord('A') + choices.index(f"{total_distance} m"))

        formatted_choices = {chr(65 + i): choice for i, choice in enumerate(choices)}

        question_data = {
            "question": question_text,
            "choices": formatted_choices,
            "correct_choice": correct_index
        }

        questions.append(question_data)

    return json.dumps(questions, indent=4)

# Example usage
# print(LO_4_question_generator())

def mdf_concept_question_set_generator(num_of_questions=10):
    aggregated_questions = []

    for question_number in range(num_of_questions):
        # Randomly pick one of the three question generator functions
        question_generator = random.choice([LO_1_question_generator, LO_2_question_generator, LO_3_question_generator, LO_4_question_generator])

        # Generate questions using the chosen generator
        generated_questions_json = question_generator(1)  # This calls the generator to get JSON string
        generated_questions = json.loads(generated_questions_json)  # Parse the JSON string back into Python objects

        # Add question numbers to each question structure
        for question in generated_questions:
            # question["question_number"] = question_number + 1  # Adding 1 to make it 1-indexed
            # Reconstruct the question with question_number as the first key
            ordered_question = {"question_number": question_number + 1}
            ordered_question.update(question)
            # Replace the original question with the ordered version
            question = ordered_question

        # Aggregate the generated question(s) with question numbers into the master list
        aggregated_questions.append(question)
        # aggregated_questions.extend(generated_questions)

    # Convert the aggregated list of dictionaries (with question numbers) back into JSON string for the return value
    return json.dumps(aggregated_questions, indent=4)

if __name__ == "__main__":
    print(mdf_concept_question_set_generator(10)) 
 