# Print out all the state names from the csv# Coded in the "object-oriented" stylefrom electiondata import ElectionResultsfilename = '2012_US_election_state.csv'results = ElectionResults(filename)results.load()print "Opened file:"state_names = results.states()for state in state_names:    print "  "+stateprint "done ("+str(results.state_count())+" lines)"print "Vote Count" +str(results.vote_count())