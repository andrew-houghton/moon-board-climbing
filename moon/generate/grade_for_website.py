import pickle
import json

from moon.utils.load_data import local_file_path
from moon.analytics.configuration import Configuration, run_configuration
from moon.models import keras_lstm_grade, keras_mlp, random_forest, xgboost_model
from moon.analytics.climb_preprocessor import HoldListPreprocessor, OneHotPreprocessor
from moon.analytics.grade_preprocessor import (
    CategoricalPreprocessor,
    FlandersPreprocessor,
    HalfGradePreprocessor,
    SplitPreprocessor,
)
from moon.types.grade import Grade

def web_json_format(climb):
    return {
        'grade': {"original":climb.grade.as_font_grade()},
        'moves': [hold.as_website_format() for hold in climb.holds]
    }

def main(year):
    # Load generated climbsets
    file_data = pickle.load(open(local_file_path(__file__, year+".pickle"), "rb"))
    website_data = {'original': [web_json_format(climb) for climb in file_data['original'].climbs]}

    Configuration.report_headings()

    setups = [
        (xgboost_model.Model(), FlandersPreprocessor()),
        (keras_mlp.Model(), CategoricalPreprocessor()),
        (random_forest.Model(), CategoricalPreprocessor()),
    ]

    for model, preprocessor in setups:
        # Train classifier on original (graded) data
        cfg = Configuration(model, file_data["original"], preprocessor)
        run_configuration(cfg)

        # Add grades to original dataset
        original_grades = cfg.sample(file_data["original"])
        original_grades = [Grade(int(i)).as_font_grade() for i in original_grades]
        for i, climb in enumerate(website_data['original']):
            climb['grade'][model.name()] = original_grades[i]

        # Sample classifier for generated data and original data
        grades = cfg.sample(file_data["lstm"])
        grades = [Grade(int(i)).as_font_grade() for i in grades]

        website_data['lstm']=[]
        for i, climb in enumerate(file_data["lstm"].climbs):
            website_data['lstm'].append({
                'grade': {model.name():grades[i]},
                'moves': [hold.as_website_format() for hold in climb.holds]
            })

    # Save to file
    with open(year+'.js', 'w') as handle:
        handle.write("var climbs = "+json.dumps(website_data))


if __name__=="__main__":
    main("2016")
    # main("2017")
