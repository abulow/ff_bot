twitter_char_limit = 280

### Transactions
team1 = "team1_template"
team2 = "team2_template"
position1 = "position1_template"
player1 = "player1_template"
player2 = "player2_template"
position2 = "position2_template"
auction = "auction_template"

trade_sentences = [
'Sources to ESPN: ' + team1 + ' and ' + team2 + ' have an agreement in place on a trade involving ' + player1 + ' to ' + team2 + '. More details available on ESPN fantasy app.',
team1 + ' traded for ' + team2 + ' locker room cancer ' + player2 + ', Howie Roseman confirms. More details available on ESPN fantasy app.',
team1 + ' acquired ' + player2 + ' in a trade with ' + team2 + ' in exchange for ' + player1 + '. More details available on ESPN fantasy app.',
player1 + ' trade from ' + team1 + ' to ' + team2 + ' is official. Expected to talk to reporters at the podium this afternoon at 3 p.m. More details available on ESPN fantasy app.',
'Source: ' + team1 + ' trade ' + player1 + ' to ' + team2 + '. More details available on ESPN fantasy app.',
'Source: ' + team1 + ' have traded for ' + team2 + ' stud ' + player2 + '. ' + team1 + ' was also interested in him last year. More details available on ESPN fantasy app.', 
]

