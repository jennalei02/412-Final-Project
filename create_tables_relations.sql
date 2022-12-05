/*
Authors: Leon Kwong, Zack Guajardo, Jenna Cooley
Group 1
CSE412
*/
 
/* Entity Sets */
 
/* Users: */
CREATE TABLE Users(userID INTEGER,
    dateOfBirth VARCHAR(30),
    PRIMARY KEY (userID));

/* Artists: */
 
CREATE TABLE Artists(artistID INTEGER,
    dateOfBirth VARCHAR(30),
    PRIMARY KEY(artistID));
 
/* Albums: */
CREATE TABLE Albums(albumID INTEGER,
    artistID INTEGER,
    playTime INTEGER,
    releaseDate VARCHAR(30),
    genre VARCHAR(30),
    PRIMARY KEY(albumID));
	
/* Songs: */
CREATE TABLE Songs(songID INTEGER,
    artistID INTEGER,
    albumID INTEGER,
    playTime INTEGER,
    releaseDate VARCHAR(30),
    genre VARCHAR(30),
    PRIMARY KEY(songID),
    FOREIGN KEY (artistID) REFERENCES Artists,
    FOREIGN KEY (albumID) REFERENCES Albums);

/* Relationship Sets: */
 
CREATE TABLE ListensTo(userID INTEGER,
    songID INTEGER,
    PRIMARY KEY (songID, userID),
    FOREIGN KEY (songID) REFERENCES  Songs,
    FOREIGN KEY (userID) REFERENCES Users);