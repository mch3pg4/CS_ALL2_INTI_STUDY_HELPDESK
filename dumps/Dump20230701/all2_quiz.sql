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
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz` (
  `idquiz` int NOT NULL AUTO_INCREMENT,
  `subj_name` varchar(45) NOT NULL,
  `chap_name` varchar(85) NOT NULL,
  `ques_title` varchar(105) NOT NULL,
  `opA` varchar(45) NOT NULL,
  `opB` varchar(45) NOT NULL,
  `opC` varchar(45) NOT NULL,
  `opD` varchar(45) NOT NULL,
  `correct_op` varchar(45) NOT NULL,
  PRIMARY KEY (`idquiz`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES (1,'Computer Architecture & Networks','1-Machine Level Representation of Data','Which of the following operations is/are performed by the ALU?','Data manipulation','Exponential','Square root','All of the above','D'),(2,'Computer Architecture & Networks','1-Machine Level Representation of Data','Which of the following is not considered as a peripheral device?','CPU','Keyboard','Monitor','All of the above','A'),(3,'Computer Architecture & Networks','1-Machine Level Representation of Data','The address in the main memory is known as ','Logical address','Physical address','Memory address','None of the above','B'),(4,'Computer Architecture & Networks','1-Machine Level Representation of Data','Subtraction in computers is carried out by ','1\'s complement','2\'s complement','3\'s complement','9\'s complement','B'),(5,'Computer Architecture & Networks','1-Machine Level Representation of Data','In which of the following form the computer stores its data in memory?','Hexadecimal form','Octal form','Binary form','Decimal form','C');
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
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
