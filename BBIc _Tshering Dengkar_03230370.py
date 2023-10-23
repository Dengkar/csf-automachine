import random
# list of subject
subjects = ['ACt101','HCM206','MAT101','CSF101','Eng101',]
# Days of the week
days = ['Monday','Tuesday','Wednesday','Thursday','Friday',]
# Initialize timetable dictionary
timetable = {}
# Generate timetable
for day in days:
    timetable[day] = []
    available_subjects = subjects.copy()
    # copy the list of subject to reset it each day
    for period in range(1, 5):  # Assuming 4 period in a day
        subject = random.choice(available_subjects)
        timetable[day].append(subject)
        available_subjects .remove(subject)
    # Remove the chosen subject to avoid repetition on the same day
    # Display timetable
    for days, subjects in timetable.items():
     print(f"{days}:{','.join(subjects)}")

