add_drop_waiver_sentences = [
'I can confirm earlier report by @JayGlazer that ' + team1 + ' will sign former ' + position2 + ' ' + player2 + ' to replace ' + player1 + ' on roster. They made the highest bid with ' + auction + '.',
'The roster churn continues. ' + team1 + ' release ' + position1 + ' ' + player1 + ' to make room for ' + position2 + ' ' + player2 + '. ' + team1 + ' won with an aggressive bid of ' + auction + '.',
position2 + ' ' + player2 + ' passes physical. ' + team1 + ' release ' + position1 + ' ' + player1 + ' to clear a roster spot. The final bid came out to ' + auction + '.' ,
'Sources: Free-agent ' + position2 + ' ' + player2 + ' is working out for ' + team1 + ' today. Barring an unexpected poor workout, ' + team1 + ' will offer ' + player2 + ' a deal to sign and replace ' + player1 + '. They are planning to spend ' + auction + ' for the acquisition.' ,
team1 + ' brought out the big bucks today, signing ' + position2 + ' ' + player2 + '  with a ' + auction + ' bid and waiving ' + position1 + ' ' + player1 + ' in the process.' ,
team1 + ' release ' + position2 + ' ' + player2 + '. This came with the signing of ' + position1 + ' ' + player1 + ' at the end of today’s press conference. They also announced their final bid: ' + auction + '.',
player2 + ' plans to sign a one year deal with ' + team1 + ' today, per source. ' + player1 + ' is released to make room. ' + team1 + ' spent ' + auction + ' to get him.' ,
team1 + ' sign ' + position2 + ' ' + player2 + '. This means the end of the road for ' + player1 + ', who was cut. ' + auction + ' ended up shedding ' + auction + ' of their waiver budget in the move.' ,
'I can confirm earlier report by @ProFootballTalk that free agent ' + position2 + ' ' + player2 + ' will sign with ' + team1 + ' after passing a physical. ' + player1 + ', who failed his physical, will be waived. The winning bid was estimated to be at ' + auction + '.' ,
'Official. ' + team1 + ' sign ' + player2 + ' and waive ' + player1 + '. ' + auction + ' spent on the transaction.' ,
'According to ESPN\'s John Clayton, ' + team1 + ' sign ' + player2 + '. Not happy news for everyone, as ' + player1 + ' is cut. At the end of the day, this is a business. ' + team1 + ' spent ' + auction + ' on this roster move.' ,
team1 + ' officially release ' + position1 + ' ' + player1 + ' to make room for free-agent ' + position2 + ' ' + player2 + '. This move cost them ' + auction + '.' ,
team1 + ' sign ' + position2 + ' ' + player2 + ', waive ' + position1 + ' ' + player1 + '. The front office decided to spend ' + auction + ' on the roster change.', 
team1 + ' on ' + player2 + ' last week: ‘He did not make the team because we believe in ' + player1 + '.' ,
'Six days later, ' + team1 + ' waive ' + player1 + ' to make room for ' + player2 + '. ' + auction + ' spent in the move.',
team1 + ' officially release ' + position1 + ' ' + player1 + ' to make room for ' + player2 + '. ' + auction + ' spent in the move.' ,
team1 + ' sign free agent ' + position2 + ' ' + player2 + ' and release ' + position1 + ' ' + player1 + '. ' + player2 + ' gets the nod over several others in for tryouts in last 12 days. They made the highest bid with ' + auction + '.',
team1 + ' release ' + position1 + ' ' + player1 + ' to make room for ' + position2 + ' ' + player2 + ' on the active roster. They made the highest bid with ' + auction + '.',
team1 + ': ' + player2 + ' "was a guy we really liked a couple of weeks ago," leading to the decision to sign him. This also led to the release of ' + player1 + '. They made the highest bid with ' + auction + '.',
'Updated. ' + team1 + ' sign ' + player2 + ' to address ' + position2 + ' shortage, place ' + player1 + ' on waivers. They made the highest bid with ' + auction + '.',
team1 + ' quickly move on from ' + player1 + ', will sign ' + player2 + ', who was part of ' + position2 + ' tryouts today, source confirms. They made the highest bid with ' + auction + '.',
team1 + ' said they’re adding ' + player2 + ' from waivers to fill spot vacated by ' + player1 + ' release. Left open the possibility of ' + player1 + ' returning to team. They made the highest bid with ' + auction + '.',
team1 + ' said decision to release ' + player1 + ' was more about the guy that was available. ' + player2 + ' signing to replace. ' + team1 + ' spent ' + auction + ' on this roster move.',
team1 + ' waive ' + position1 + ' ' + player1 + ', sign ' + player2 + '. ' + team1 + ' won with an aggressive bid of ' + auction + '.',
'With recent team roadbumps, ' + team1 + ' sign ' + player2 + ' from free agency, waive ' + player1 + '. ' + team1 + ' spent ' + auction + ' on this roster move.',
'Per league transaction release, ' + team1 + ' has signed ' + player2 + ' and waived ' + position1 + ' ' + player1 + '. ' + team1 + ' spent ' + auction + ' on this roster move.',
team1 + ' has officially announced the release of ' + position1 + ' ' + player1 + ' and the addition of ' + position2 + ' ' + player2 + '. ' + auction + ' spent on the transaction.',
position1 + ' ' + player1 + '\'s release listed with \'failure to disclose physical condition\' on ' + team1 + '\'s transaction report. ' + player2 + ' was brought in to fill the empty roster spot. ' + auction + ' spent on the transaction.',
'Can confirm ' + team1 + ' are expected to sign ' + position2 + ' ' + player2 + ' to replace ' + position1 + ' ' + player1 + '. ' + auction + ' spent on the transaction.',
team1 + ' are expected to sign ' + position2 + ' ' + player2 + ' from waivers and release ' + position1 + ' ' + player1 + ' to address ' + position2 + ' depth. ' + auction + ' spent on the transaction.',
team1 + ' announced the release of ' + player1 + ' and have added ' + position2 + ' ' + player2 + ' to their roster. ' + auction + ' spent on the transaction. ' + team1 + ' spent ' + auction + ' on this roster move.',
team1 + ' said "everything" was a factor when asked if contract was a factor with the release of ' + position1 + ' ' + player1 + '.  Said knee had held up. ' + player2 + ' was signed in the corresponding roster move. ' + team1 + ' spent ' + auction + ' on this roster move.',
team1 + ' officially place ' + position1 + ' ' + player1 + ' on waivers, sign ' + position2 + ' ' + player2 + '. ' + team1 + ' spent ' + auction + ' on this roster move.',
'RT @JasonLaCanfora: ' + team1 + ' was high on ' + player2 + '. He will sign there. ' + player1 + ' is the player to be released in the move. ' + team1 + ' spent ' + auction + ' on this roster move.',
]

