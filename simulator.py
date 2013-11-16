import consts
import agents
import random
from ticTacToe import game

def simulate(agent1, agent2, times):
    """Simulates a game between agent1 and agent2 a certain number of times
    ramdomly chooses agent1 or agent2 to be x each game

    returns statistics about the games"""
    
    data = { consts.UNOWNED: 0,\
             'O agent1': 0,\
             'X agent1': 0,\
             'O agent2': 0,\
             'X agent2': 0,\
             'agent1 drew X': 0,\
             'agent2 drew X': 0}
    
    #play times games and collect stats on the winners
    for x in range(times):
        am = {} # I am not proud of this
        if random.randint(0,1) == 0:
            winner = game(agent2, agent1, False)
            data['agent2 drew X'] += 1
            am['X'] = "agent2"
            am['O'] = "agent1"
        else:
            winner = game(agent1, agent2, False)
            data['agent1 drew X'] += 1
            am['X'] = "agent1"
            am['O'] = "agent2"

        if winner == consts.UNOWNED:
            data[winner] += 1
        else:
            winner = winner + " " + am[winner]
            data[winner] += 1

    return data

def displayStats(data, games):
    print "Cat's games: %d (%.1f%%)" % (data[consts.UNOWNED], (data[consts.UNOWNED] / float(games) * 100.0))
    print 'Agent 1:'
    print 'Overall win %: ' + str((data['X agent1'] + data['O agent1']) / float(games) * 100.0)
    print "X wins: %d (%.1f%%)" % (data['X agent1'], data['X agent1'] / float(games) * 100.0)
    print "O wins: %d (%.1f%%)" % (data['O agent1'], data['O agent1'] / float(games) * 100.0)
    print 'Agent 2:'
    print 'Overall win %: ' + str((data['X agent2'] + data['O agent2']) / float(games) * 100.0)
    print "X wins: %d (%.1f%%)" % (data['X agent2'], data['X agent2'] / float(games) * 100.0)
    print "O wins: %d (%.1f%%)" % (data['O agent2'], data['O agent2'] / float(games) * 100.0)


if __name__ == '__main__':
    #how many games to simulate
    games = 1000
    #simulate the games and collect data
    data = simulate(agents.stoogeAgent, agents.stoogeAgent, games)
    #display the data to screen
    displayStats(data, games)
