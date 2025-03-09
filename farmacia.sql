/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.5.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: farmacia
-- ------------------------------------------------------
-- Server version	11.5.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `Empleado`
--

DROP TABLE IF EXISTS `Empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Empleado` (
  `IDempleado` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) DEFAULT NULL,
  `documento` char(8) DEFAULT NULL,
  `sucursal` char(4) DEFAULT NULL,
  PRIMARY KEY (`IDempleado`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empleado`
--

LOCK TABLES `Empleado` WRITE;
/*!40000 ALTER TABLE `Empleado` DISABLE KEYS */;
INSERT INTO `Empleado` VALUES
(1,'Juan Pérez','12345678','L001'),
(2,'Ana Gómez','87654321','L002'),
(3,'Carlos Ruiz','11223344','L001');
/*!40000 ALTER TABLE `Empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Producto`
--

DROP TABLE IF EXISTS `Producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Producto` (
  `IDproducto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `IDproveedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`IDproducto`),
  KEY `IDproveedor` (`IDproveedor`),
  CONSTRAINT `Producto_ibfk_1` FOREIGN KEY (`IDproveedor`) REFERENCES `Proveedor` (`IDproveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Producto`
--

LOCK TABLES `Producto` WRITE;
/*!40000 ALTER TABLE `Producto` DISABLE KEYS */;
INSERT INTO `Producto` VALUES
(1,'Diflucan',15.1,2),
(2,'Medrol',68.5,2),
(3,'Nistazinc NF',19.6,1),
(4,'Gents',6,1),
(5,'linovera',138.88,3),
(6,'Askina Barrier Film',65,3),
(7,'Prontosan Gel',109.6,3),
(8,'Sal de Andrews 12u',8.99,1),
(9,'Caramelo Mentholatum 20u',14.4,1),
(10,'Hylo Fresh',81.4,1),
(11,'Ácido Mefanámico',7.9,2);
/*!40000 ALTER TABLE `Producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proveedor`
--

DROP TABLE IF EXISTS `Proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proveedor` (
  `IDproveedor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) DEFAULT NULL,
  `ruc` char(11) DEFAULT NULL,
  `direccion` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`IDproveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proveedor`
--

