import csv

with open('contacts.CSV', 'r', encoding='mac_roman') as csvfile:
     lines = []
     reader = csv.reader(csvfile, delimiter=',')
     titles = next(reader)
     lines.append(titles)
     for i, title in enumerate(titles):
         if title == 'E-mail Address':
             email_slot = i
             print(title)
             print(i)
         if title == 'E-mail Display Name':
             email_now = i
             print(title)
             print(i)

     for line in reader:
        longemail = line[email_now]
        email = longemail[longemail.find('(')+1:longemail.find(')')]
        line[email_slot] = email
        lines.append(line)
        print(line[email_slot])

with open('contacts1.CSV', 'w', encoding='mac_roman') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for line in lines:
        writer.writerow(line)
