--
-- Table structure for table `word`
--

DROP TABLE IF EXISTS `word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `word` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `English` text COLLATE utf8_bin,
  `Chinese` text COLLATE utf8_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1436 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;