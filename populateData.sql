INSERT INTO Users VALUES
    (001, '2001-1-10'),
    (002, '2002-2-20'),
    (003, '2003-3-30');

INSERT INTO Artists VALUES
	(101, '2001-01-01'),
	(102, '2001-01-01'),
	(103, '2001-01-01'),
	(104, '2001-01-01'),
	(105, '2001-01-01');


INSERT INTO Albums VALUES
	(201, 101, 10, '2001-01-01', 'Rock'),
	(202, 102, 3, '2002-01-01', 'Pop'),
	(203, 103, 10, '2003-01-01', 'Electric'),
	(204, 103, 7, '2004-01-01', 'Classic'),
	(205, 103, 11, '2005-01-01', 'Dubstep'),
	(206, 104, 28, '2006-01-01', 'Rap'),
	(207, 105, 3, '2007-01-01', 'Electric'),
	(208, 105, 6, '2008-01-01', 'Country');

INSERT INTO Songs VALUES
	(001, 101, 201, 3, '1999-11-8', 'Rock'),
	(002, 101, 201, 3, '2000-9-19', 'Rock'),
	(003, 101, 201, 3, '1992-9-24', 'Rock'),
	(004, 102, 202, 3, '2012-6-20', 'Pop'),
	(005, 103, 203, 3, '2008-2-18', 'Electric'),
	(006, 103, 204, 3, '2015-2-1', 'Classic'),
	(007, 103, 204, 3, '2016-11-8', 'Classic'),
	(008, 103, 205, 3, '2018-9-9', 'Dubstep'),
	(009, 103, 205, 3, '2013-9-23', 'Dubstep'),
	(010, 103, 205, 3, '2004-7-22', 'Dubstep'),
	(011, 104, 206, 3, '2010-3-22', 'Rap'),
	(012, 104, 206, 4, '2003-4-3', 'Rap'),
	(013, 104, 206, 3, '2020-9-7', 'Rap'),
	(014, 104, 206, 3, '1992-11-8', 'Rap'),
	(015, 104, 206, 3, '1998-9-11', 'Rap'),
	(016, 104, 206, 3, '2017-9-3', 'Rap'),
	(017, 104, 206, 3, '2010-3-21', 'Rap'),
	(018, 105, 207, 3, '1996-9-24', 'Electric'),
	(019, 105, 208, 3, '2019-7-27', 'Country'),
	(020, 105, 208, 3, '2014-1-6', 'Classic');

INSERT INTO listensTo VALUES
    (003, 016),
    (002, 003),
    (002, 018),
    (003, 012),
    (003, 011),
    (001, 008),
    (001, 014),
    (002, 016),
    (001, 016);

