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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `idbooks` int NOT NULL AUTO_INCREMENT,
  `bookname` varchar(200) NOT NULL,
  `bookcategory` varchar(45) NOT NULL,
  `bookfile` longtext NOT NULL,
  `bookcover` longtext NOT NULL,
  PRIMARY KEY (`idbooks`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'The Design of Everyday Things','Design','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/The-Design-of-Everyday-Things-Don-Norman.pdf','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/The-Design-of-Everyday-Things-Don-Norman.png'),(3,'C++ From Control Structures through Objects','Computer Science','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/GaddisStartingOut.pdf','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/GaddisStartingOut.png'),(4,'Computer Organization & Architecture','Computer Science','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/computer-organization-and-architecture.pdf','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/computer-organization-and-architecture.png'),(5,'Object Oriented Programming in C++','Computer Science','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/ObjectOrientedProgramminginC4thEdition.pdf','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/ObjectOrientedProgramminginC4thEdition.png'),(6,'Discrete Mathematics and its Applications','Maths','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/rosen_discrete_mathematics_and_its_applications_7th_edition.pdf','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/rosen_discrete_mathematics_and_its_applications_7th_edition.png'),(7,'Computer Architecture','Computer Science','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/Computer Architecture, Sixth Edition_ A Quantitative Approach ( PDFDrive ).pdf','C:/Users/mch/Desktop/CS_ALL2_INTI_STUDY_HELPDESK/books/Computer Architecture, Sixth Edition_ A_Quantitative_Approach.png');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-01 15:34:50
