# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:25:20 2022

@author: DELL
"""

sequence = "ACGTAACCCTGATTTA";
c = sequence.count('C');
g = sequence.count('G');
total = len(sequence);
fraction = (sequence.count ('C') + sequence.count('G')) / len(sequence)