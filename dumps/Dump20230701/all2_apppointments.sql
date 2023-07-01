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
-- Table structure for table `apppointments`
--

DROP TABLE IF EXISTS `apppointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apppointments` (
  `idapppointments` int NOT NULL AUTO_INCREMENT,
  `stud_name` varchar(85) NOT NULL,
  `email` varchar(85) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `app_date` varchar(105) NOT NULL,
  `hour` varchar(45) NOT NULL,
  `minute` varchar(45) NOT NULL,
  `lecturer` varchar(45) NOT NULL,
  `description` varchar(255) NOT NULL,
  `status` varchar(45) NOT NULL DEFAULT 'Pending',
  `reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idapppointments`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `usersubjects` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apppointments`
--

LOCK TABLES `apppointments` WRITE;
/*!40000 ALTER TABLE `apppointments` DISABLE KEYS */;
INSERT INTO `apppointments` VALUES (1,'Gark Jun Feng','Garkjf@gmail.com','P12345678','16/06/2023','11','15','Lect1','Discuss about Logic Gates\n','Accepted','\n'),(2,'Tom','tom@gmail.com','P12345679','16/06/2023','11','30','Lect1','Discussion for Logic Gates\n','Rejected','Pls choose another time around 2-4pm\n');
/*!40000 ALTER TABLE `apppointments` ENABLE KEYS */;
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
