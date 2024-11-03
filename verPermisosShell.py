from django.contrib.auth.models import User

# Obtener todos los usuarios y sus permisos
for user in User.objects.all():
    print(f"Usuario: {user.username}")
    print("Permisos individuales:")
    for perm in user.user_permissions.all():
        print(f" - {perm.name} ({perm.codename})")
    print("Permisos de grupos:")
    for group in user.groups.all():
        print(f"  Grupo: {group.name}")
        for perm in group.permissions.all():
            print(f"   - {perm.name} ({perm.codename})")
