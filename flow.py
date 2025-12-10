import streamlit as st
import pandas as pd
import random

# spec
# 1. Vælge om det skal være tabata eller A/B -> lige nu er kun A/B supporteret
# 2. Generer 2x8 øvelser, hvoraf en er A og en er B. A og B må ikke være af samme muskeltype. 
# 3. Formater på en eller anden måde der giver mening for mor.. Et skema og så et appendix evt med billeder
# jeg vil have semi random selection af keys. Første valg er random, og derefter skal den næste value være en anden
a = {
    "Armbøjninger": 1,
    "Squat": 2,
    "Lunges": 2,
    "Thrusters": 2,
    "Skulderpres": 1,
    "Devils press": 1,
    "Renegade row": 1,
    "Løb": 2,
    "Biceps curls": 1,
    "Bend over back fly": 4,
    "Lateral raises": 1,
    "Clean": 1,
    "Kettlebell swing": 3,
    "Goblet squat": 2,
    "One arm row": 4,
    "One arm front squat": 1,
    "Step ups": 2,
    "Bulgarian squat": 2,
    "Split squat": 2,
    "Sjip": 2,
    "Bænkpres fra gulv": 1,
    "Snatch": 1,
    "Dødløft": 2,
    "Tricep curls": 1}

b = {
    "Jump squat": 2,
    "Jump lunges": 2,
    "Mavebøjninger": 3,
    "Sidemavebøjninger": 3,
    "Atomic situps": 3,
    "Cykelmavebøjning": 3,
    "Leg raises": 3,
    "Heel touches": 3,
    "Burpees": 1,
    "Planke": 3,
    "Sideplanke": 3,
    "Glute bridge": 2,
    "Reverse burpee": 3,
    "Walkout": 3,
    "Shoulder taps": 1,
    "Dips": 1,
    "Skovskider": 2,
    "Rygbøjninger": 4,
    "Bird dog": 4,
    "Mountainclimbers": 3,
    "Hollow hold": 3,
    "Russian twist": 3,
}

a = list(a.items())
b = list(b.items())

def make_exercise_pairs():
    '''This function will choose a random exercise from group A,
    then ensure that next exercise is different value that first exercise, etc. until it has picked 8 exercises.'''
    # while i is not 8 (i.e. we need to do this loop 8 times)
    exercise_a = []
    start_a_exercise, start_a_musclegroup = random.choice(a)
    exercise_a.append(start_a_exercise)
    start_b_exercise, start_b_musclegroup = random.choice(b)
    while start_b_musclegroup == start_a_musclegroup:
        start_b_exercise, start_b_musclegroup = random.choice(b)
    i = 0
    while i < 7:
        next_a_exercise, next_a_musclegroup = random.choice(a)
        while next_a_musclegroup == start_a_musclegroup:
            # if same muscletype is selected, try to pick new one
            next_a_exercise, next_a_musclegroup = random.choice(a)
        # Then we select B exercise choosing same approac
        next_b_exercise, next_b_musclegroup = random.choice(a)


        

        

st.title("Mors tabata app")

df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Score": [95, 80, 75]})

st.write("Vælg:")
st.dataframe(df)

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV", data=csv_data, file_name="results.csv", mime="text/csv"
)
