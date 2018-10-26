twitter_char_limit = 280

### Transactions
team1 = "team1_template"
team2 = "team2_template"
player1 = "player1_template"
position1 = "position1_template"
player2 = "player2_template"
position2 = "position2_template"
auction = "auction_template"

trade_sentences = [
'ESPN is now reporting that ' + team1 + ' traded ' + player1 + ' to ' + team2 + ' in exchange for ' + player2 + '. ESPN has officially become fake news, because there is no way even ' + team1 + ' would be so inept to make a trade like that.',
'The great heists of BTLMF trade history is spectacular: Kyle Rudolph for AJ Green, Marvin Jones for Todd Gurley, Doug Martin for Michael Thomas. Add this one to the list: ' + team1 + ' gets ' + player2 + ' from ' + team2 + ' for just ' + player1 + '.',
'You can tell that ' + team1 + ' and ' + team2 + ' are not friends. If they were friends, there is no way ' + team1 + ' would have the heart to steal ' + player2 + ' from ' + team2 + ' for merely ' + player1 + '.',
'Until today, I have not seen a fair and balanced trade this year. It looks that that will be true tomorrow as well. ' + team1 +  ' just hoodwinked ' + team2 + ' by sending ' + player1 + ' in exchange for ' + player2 + '.',
'At this point, I feel bad for ' + team1 + '. People see a dying team run by an incompetent owner and, like vultures, prey on its weakness. That just what ' + team2 + ' did when he convinced ' + team1 + ' to trade ' + player1 + ' for ' + player2 + '.',
'I have 9-1-1 dialed on my phone and am about to press call, because I have a ROBBERY to report. ' + team1 + ' just got ' + player2 + ' from ' + team2 + ' for only ' + player1 + '. Clearly illegal, likely to be vetoed.',
'All signs point to collusion in the latest BTLMF trade. Apparently, ' + team1 + ' is willing to send ' + player1 + ' to ' + team2 + ' for ' + player2 + ' on his own free will. I call BS.',
'BREAKING NEWS: POTENTIAL BLOCKBUSTER TRADE OF THE YEAR. ' + team1 + ' sends ' + player1 + ' to ' + team2 + ' in a deal involving ' + player2 + '. I did not think ' + team1 + ' had the huevos to pull this one off.',
'IT\'S TRADING SZN Y\'ALL. ' + team1 + ' and ' + team2 + ' shake it up by swapping ' + player1 + ' for ' + player2 + '.',

]

