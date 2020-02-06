======
ff_bot
======

Intro:
======

This bot tweets out fantasy football updates. Follow at @analysteytan

.. image:: example.png
   :width: 584 px
   :height: 390 px

Note (2019 Season):
===================

FF Bot is still up and running (and better than ever), but the code in this Github repo is out of date. The latest version is stored privately in S3 and runs using AWS Lambda. No further updates will be made here, but this code demonstrates the general framework. Due to improved ESPN security measures, the bot now logs into ESPN via headless Chrome with Selenium.

Instructions:
=============
1. Edit the files in the config directory to change twitter login settings, the league settings and the sentence structure for the tweets.
2. Execute run_jobs.py

This will look for new transactions every minute and tweet them out if there are any. It will also tweet game recaps early Tuesday mornings.

Notes:
======

Concept, sentences, and Twitter profile pic courtesy of Josh Lurie.

Special thanks to Eytan Wallace for allowing us to use his likeness.