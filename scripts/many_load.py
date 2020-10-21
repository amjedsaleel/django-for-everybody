import csv
from many.models import Person, Course, Membership


def run():
    csv_file = open('many/load.csv')
    read_csv = csv.reader(csv_file)

    # Person.objects.all().delete()
    # Course.objects.all().delete()
    # Membership.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in read_csv:
        print(row)

        p, created = Person.objects.get_or_create(email=row[0])
        c, created = Course.objects.get_or_create(title=row[2])

        r = Membership.LEARNER
        if row[1] == 'I' :
            r = Membership.INSTRUCTOR

        membership = Membership(role=r, person=p, course=c)
        membership.save()
