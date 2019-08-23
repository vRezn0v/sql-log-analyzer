# Python SQL Log Analyzer #
A project under Udacity Full Stack Nanodegree program, written in Python and SQL using the psycopg2 API.

Built to calculate and complete tasks related to elements a relational database consisting of three tables
(articles,authors and log). 

The tasks are:

- To find the top 3 posts of all time.

- To rank the authors according to the total views on their articles.

- To list the days when more than 1% of requests to the server resulted in errors. (Codes other than 200 OK)

## Dependencies: ##
- psycopg2
- Vagrant
- FSND Virtual Machine

## Execution: ##
- Download the 'newsdata.sql' file from the Udacity page for this project and place it in vagrant directory.
- Start the vagrant session with
'''sh
vagrant up
'''
- Log into vagrant box via SSH
'''sh
vagrant ssh
'''
- Load the database into vagrant box by executing
'''sh
psql -d news -f newsdata.sql
'''
- Finally, run the analyzer script using
'''sh
python log-analyzer.py
'''

---