# player2 is added player
# player1 is dropped player
add_drop_waiver_sentences =[
'After naming himself, \"The best ' + position1 + ' on the team,\" ' + player1 + ' has been waived. ' + team1 + ' spends ' + auction + ' to sign ' + player2 + ' in the corresponding move.',
'I am HYPED up: ' + team1 + ' spends ' + auction + ' to sign ' + player2 + ' and release ' + player1 + '. #FantasyFootballIsTheOpiumOfTheMasses',
'After finding out ' + team1 + ' spent ' + auction + ' to waive him for ' + player2 + ', ' + player1 + ' said, \"Every form of society has been based on the antagonism of oppressing and oppressed classes.\" Actually nvm that was Karl Marx.',
'THE PROLETARIANS HAVE NOTHING TO LOSE BUT THEIR CHAINS! I know what you\'re thinking, \"stick to football.\" Ok. ' + team1 + ' spends ' + auction + ' to add ' + player2 + ' and drop ' + player1 + '.',
'Can\'t ask for a better birthday present: ' + player2 + ' signed to ' + team1 + '\'s roster. Unfortunately, it was actually ' + player1 + '\'s birthday, who was cut.',
team1 + '\'s coach\'s message to ' + player2 + ' after signing him, \"It\'s time to earn your bread son.\" It seems like ' + player1 + ' only earned matzah this season, as he\'s been cut.',
player1 + ' just texted me LIVID. He\'s been informed by ' + team1 + ' that he has been waived to make room for ' + player2 + '.',
'i\'m at a abr right now because it izs late anbd i can tweet from wherevre li wmant. just wanted ot let you konow that ' + team1 + ' addedn ' + player2 + ', dropped ' + player1 + ' , and srpent ' + auction + ' on the movei.',
'I really like ' + team1 + '\'s move to add ' + player2 + ' and drop ' + player1 + ' for ' + auction + '. But I\'m a bot who tweets pre-written template sentences, so what do I know?',
'This past weekend, ' + team1 + '\'s owner attended ' + player1 + '\'s housewarming party for his new multi-million dollar home. Now that property is already back on the market after ' + player1 + ' was cut for ' + player2 + ' today.',
team1 + '\'s decision to add ' + player2 + ' and drop ' + player1 + ' really does improve their roster. Whether to says more about ' + player2 + ' or their roster is up to you.',
'Despite opinions by so-called NFL analysts, I actually think the addition of ' + player2 + ' to ' + team1 + ' is a great addition to the roster. They also dropped ' + player1 + ' and spent ' + auction + ' to do it.',
'Dropping ' + player1 + ' for ' + player2 + ' was a bad move by ' + team1 + '. Change my mind. #ComeAtMeStevenCrowder',
'The ghost of Jacob Pardo is alive within ' + team1 + ', demonstrated by their latest roster blunder: dropping ' + player1 + ' for ' + player2 + '. They spent ' + auction + ' on the move.',
player1 + ' has been promoted to the starting lineup. Just kidding, he\'s been waived and ' + team1 + ' signs ' + player2 + '. They spent ' + auction + ' on the roster change.',
'Does ' + team1 + ' really need a ' + position2 + '? Yes. Will ' + player2 + ' fill that need? I don\'t think so, but ' + team1 + ' clearly does as they dropped ' + player1 + ' and ' + auction + ' for him.',
'9/10 people think ' + player2 + ' is not worth ' + auction + '. Clearly, ' + team1 + ' is the outlier here as they signed him and cut ' + player1 + '.',
'I like to think that more prople know who I am more than know who ' + player2 + ' is. That changed today as ' + team1 + ' signed him and cut ' + player1 + ' for ' + auction + '.',
'I\'m not one to sensationlize meaningless news, so I won\'t: ' + team1 + ' cuts ' + player1 + ' and signs ' + player2 + ' for ' + auction + '. An exceedingly lateral move for this squad.',
'Awkward moment in the ' + team1 + ' facilities today. After ' + player2 + ' signed with the team from waivers, he received a congratulations text from ' + player1 + '. ' + player2 + ' then had to inform ' + player1 + ' that he was cut in the move.',
'First Eric drops Keke Coutee the day before Will Fuller tears his ACL. And now ' + team1 + ' drops ' + player1 + ' the week before I predict he goes off. More than that, he only added ' + player2 + ' in exchange and spent ' + auction + ' on the move.',
'I have seen hundreds if not thousands of waiver acquisitions in my time reporting, but I have never seen one as meaningless or uninteresting as ' + team1 + ' dropping ' + player1 + ' and adding ' + player2 + ' for ' + auction + '.',
'The fact that he would spend ' + auction + ' and drop ' + player1 + ' to get ' + player2 + ' tells me that he is locked up somewhere and someone else is controlling his team. Don\'t worry ' + team1 + ' help is on the way.',
'I\'m not going to say that ' + team1 + '\'s ' + position2 + 's are trash, but I will say that spending ' + auction + ' and dropping ' + player1 + ' to get ' + player2 + ' isn\'t going to help the situation.',
team1 + ' definitely watched the FS1 Undisputed segment where @ShannonSharpe said ' + player2 + ' will finish as a top 5 ' + position2 + ' this season. That\'s the only reason he would drop ' + player1 + 'and spend ' + auction + ' on this move.',
team1 + ' dropped ' + player1 + ' for ' + player2 + '. @RealSkipBayless just asked his followers if this move can win ' + team1 + ' the title. The answer Skip, is a resounding no.',
'Every week, I have to wait up way past my bedtime to be the first to report waivers. Can you really not wait until the sun rises to hear that ' + team1 + ' dropped ' + player1 + ' for ' + player2 + ' and ' + auction + '? #LookingForANineToFive',
team1 + ' spent ' + auction + ' acquiring ' + player2 + ' and dropping ' + player1 + '. I am willing to bet ' + team1 + ' ' + auction + ' in real US dollars that he will end up regretting this move.',
'Fans are outside of ' + team1 + '\'s facilties chanting \"Heega kamini soma kanakra heega.\" They believe waiver add ' + player2 + ' will win them the championship. If they are right, ' + team1 + ' just spent ' + player1 + ' and ' + auction + ' for the title.',
'I can confirm earlier report by @JayGlazer that ' + team1 + ' will sign ' + position2 + ' ' + player2 + ' to replace ' + player1 + ' on roster. They made the highest bid with ' + auction + '.',
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
team1 + ' on ' + player2 + ' yesterday: ‘He did not make the team because we believe in ' + player1 + '. Today, ' + team1 + ' waive ' + player1 + ' to make room for ' + player2 + '. ' + auction + ' spent in the move.',
team1 + ' officially release ' + position1 + ' ' + player1 + ' to make room for ' + player2 + '. ' + auction + ' spent in the move.' ,
team1 + ' sign free agent ' + position2 + ' ' + player2 + ' and release ' + position1 + ' ' + player1 + '. ' + player2 + ' gets the nod over several others in for tryouts in last few days. They made the highest bid with ' + auction + '.',
team1 + ' release ' + position1 + ' ' + player1 + ' to make room for ' + position2 + ' ' + player2 + ' on the active roster. They made the highest bid with ' + auction + '.',
team1 + ': ' + player2 + ' "was a guy we really liked a couple of weeks ago," leading to the decision to sign him. This also led to the release of ' + player1 + '. They made the highest bid with ' + auction + '.',
'Free Agency update: ' + team1 + ' sign ' + player2 + ' to address ' + position2 + ' shortage, place ' + player1 + ' on waivers. They made the highest bid with ' + auction + '.',
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

# player2 is added player
# player1 is dropped player
add_drop_sentences = [
'I can confirm earlier report by @JayGlazer that ' + team1 + ' will sign ' + position2 + ' ' + player2 + ' to replace ' + player1 + ' on roster.' ,
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
team1 + ' on ' + player2 + ' yesterday: ‘He did not make the team because ' + player1 + ' came on.’ Today, ' + team1 + ' waive ' + player1 + ' to make room for ' + player2 + '.',
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

def clean_sentence(sentence, team1='', team2='', player1='', position1='', player2='', position2='', auction='', week_num='', winning_team='', winning_owner='', winning_score='', winning_wins='', winning_losses='', losing_team='', losing_owner='', losing_score='', losing_wins='', losing_losses=''):
    new_sentence = sentence.replace("team1_template", team1)
    new_sentence = new_sentence.replace("team2_template", team2)
    new_sentence = new_sentence.replace("player1_template", player1)
    new_sentence = new_sentence.replace("position1_template", position1)
    new_sentence = new_sentence.replace("player2_template", player2)
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
