#!/usr/bin/env python

""" 
    Alex Gavin, Spring 2020

    Simple program to determine faculty of the year using pyrankvote library.
    Used for deciding WWU CS Department 2020 Faculty of the year.

    Faculty file should be a csv and contain faculty names in a "faculty" column.

    Results file should be a csv named "raw_results.csv" containing individual
    votes for up to three candidates and should have the following columns:

        first, second, third
"""

import pyrankvote
import pandas
from pyrankvote import Candidate, Ballot

# Open files, read data
candidates_df = pandas.read_csv("faculty.csv")
candidates = {name: Candidate(name) for name in candidates_df["faculty"]}

votes_df = pandas.read_csv("raw_results.csv")
voter_list = [(one, two, three) for one, two, three in zip(votes_df['first'], votes_df['second'], votes_df['third'])]

# Votes to ballots
ballots = []
for voter in voter_list:
    ranked_candidates = []
    for vote in voter:
        if vote in candidates and candidates[vote] not in ranked_candidates:
            ranked_candidates.append(candidates[vote])
        
        if vote not in candidates:
            print(f"Error: {vote} not in candidates!")
            exit()

    ballots.append(Ballot(ranked_candidates=ranked_candidates))

# pyrank vote requires candidates as a list, so cannot use a dict :(
candidates_list = [candidates[candidate] for candidate in candidates]

election_result = pyrankvote.instant_runoff_voting(candidates_list, ballots)
winners = election_result.get_winners()
print(election_result)
