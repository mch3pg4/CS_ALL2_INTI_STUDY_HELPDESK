-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: all2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `usersubjects`
--

DROP TABLE IF EXISTS `usersubjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersubjects` (
  `user_id` varchar(45) NOT NULL,
  `level` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL,
  `school` text NOT NULL,
  `program` varchar(256) NOT NULL,
  `semester` varchar(256) NOT NULL,
  `subject1` varchar(256) NOT NULL,
  `subject2` varchar(256) NOT NULL,
  `subject3` varchar(256) NOT NULL,
  `subject4` varchar(256) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `usersubjects_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `userdata` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersubjects`
--

LOCK TABLES `usersubjects` WRITE;
/*!40000 ALTER TABLE `usersubjects` DISABLE KEYS */;
INSERT INTO `usersubjects` VALUES ('P12345678','Degree','2','School of Computing','BCSCUN','1','Programming & Algorithms','Mathematics for Computer Science','Database Systems','Select'),('P12345679','Degree','1','School of Computing','BCSCUN','2','Computer Architecture & Networks','Objected Oriented Programming','Mathematics for Computer Science','Programming & Algorithms');
/*!40000 ALTER TABLE `usersubjects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-01 15:34:51
