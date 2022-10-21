windows_filenames = ["plaintext_passwords.txt", "grades.xsl", "exam_questions.doc"]
filenames = []
for name in windows_filenames:
    first_part, separator, last_part = name.rpartition(".")
    filenames.append(first_part)

print(filenames)
