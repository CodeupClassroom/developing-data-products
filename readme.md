# Developing Data Products

1. Virtual Environments
1. Build A Model
1. Flask Intro
1. HTML Templates
1. HTML Forms
1. Styling
1. Next Steps

## Virtual Environments

1. Tool for isolating and managing project dependencies
1. `venv`
1. We'll create a folder inside of our project that holds python and related
   libraries
1. Workflow
    1. Creation `python -m venv`
    2. Activate it `. env/bin/activate`
    3. Work on our project
    4. Deactivate

## HTML Forms

Form workflow

1. Visit a page where a form is shown (GET)
2. Fill out information in the form
3. Submit the form (POST)
4. Form inputs are processed
5. Results are shown

## How do we make our website live?

1. Buy a domain name (namecheap.com)
2. Own/rent a server -- cloud hosting (digital ocean)
3. Domain Name -> Server IP Address -- DNS
4. Server Setup
    - web server running that runs flask

Don't pay money for an https cert!

Check out the [codeup deployment tool][1]

[1]: https://github.com/zgulde/cods/blob/master/docs/python-deployment-guide.md
