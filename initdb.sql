insert into Queues values(0, 0, 0);
insert into Queues values(1, 0, 0);
insert into Queues values(2, 0, 0);
insert into Queues values(3, 0, 0);
insert into QSettings values (0, 'tgr4', 10, 'thomas,seattle', 'seattle,uw', 1, null, null, null, null, 'What is your name?');
insert into QSettings values (1, 'portland', 10, 'portland,oregon', 'portland,oregon', 1, null, null, null, null, 'What is the something velocity of a swallow?');
insert into QSettings values (2, 'bestqueueever', 10, 'best,favorite', 'moon', 1, null, null, null, null, 'Party size:');
insert into QSettings values (3, 'RedRobin', 10, 'RedRobin,restaurant,food,covington', 'covington', 1, null, null, null, null, 'Party size:');
insert into Users values (0, 0, 'Creator', 'Thomas', 'Rothschilds', 'tgr4@uw.edu', 'Creator');
insert into Users values (1, 0, 'Jim', 'Jim', 'Jim', 'jim@jim.jim', 'Jim');
insert into Users values (2, 0, 'boi', 'oh', 'hai', 'boi@oh.hai', 'boi');
insert into Permissions values (0, 0, 3);
insert into Permissions values (0, 1, 3);
insert into Permissions values (0, 2, 3);
insert into Permissions values (0, 3, 1);
insert into Permissions values (1, 0, 1);
insert into Permissions values (1, 1, 3);
insert into Permissions values (1, 2, 1);
insert into QIndex values(0, 0, (select ending_index from Queues where id=0), 'Thomas');
update Queues set ending_index=ending_index+1 where id=0;
insert into QHistory values (0, 0, 1400884418, null);
insert into QIndex values(1, 0, (select ending_index from Queues where id=0), 'Which kind of swallow?');
update Queues set ending_index=ending_index+1 where id=0;
insert into QHistory values (1, 0, 1400884419, null);
insert into QIndex values(2, 1, (select ending_index from Queues where id=1), '10');
update Queues set ending_index=ending_index+1 where id=1;
insert into QHistory values (2, 1, 1400884429, null);
insert into QIndex values(1, 1, (select ending_index from Queues where id=1), '1125');
update Queues set ending_index=ending_index+1 where id=1;
insert into QHistory values (1, 1, 1400884450, null);
