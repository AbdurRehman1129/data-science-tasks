universal = {"Ayah", "Ayan", "Ali", "Fatima", "Omar", "Malik", "Suleman",
             "Aisha", "Rahman", "Jibril", "Zainab", "Hassan", "Khadija",
             "Rayyan", "Safia", "Ibrahim", "Maha"}
math_club = {"Ayah", "Ali", "Ayan", "Fatima", "Omar"}
science_club = {"Omar", "Malik", "Aisha", "Fatima"}
sports_club = {"Rahman", "Jibril", "Omar", "Zainab", "Fatima"}
speech_club = {"Hassan", "Khadija", "Rayyan",
               "Safia", "Omar", "Ibrahim", "Fatima"}
union = math_club.union(science_club, sports_club, speech_club)
intersection = math_club.intersection(science_club, sports_club, speech_club)
difference = universal.difference(union)
only_math = math_club.difference(intersection)
only_science = science_club.difference(intersection)
only_sports = sports_club.difference(intersection)
only_speech = speech_club.difference(intersection)

print("\nStudents participated in only Math Activites")
for i in only_math:
    print(i)
print("\nStudents participated in only Science Activites")
for i in only_science:
    print(i)
print("\nStudents participated in only Sports Activites")
for i in only_sports:
    print(i)
print("\nStudents participated in only Speech Activites")
for i in only_speech:
    print(i)
print("\nStudents participated in All Activites")
for i in intersection:
    print(i)
print("\nStudents participated in none Activites")
for i in difference:
    print(i)
