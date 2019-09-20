
better-music-fix
================

manages playlists for large groups of people in a communal settings. instead of allowing a single person to monopolize DJ'ing, the collective opinions of the group are synthesized in an upvote/downvote system. 

or it's like, reddit for youtube playlists

made at hackmit 2019 ❤️

known issues
============

- inconsistent playlist state:
    - hosted on heroku which scales servers according to load
    - the app keeps the playlist in local memory so we get multiple playlist states for each server
    - should move to postgresql but mvp for hackathon, you know how it is
