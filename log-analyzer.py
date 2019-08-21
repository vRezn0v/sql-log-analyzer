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
q1='''select title,count(*) as views from articles inner join 
      log on CONCAT('/article/',articles.slug)=log.path
      where log.status='200 OK'
      group by log.path,articles.title order by views desc limit 3;'''
//Views on posts by different authors
q2='''select authors.name,count(*) as views from articles inner join 
      authors on articles.author = authors.id inner join 
      log on CONCAT('/article/',articles.slug)=log.path where 
      log.status='200 OK' group by authors.name order by views desc;'''
//Find Days having more than 1 percent downtime
q3='''//QUERY 3'''