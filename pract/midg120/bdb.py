ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, permissions = input().split(' ', maxsplit=1)
    file_permissions[file] = set(permissions.split())

for i in range(int(input())):
    action, file = input().split()
    
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
