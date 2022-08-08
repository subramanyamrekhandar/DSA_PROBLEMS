home_team = 1
def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam , awayTeam = competition

        winningTeam = homeTeam if result == home_team else awayTeam

        updateScores(winningTeam , 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam 
    
def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points 
