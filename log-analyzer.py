#!/usr/bin/env python

import psycopg2

def send_query(query):
    '''Makes a query to the database.'''
    db=psycopg2.connect(database="news")
    c=db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()
//Find top 3 posts of all time
q1='''select title,count(*) as views
      from articles,log
      where log.path=CONCAT('/articles/',articles.slug)
      group by articles.title
      order by views desc'''
//Views on posts by different authors
q2='''select authors.name,count(*) as views
      from articles inner join authors
      on articles.author = authors.id
      inner join log 
      on CONCAT('/articles/',articles.slug)'''
//Find Days having more than 1 percent downtime
q3='''//QUERY 3'''