#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


    #try:
    #    print(sys.argv[1])
    #    if sys.argv[1]=='run':
    #        os.system('powershell -command "Get-NetTCPConnection -LocalPort 8000 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"')
    #        os.system('cd berlinvenv/Scripts & activate & cd ../.. & taskkill /f /im uvicorn.exe & uvicorn myproject.asgi:application --host 127.0.0.1 --port 8000')
    #        exit()
    #    elif sys.argv[1]=='stop':
    #        os.system('powershell -command "Get-NetTCPConnection -LocalPort 8000 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"')
    #        exit()
    #    else: 
    #        main()
    #except:
    #    os.system('powershell -command "Get-NetTCPConnection -LocalPort 8000 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"')
    #    os.system('cd berlinvenv/Scripts & activate & cd ../.. & taskkill /f /im uvicorn.exe & uvicorn myproject.asgi:application --host 127.0.0.1 --port 8000')

    