add_drop_sentences = [
'I can confirm earlier report by @JayGlazer that ' + team1 + ' will sign former ' + position2 + ' ' + player2 + ' to replace ' + player1 + ' on roster.' ,
'The roster churn continues. ' + team1 + ' release ' + position1 + ' ' + player1 + ' to make room for ' + position2 + ' ' + player2 + '.' ,
position2 + ' ' + player2 + ' passes physical. ' + team1 + ' release ' + position1 + ' ' + player1 + ' to clear a roster spot.' ,
'Sources: Free-agent ' + position2 + ' ' + player2 + ' is working out for ' + team1 + ' today. Barring an unexpected poor workout, ' + team1 + ' will offer ' + player2 + ' a deal to sign and replace ' + player1 + '.' ,
team1 + ' sign ' + position2 + ' ' + player2 + ' and waive ' + position1 + ' ' + player1 + '.' ,
team1 + ' release ' + position2 + ' ' + player2 + '. This came with the signing of ' + position1 + ' ' + player1 + ' at the end of today’s press conference.',
player2 + ' plans to sign a one year deal with ' + team1 + ' today, per source. ' + player1 + ' is released to make room.',
team1 + ' sign ' + position2 + ' ' + player2 + '. This means the end of the road for ' + player1 + ', who was cut.',
'I can confirm earlier report by @ProFootballTalk that free agent ' + position2 + ' ' + player2 + ' will sign with ' + team1 + ' after passing a physical. ' + player1 + ', who failed his physical, will be waived.',
'Official. ' + team1 + ' sign ' + player2 + ' and waive ' + player1 + '.',
'According to ESPN\'s John Clayton, ' + team1 + ' sign ' + player2 + '. Not happy news for everyone, as ' + player1 + ' is cut. At the end of the day, this is a business.',
team1 + ' officially release ' + position1 + ' ' + player1 + ' to make room for free-agent ' + position2 + ' ' + player2 + '.',
team1 + ' sign ' + position2 + ' ' + player2 + ', waive ' + position1 + ' ' + player1 + '.',
team1 + ' on ' + player2 + ' last week: ‘He did not make the team because ' + player1 + ' came on.’ Six days later, ' + team1 + ' waive ' + player1 + ' to make room for ' + player2 + '.',
team1 + ' officially release ' + position1 + ' ' + player1 + ' to make room for ' + player2 + '.',
team1 + ' sign free agent ' + position2 + ' ' + player2 + ' and release ' + position1 + ' ' + player1 + '. ' + player2 + ' gets the nod over several others in for tryouts in last 12 days.',
team1 + ' release ' + position1 + ' ' + player1 + ' to make room for ' + position2 + ' ' + player2 + ' on the active roster.',
team1 + ': ' + player2 + ' "was a guy we really liked a couple of weeks ago," leading to the decision to sign him. This also led to the release of ' + player1 + '.',
'Updated. ' + team1 + ' sign ' + player2 + ' to address ' + position2 + ' shortage, place ' + player1 + ' on waivers.',
team1 + ' quickly move on from ' + player1 + ', will sign ' + player2 + ', who was part of ' + position2 + ' tryouts today, source confirms.',
team1 + ' said they’re adding ' + player2 + ' from waivers to fill spot vacated by ' + player1 + ' release. Left open the possibility of ' + player1 + ' returning to team.',
team1 + ' said decision to release ' + player1 + ' was more about the guy that was available. ' + player2 + ' signing to replace.',
team1 + ' waive ' + position1 + ' ' + player1 + ', sign ' + player2 + '.',
'With recent team roadbumps, ' + team1 + ' sign ' + player2 + ' from free agency, waive ' + player1 + '.',
'Per league transaction release, ' + team1 + ' has signed ' + player2 + ' and waived ' + position1 + ' ' + player1 + '.',
team1 + ' has officially announced the release of ' + position1 + ' ' + player1 + ' and the addition of ' + position2 + ' ' + player2 + '.',
position1 + ' ' + player1 + '\'s release listed with \'failure to disclose physical condition\' on ' + team1 + '\'s transaction report. ' + player2 + ' was brought in to fill the empty roster spot.',
'Can confirm ' + team1 + ' are expected to sign ' + position2 + ' ' + player2 + ' to replace ' + position1 + ' ' + player1 + '.',
team1 + ' are expected to sign ' + position2 + ' ' + player2 + ' from waivers and release ' + position1 + ' ' + player1 + ' to address ' + position2 + ' depth.',
team1 + ' announced the release of ' + player1 + ' and have added ' + position2 + ' ' + player2 + ' to their roster.',
team1 + ' said "everything" was a factor when asked if contract was a factor with the release of ' + position1 + ' ' + player1 + '.  Said knee had held up. ' + player2 + ' was signed in the corresponding roster move.',
team1 + ' officially place ' + position1 + ' ' + player1 + ' on waivers, sign ' + position2 + ' ' + player2 + '.',
'RT @JasonLaCanfora: ' + team1 + ' was high on ' + player2 + '. He will sign there. ' + player1 + ' is the player to be released in the move.',
]

add_sentences = [
'' + player1 + ' plans to sign a one year deal with ' + team1 + ' today, per source.' ,
'' + team1 + ' sign ' + position1 + ' ' + player1 + '.' ,
'I can confirm earlier report by @ProFootballTalk that free agent ' + position1 + ' ' + player1 + ' will sign with ' + team1 + ' after passing a physical.' ,
'Official. ' + team1 + ' sign ' + player1 + '.' ,
'According to ESPN\'s John Clayton, ' + team1 + ' sign ' + player1 + ' as new ' + position1 + '.' ,
]

