/*Get the specific user's total playtime of songs, in this case userID = 001*/
SELECT SUM(playTime) FROM Users, Songs, ListensTo WHERE Users.userID = '001' AND Users.userID = ListensTo.userID AND ListensTo.songID = Songs.SongID

/*Search for all songs in an album, in this case albumID = 201*/
SELECT songID FROM Songs, Albums WHERE Songs.albumID = Albums.albumID AND Songs.albumID = '201'

/*List all the songs a artists creates*/
SELECT songID FROM Songs, Artists WHERE Songs.artistID = Artists.artistID AND Artists.artistID = 104

/*Count how many artists and albums the user listens to*/
/*Artists*/
WITH Table1 AS (SELECT * FROM Artists NATURAL JOIN Songs) SELECT COUNT(distinct(artistID)) from Table1, ListensTo , Users where Table1.songID =  ListensTo.songID AND ListensTo.userID = Users.userID AND Users.userID = 1
/*Albums*/
SELECT COUNT(DISTINCT(Songs.albumID)) FROM Songs, Users, ListensTo WHERE Users.userID = ListensTo.userID AND ListensTo.songID = Songs.songID AND Users.userID = 3

/*Number of songs per selected genre*/
SELECT COUNT(DISTINCT(Songs)) FROM Songs WHERE Songs.genre = 'Rap'

/*Test Insert Update, and Delete Functions */
/*Insert*/
INSERT INTO Albums VALUES(209, 101, 8, '2007-11-08', 'Dubstep');
INSERT INTO Songs VALUES(022, 101, 209, 7, '2022-10-28', 'K-POP');
INSERT INTO ListensTo VALUES(003, 022);

UPDATE ListensTo SET userID = 2 WHERE songID = 022 /*Changes last insert statement to be user 2 instead of 3. Test with the album command in line 14. Result should be 2 instead of 3*/

DELETE FROM ListensTo WHERE songID = 22
DELETE FROM Songs WHERE songID = 22