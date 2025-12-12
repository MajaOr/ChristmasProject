import streamlit as st
import pandas as pd
import random
from fpdf import FPDF

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
    "Tricep curls": 1,
}

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

exercise_images = {
    "Armbøjninger": "images/pushup.jpg",
    "Squat": "images/squat.jpg",
    "Lunges": "images/lunges.jpg",
    "Thrusters": "images/thruster.jpg",
    "Skulderpres": "images/shoulderpress.jpg",
    "Devils press": "images/devilspress.jpg",
    "Renegade row": "images/renegade.jpg",
    "Løb": "images/running.jpg",
    "Biceps curls": "images/bicep.jpg",
    "Bend over back fly": "images/bentovre.jpg",
    "Lateral raises": "images/lateral.jpg",
    "Clean": "images/clean.jpg",
    "Kettlebell swing": "images/kettlebell.jpg",
    "Goblet squat": "images/gobletsquat.jpg",
    "One arm row": "images/onearmrow.jpg",
    "One arm front squat": "images/onearmfrontsquat.jpg",
    "Step ups": "images/stepups.jpg",
    "Bulgarian squat": "images/bulgariansplitsquat.jpg",
    "Split squat": "images/splitsquat.jpg",
    "Sjip": "images/sjip.jpg",
    "Bænkpres fra gulv": "images/chestpress.jpg",
    "Snatch": "images/snatch.jpg",
    "Dødløft": "images/deadlift.jpg",
    "Tricep curls": "images/tricepcurls.jpg",
    "Jump squat": "images/jumpsquat.jpg",
    "Jump lunges": "images/jumplunges.jpg",
    "Mavebøjninger": "images/situp.jpg",
    "Sidemavebøjninger": "images/sidemave.jpg",
    "Atomic situps": "images/atomicsitup.png",
    "Cykelmavebøjning": "images/cykelmave.jpg",
    "Leg raises": "images/legraises.jpg",
    "Heel touches": "images/heeltouches.png",
    "Burpees": "images/burpees.jpg",
    "Planke": "images/planke.jpg",
    "Sideplanke": "images/sideplanke.jpg",
    "Glute bridge": "images/glutebridge.jpg",
    "Reverse burpee": "images/reverseburpee.jpg",
    "Walkout": "images/walkouts.jpg",
    "Shoulder taps": "images/shouldertaps.jpg",
    "Dips": "images/dips.jpg",
    "Skovskider": "images/skovskider.jpg",
    "Rygbøjninger": "images/rygbøjninger.png",
    "Bird dog": "images/birddog.jpg",
    "Mountainclimbers": "images/mountainclimbers.jpg",
    "Hollow hold": "images/hollowhold.png",
    "Russian twist": "images/russiantwist.png",
}


a = list(a.items())
b = list(b.items())


def append_and_remove(
    start_exerciselist: list, exercise_list: list, exercise: str, musclegroup: int
):
    exercise_list.append(exercise)
    start_exerciselist.remove((exercise, musclegroup))


a_copy = a.copy()
b_copy = b.copy()


