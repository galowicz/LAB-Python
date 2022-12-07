#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np
import csv
import pandas as pd


class Tasklist:
    def __init__(self):
        self.noOfTasks = 0
        self.Tasks = pd.DataFrame(
            columns=['Name', 'Note', 'Due Date', 'State'])
        self.fpath = 'tasklist.csv'

    def read_csv(self):
        try:
            self.Tasks = pd.read_csv(self.fpath)
            print(self.Tasks)
        except:
            self.add_task('example Task', "example note",
                          "1970-01-01", 'Ongoing')
            self.save_csv()
        # except NameError:
        # 	self.add_task('example Task', "example note", "1970-01-01", 'ongoing')
        # 	self.save_csv()
        # try:
        # 	with open(fpath,mode='r') as csv_file:

    def save_csv(self):
        self.Tasks.to_csv(self.fpath, index=False)

    def print(self):
        print(self.Tasks)

    def add_task(self, name: str, note: str, due_date: np.datetime64, state: str):
        row = {'Name': name, 'Note': note,
               'Due Date': due_date, 'State': state}
        self.Tasks = self.Tasks.append(row, ignore_index=True)
        self.noOfTasks += 1

    def remove_task(self, taskno: int):
        self.Tasks.drop(index=taskno)

    def mark_done(self, taskno: int):
        self.Tasks.loc[taskno, ['State']] = 'Done'

    def mark_undone(self, taskno: int):
        self.Tasks.loc[taskno, ['State']] = 'Ongoing'


if __name__ == '__main__':
    tasklist = Tasklist()
    tasklist.read_csv()
    repeat = 1
    try:
        print('type commands one per line\n To exit type "exit"')
        while (repeat):
            string = input('->')
            if string == 'print':
                tasklist.print()
            if string == 'add':
                name = input("Set Title:")
                note = input("Type additional notes:")
                due_date = input("type Due date:")
                tasklist.add_task(name, note, due_date, state='ongoing')
            if string == 'del':
                index = int(input("type number of task:"))
                try:
                    tasklist.remove_task(index)
                except ValueError:
                    print()
            if string == 'mark':
                index = int(input('type number of task:'))
                tasklist.mark_done(index)
            if string == 'unmark':
                index = int(input('type number of task:'))
                tasklist.mark_undone(index)
            if (string == 'exit'):
                repeat = 0
                tasklist.save_csv()

    except EOFError:
        repeat = 0
        tasklist.save_csv()
