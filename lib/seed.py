#!/usr/bin/env python3

from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Dev, Company, Freebies

engine = create_engine('sqlite:///seed_db.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_records():
    session.query(Dev).delete()
    session.query(Company).delete()
    session.query(Freebies).delete()
    session.commit()

def create_records():
    companies = [Company() for i in range(500)]
    devs = [Dev() for i in range(500)]
    freebies = [Freebies() for i in range(1000)]
    session.add_all(companies + devs + freebies)
    session.commit()
    return companies, devs, freebies

def relate_one_to_many(devs, companies, freebies):
    for freebie in freebies:
        freebie.dev = rc(devs)
        freebie.company = rc(companies)

    session.add_all(freebies)
    session.commit()

if __name__ == '__main__':
    delete_records()
    devs, companies, freebies = create_records()
    relate_one_to_many(devs, companies, freebies)
