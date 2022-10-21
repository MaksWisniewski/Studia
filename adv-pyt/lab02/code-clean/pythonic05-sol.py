windows_filenames = ["plaintext_passwords.txt", "grades.xsl", "exam_questions.doc"]

halfway = []
for name in windows_filenames:
    first_part, _, _ = name.rpartition(".")
    halfway.append(first_part)

filenames = [name.rpartition(".")[0] for name in windows_filenames]
print(filenames)