drop_sentences = [
'For those wondering about ' + team1 + '’s ' + player1 + ' release, he was replaced as the ' + position1 + ' this year because of inconsistencies at the position. ' + team1 + ' also had strong words for ' + player1 + ' after his most recent missed opportunity.',
team1 + ' release ' + position1 + ' ' + player1 + '.',
'Release of ' + player1 + ' signals ' + position1 + ' revamp for ' + team1 + '.',
team1 + ' releases ' + position1 + ' ' + player1 + ' after failed physical.',
team1 + ' tried to trade ' + position1 + ' ' + player1 + '. No takers. So, he was cut, per source.',
team1 + ' releases ' + position1 + ' ' + player1 + '. Guess they feel good about their ' + position1 + ' situation',
team1 + ' releases ' + position1 + ' ' + player1 + '. Tough break for a west coast kid. Played well in a limited role last year',
]

### End of Transactions


### Game Recaps
week_num = "week_num_template"
winning_team = "winning_team_template"
winning_owner = "winning_owner_template"
winning_score = "winning_score_template"
winning_wins = "winning_wins_template"
winning_losses = "winning_losses_template"
losing_team = "losing_team_template"
losing_owner = "losing_owner_template"
losing_score = "losing_score_template"
losing_wins = "losing_wins_template"
losing_losses = "losing_losses_template"

score_sentences = [
winning_team + ' defeated ' + losing_team + ' ' + winning_score + '-' + losing_score + '. ' + losing_owner + ' remarked, "THEY ARE WHO WE THOUGHT THEY WERE," later adding that his team "let them off the hook."',
'To no one\'s surprise, ' + winning_team + ' dominated ' + losing_team + ' ' + winning_score + '-' + losing_score + '.',
losing_team + ' was outclassed by ' + winning_team + ' ' + winning_score + '-' + losing_score + '. ' + winning_owner + ': "We can beat anybody in this league."',
winning_team + ' took down ' + losing_team + ' ' + winning_score + '-' + losing_score + '. Nobody wants to face ' + winning_team + ' right now.',
losing_team + ' lost to ' + winning_team + ' ' + winning_score + '-' + losing_score + '. Asked about his team\'s playoff chances, ' + losing_owner + ' said, "I just hope we can win a game."'
]
score_sentences = ['Week ' + week_num + ' Game Recap: ' + x for x in score_sentences]
score_sentences = [x + ' ' + winning_team + ' improves to ' + winning_wins + '-' + winning_losses + '. ' + losing_team + ' falls to ' + losing_wins + '-' + losing_losses + '.' for x in score_sentences]
### End of Game Recaps

def clean_sentence(sentence, team1='', team2='', player1='', player2='', position1='', position2='', auction='', week_num='', winning_team='', winning_owner='', winning_score='', winning_wins='', winning_losses='', losing_team='', losing_owner='', losing_score='', losing_wins='', losing_losses=''):
    new_sentence = sentence.replace("team1_template", team1)
    new_sentence = new_sentence.replace("team2_template", team2)
    new_sentence = new_sentence.replace("player1_template", player1)
    new_sentence = new_sentence.replace("player2_template", player2)
    new_sentence = new_sentence.replace("position1_template", position1)
    new_sentence = new_sentence.replace("position2_template", position2)
    new_sentence = new_sentence.replace("auction_template", auction)
    new_sentence = new_sentence.replace("week_num_template", week_num)
    new_sentence = new_sentence.replace("winning_team_template", winning_team)
    new_sentence = new_sentence.replace("winning_owner_template", winning_owner)
    new_sentence = new_sentence.replace("winning_score_template", winning_score)
    new_sentence = new_sentence.replace("winning_wins_template", winning_wins)
    new_sentence = new_sentence.replace("winning_losses_template", winning_losses)
    new_sentence = new_sentence.replace("losing_team_template", losing_team)
    new_sentence = new_sentence.replace("losing_owner_template", losing_owner)
    new_sentence = new_sentence.replace("losing_score_template", losing_score)
    new_sentence = new_sentence.replace("losing_wins_template", losing_wins)
    new_sentence = new_sentence.replace("losing_losses_template", losing_losses)
    new_sentence = new_sentence.replace('  ', ' ')
    new_sentence = new_sentence.replace(' .', '.')
    return new_sentence