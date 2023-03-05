def main():
    """
        Makes common .env file from all directories that
        are going to be containerized with docker-compose.
    """
    
    list_of_directories = [
        './backend/',
        './frontend/',
    ]
    
    list_of_lines = list()
    
    for dir in list_of_directories:
        with open(dir + '.env', 'r') as env:
            lines = env.readlines()
            list_of_lines += lines
    
    with open('.env', 'w') as env:
        env.writelines(list_of_lines)
    
    
if __name__ == '__main__':
    main()