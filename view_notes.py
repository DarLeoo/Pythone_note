from repository_file import create_note, read_note, update_note, delete_note, list_notes


def start():
    while True:
        print('\nCommands: create, read, update, delete, list, quit')
        command = input('Enter command: ')
        if command == 'create':
            create_note()
        elif command == 'read':
            read_note()
        elif command == 'update':
            update_note()
        elif command == 'delete':
            delete_note()
        elif command == 'list':
            list_notes()
        elif command == 'quit':
            break
        else:
            print('Invalid command')