LOCK TABLES `Proveedor` WRITE;
/*!40000 ALTER TABLE `Proveedor` DISABLE KEYS */;
INSERT INTO `Proveedor` VALUES
(1,'Medifarma','20100018625','Jr. Ecuador 787'),
(2,'Pfizer','20100127670','Calle Las Orquídeas 585'),
(3,'B. Braun Medical','20377339461','Av. Separadora Industrial 887');
/*!40000 ALTER TABLE `Proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Venta`
--

DROP TABLE IF EXISTS `Venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Venta` (
  `IDventa` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `costototal` double DEFAULT NULL,
  `IDempleado` int(11) DEFAULT NULL,
  PRIMARY KEY (`IDventa`),
  KEY `IDempleado` (`IDempleado`),
  CONSTRAINT `Venta_ibfk_1` FOREIGN KEY (`IDempleado`) REFERENCES `Empleado` (`IDempleado`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Venta`
--

LOCK TABLES `Venta` WRITE;
/*!40000 ALTER TABLE `Venta` DISABLE KEYS */;
INSERT INTO `Venta` VALUES
(1,'2024-11-02 14:35:27',30.2,1),
(2,'2024-11-05 15:50:15',137,2),
(3,'2024-11-10 16:10:45',78.4,3),
(4,'2024-11-15 13:25:50',18,1),
(5,'2024-11-01 18:45:12',45.3,1),
(6,'2024-11-02 15:05:33',137,2),
(7,'2024-11-03 17:15:21',78.4,3),
(8,'2024-11-04 14:50:10',12,1),
(9,'2024-11-05 15:25:30',205.5,2),
(10,'2024-11-06 16:40:00',60.4,3),
(11,'2024-11-07 17:55:45',24,1),
(12,'2024-11-08 14:30:10',102.8,2),
(13,'2024-11-09 18:10:00',18,3),
(14,'2024-11-10 15:35:20',91.5,1),
(15,'2024-11-11 17:45:30',54.3,2),
(16,'2024-11-12 14:55:50',60.4,3),
(17,'2024-11-12 16:20:33',137,1),
(18,'2024-11-13 14:35:50',45.3,2),
(19,'2024-11-13 17:50:15',18,3),
(20,'2024-11-13 18:15:40',72.3,1),
(21,'2024-11-01 14:45:00',160.5,1),
(22,'2024-11-02 16:50:25',230,2),
(23,'2024-11-03 14:15:10',89.9,1),
(24,'2024-11-04 17:30:50',138,3),
(25,'2024-11-05 16:10:15',210.4,2),
(26,'2024-11-06 15:20:50',115,1),
(27,'2024-11-07 14:40:33',98.3,3),
(28,'2024-11-08 18:50:10',187.5,2),
(29,'2024-11-09 16:30:25',134.2,1),
(30,'2024-11-10 15:25:00',142.7,2),
(31,'2024-11-11 17:35:15',210.9,3),
(32,'2024-11-12 18:10:40',167.8,1),
(33,'2024-11-13 14:45:50',99.4,3),
(34,'2024-11-14 17:55:33',185.6,2),
(35,'2024-11-15 16:20:00',153.2,1),
(36,'2024-11-16 15:40:12',121,3),
(37,'2024-11-17 18:15:27',143.7,2),
(38,'2024-11-18 14:50:50',158.9,1),
(39,'2024-11-19 17:30:33',97.6,2),
(40,'2024-11-20 18:40:45',192.3,3),
(41,'2024-11-01 15:10:00',150.8,1),
(42,'2024-11-02 14:55:50',210.6,2),
(43,'2024-11-03 18:20:10',190.3,3),
(44,'2024-11-04 16:45:33',130,1),
(45,'2024-11-05 17:15:20',220.5,2),
(46,'2024-11-06 16:30:10',110.9,3),
(47,'2024-11-07 18:00:15',180.2,1),
(48,'2024-11-08 15:40:25',215.3,2),
(49,'2024-11-09 16:55:30',120.7,3),
(50,'2024-11-10 18:35:10',140.1,1),
(51,'2024-11-11 17:50:20',125.5,2),
(52,'2024-11-12 16:20:45',210,3),
(53,'2024-11-13 14:40:15',135.8,1),
(54,'2024-11-14 17:55:50',205.6,2),
(55,'2024-11-01 15:25:33',160.4,3),
(56,'2024-11-02 16:30:20',145,1),
(57,'2024-11-03 15:55:10',150.2,2),
(58,'2024-11-04 17:20:00',175.3,3),
(59,'2024-11-05 18:00:33',180.7,1),
(60,'2024-11-06 15:40:15',130.5,2),
(61,'2024-11-07 16:10:50',155.8,3),
(62,'2024-11-08 17:20:30',120.6,1),
(63,'2024-11-09 14:45:15',145.9,2),
(64,'2024-11-10 16:55:50',135.7,3),
(65,'2024-11-11 18:20:10',200.2,1),
(66,'2024-11-12 15:30:25',195.4,2),
(67,'2024-11-13 16:40:33',185.3,3),
(68,'2024-11-14 18:15:20',125,1),
(69,'2024-11-01 14:50:33',140.9,2),
(70,'2024-11-02 15:40:50',160.3,3);
/*!40000 ALTER TABLE `Venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Venta_Producto`
--

DROP TABLE IF EXISTS `Venta_Producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Venta_Producto` (
  `IDventa` int(11) NOT NULL,
  `IDproducto` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` double DEFAULT NULL,
  `IDventa_producto` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`IDventa_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Venta_Producto`
--

LOCK TABLES `Venta_Producto` WRITE;
/*!40000 ALTER TABLE `Venta_Producto` DISABLE KEYS */;
INSERT INTO `Venta_Producto` VALUES
(1,1,3,15.1,1),
(2,2,2,68.5,2),
(4,4,2,6,4),
(5,2,3,68.5,5),
(6,3,2,19.6,6),
(6,4,3,6,7),
(7,4,4,6,8),
(8,2,1,68.5,9),
(8,3,2,19.6,10),
(9,4,3,6,11),
(10,1,3,15.1,12),
(10,4,4,6,13),
(11,3,2,19.6,14),
(11,4,2,6,15),
(12,3,2,19.6,16),
(12,4,3,6,17),
(13,2,2,68.5,18),
(14,1,3,15.1,19),
(15,4,3,6,20),
(16,3,2,19.6,21),
(16,4,3,6,22),
(1,2,1,68.5,24),
(1,3,2,20.3,25),
(2,4,10,9.6,26),
(2,5,1,138.8,27),
(3,6,4,8.5,28),
(3,7,1,25.4,29),
(4,8,2,15,30),
(4,9,2,18,31),
(5,10,5,7.9,32),
(5,1,4,15.1,33),
(6,2,1,68.5,34),
(6,3,3,20.3,35),
(7,4,6,9.6,36),
(7,5,1,138.8,37),
(8,6,8,8.5,38),
(8,7,1,25.4,39),
(9,8,5,15,40),
(9,9,2,18,41),
(10,10,3,7.9,42),
(10,1,1,15.1,43),
(11,2,2,68.5,44),
(11,3,4,20.3,45),
(12,4,5,9.6,46),
(12,5,1,138.8,47),
(13,6,3,8.5,48),
(13,7,2,25.4,49),
(14,8,6,15,50),
(14,9,1,18,51),
(15,10,7,7.9,52),
(15,1,2,15.1,53),
(16,2,1,68.5,54),
(16,3,5,20.3,55),
(17,4,4,9.6,56),
(17,5,1,138.8,57),
(18,6,6,8.5,58),
(18,7,1,25.4,59),
(19,8,3,15,60),
(19,9,4,18,61),
(20,10,2,7.9,62),
(20,1,5,15.1,63),
(21,1,4,15.1,64),
(21,2,2,68.5,65),
(22,3,3,20.3,66),
(22,4,10,9.6,67),
(23,5,1,138.8,68),
(23,6,5,8.5,69),
(24,7,2,25.4,70),
(24,8,4,15,71),
(25,9,3,18,72),
(25,10,6,7.9,73),
(26,1,2,15.1,74),
(26,2,1,68.5,75),
(27,3,5,20.3,76),
(27,4,8,9.6,77),
(28,5,1,138.8,78),
(28,6,6,8.5,79),
(29,7,3,25.4,80),
(29,8,2,15,81),
(30,9,7,18,82),
(30,10,4,7.9,83),
(31,1,3,15.1,84),
(31,2,1,68.5,85),
(32,3,4,20.3,86),
(32,4,5,9.6,87),
(33,5,1,138.8,88),
(33,6,8,8.5,89),
(34,7,2,25.4,90),
(34,8,5,15,91),
(35,9,1,18,92),
(35,10,3,7.9,93),
(36,1,6,15.1,94),
(36,2,2,68.5,95),
(37,3,3,20.3,96),
(37,4,4,9.6,97),
(38,5,1,138.8,98),
(38,6,7,8.5,99),
(39,7,1,25.4,100),
(39,8,3,15,101),
(40,9,2,18,102),
(40,10,5,7.9,103),
(41,1,4,15.1,104),
(41,2,1,68.5,105),
(42,3,6,20.3,106),
(42,4,2,9.6,107),
(43,5,1,138.8,108),
(43,6,5,8.5,109),
(44,7,2,25.4,110),
(44,8,4,15,111),
(45,9,3,18,112),
(45,10,6,7.9,113),
(46,1,1,15.1,114),
(46,2,5,68.5,115),
(47,3,4,20.3,116),
(47,4,3,9.6,117);
/*!40000 ALTER TABLE `Venta_Producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-03-09 14:08:12
