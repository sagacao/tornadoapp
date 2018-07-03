/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE DATABASE IF NOT EXISTS serverdb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

use serverdb;

DROP TABLE IF EXISTS `users_tb`;
CREATE TABLE `users_tb` (
    `userid` int(11) NOT NULL PRIMARY KEY,
    `useraccount` varchar(64) NOT NULL,
    `serverid` int(11) NOT NULL,
    `level` int(11) NOT NULL,
    `prof` int(11) NOT NULL,
    `sex` int(11) NOT NULL,
    INDEX  `user_tb_index` ( `userid`, `useraccount`, `serverid` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
