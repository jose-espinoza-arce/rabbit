from django.contrib.auth.models import Group

grps = Group.objects.all()


def write():
    with open("perms.txt", "w") as text_file:
        for g in grps:
            text_file.write("Permisos para el grupo: {0} \n".format(g))
            for p in g.permissions.all():
                text_file.write("-- {0} \n".format(p))