def make_exercise_lists():
    """This function will choose a random exercise from group A,
    then ensure that next exercise is different value that first exercise, etc. until it has picked 8 exercises.
    Returns two lists of 8 exercises each, one from group A and one from group B. Group B exercises are also chosen such that
    they do not match the muscle group of the corresponding exercise in group A. However, group B exercises can have the same muscle group as previous exercises in group B.
    """
    # We start by creating two empty lists
    exercise_a = []
    exercise_b = []
    # Then we pick the first exercise from each group
    start_a_exercise, start_a_musclegroup = random.choice(a_copy)
    # We append the exercise to the list and remove it from the pool such that it cannot be chosen again
    append_and_remove(a_copy, exercise_a, start_a_exercise, start_a_musclegroup)
    # Now we pick the first exercise from group B, ensuring it is not the same muscle group as the first exercise from group A
    start_b_exercise, start_b_musclegroup = random.choice(b_copy)
    while start_b_musclegroup == start_a_musclegroup:
        start_b_exercise, start_b_musclegroup = random.choice(b_copy)
    append_and_remove(b_copy, exercise_b, start_b_exercise, start_b_musclegroup)
    i = 0
    # Then we continue picking exercises until we have 8 in each list
    while i < 7:
        next_a_exercise, next_a_musclegroup = random.choice(a_copy)
        while next_a_musclegroup == start_a_musclegroup:
            # if same muscletype is selected, try to pick new one
            next_a_exercise, next_a_musclegroup = random.choice(a_copy)
        append_and_remove(a_copy, exercise_a, next_a_exercise, next_a_musclegroup)
        # Then we select B exercise choosing same approach however b are allowed to be same as start_b, just not same as a
        next_b_exercise, next_b_musclegroup = random.choice(b_copy)
        while next_b_musclegroup == next_a_musclegroup:
            next_b_exercise, next_b_musclegroup = random.choice(b_copy)
        append_and_remove(b_copy, exercise_b, next_b_exercise, next_b_musclegroup)
        # Update start musclegroup to be the last selected one
        start_a_musclegroup = next_a_musclegroup
        i += 1
    return exercise_a, exercise_b


def df_to_pdf(df, exercise_images, filename="results.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Mors tabata app", ln=True, align="C")
    pdf.ln(5)

    for i in range(len(df)):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(0, 10, f"Round {i+1}", ln=True)
        pdf.set_font("Arial", size=12)
        y_before = pdf.get_y()

        # Exercise A
        pdf.cell(40, 10, f"A: {df.iloc[i]['Exercise A']}", border=1)
        if df.iloc[i]["Exercise A"] in exercise_images:
            x = pdf.get_x()
            y = y_before
            pdf.image(exercise_images[df.iloc[i]["Exercise A"]], x=x, y=y, w=30, h=20)
            pdf.set_y(y + 20)
        else:
            pdf.cell(40, 10, "No image", border=1)

        # Exercise B
        pdf.set_y(y_before)
        pdf.set_x(100)
        pdf.cell(40, 10, f"B: {df.iloc[i]['Exercise B']}", border=1)
        if df.iloc[i]["Exercise B"] in exercise_images:
            x = pdf.get_x()
            y = y_before
            pdf.image(exercise_images[df.iloc[i]["Exercise B"]], x=x, y=y, w=30, h=20)
            pdf.set_y(y + 20)
        else:
            pdf.cell(40, 10, "No image", border=1)

        pdf.ln(25)  # Space before next round

    pdf_output = pdf.output(dest="S").encode("latin1")
    return pdf_output


if "exercise_a" not in st.session_state or "exercise_b" not in st.session_state:
    st.session_state.exercise_a, st.session_state.exercise_b = make_exercise_lists()

if st.button("Generate new"):
    st.session_state.exercise_a, st.session_state.exercise_b = make_exercise_lists()

exercise_a = st.session_state.exercise_a
exercise_b = st.session_state.exercise_b


st.title("Mors tabata app")

for i in range(len(exercise_a)):
    st.subheader(f"**Round {i+1}**")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**A**: {exercise_a[i]}")
        st.image(exercise_images[exercise_a[i]], width=200)

    with col2:
        st.write(f"**B**: {exercise_b[i]}")
        st.image(exercise_images[exercise_b[i]], width=200)
    st.write("---")

df = pd.DataFrame(
    {
        "Round": [i + 1 for i in range(len(exercise_a))],
        "Exercise A": exercise_a,
        "Exercise B": exercise_b,
    }
)


pdf_data = df_to_pdf(df, exercise_images)

st.download_button(
    label="📥 Download PDF",
    data=pdf_data,
    file_name="results.pdf",
    mime="application/pdf",
)
