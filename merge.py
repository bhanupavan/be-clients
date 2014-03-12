#!/usr/bin/python

# Meger all the client branches to be-clients 'master'

print "Meger all the client branches to be-clients 'master'! started.....";

from subprocess import check_output
import sys


def get_merged_branches():
    ''' a list of merged branches, not couting the current branch or master '''
    raw_results = check_output('git branch ', shell=True)
    print raw_results
    return [b.strip() for b in raw_results.split('\n')
			if b.strip() and not b.startswith('*') and (b.strip() != 'master' or b.strip() != 'dummy') ]


def delete_branch(branch):
    return check_output('git branch -D %s' % branch, shell=True).strip()


if __name__ == '__main__':
    dry_run = '--confirm' not in sys.argv
    for branch in get_merged_branches():
        if dry_run:
            print branch
        else:
            print delete_branch(branch)
    if dry_run:
        print '*****************************************************************'
        print 'Did not actually delete anything yet, pass in --confirm to delete'
        print '*****************************************************************'
