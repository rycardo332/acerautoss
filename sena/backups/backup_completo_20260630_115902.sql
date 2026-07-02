-- Respaldo de acerautos_proyecto
-- Fecha: 2026-06-30 11:59:03
-- Tipo: Completo (Estructura + Datos)

-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: acerautos_proyecto
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',2,'add_permission'),(2,'Can change permission',2,'change_permission'),(3,'Can delete permission',2,'delete_permission'),(4,'Can view permission',2,'view_permission'),(5,'Can add group',1,'add_group'),(6,'Can change group',1,'change_group'),(7,'Can delete group',1,'delete_group'),(8,'Can view group',1,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add session',4,'add_session'),(14,'Can change session',4,'change_session'),(15,'Can delete session',4,'delete_session'),(16,'Can view session',4,'view_session'),(17,'Can add caja',5,'add_caja'),(18,'Can change caja',5,'change_caja'),(19,'Can delete caja',5,'delete_caja'),(20,'Can view caja',5,'view_caja'),(21,'Can add cliente',6,'add_cliente'),(22,'Can change cliente',6,'change_cliente'),(23,'Can delete cliente',6,'delete_cliente'),(24,'Can view cliente',6,'view_cliente'),(25,'Can add compra',8,'add_compra'),(26,'Can change compra',8,'change_compra'),(27,'Can delete compra',8,'delete_compra'),(28,'Can view compra',8,'view_compra'),(29,'Can add marca',11,'add_marca'),(30,'Can change marca',11,'change_marca'),(31,'Can delete marca',11,'delete_marca'),(32,'Can view marca',11,'view_marca'),(33,'Can add proveedor',16,'add_proveedor'),(34,'Can change proveedor',16,'change_proveedor'),(35,'Can delete proveedor',16,'delete_proveedor'),(36,'Can view proveedor',16,'view_proveedor'),(37,'Can add Tipo de Servicio',18,'add_tiposervicio'),(38,'Can change Tipo de Servicio',18,'change_tiposervicio'),(39,'Can delete Tipo de Servicio',18,'delete_tiposervicio'),(40,'Can view Tipo de Servicio',18,'view_tiposervicio'),(41,'Can add Usuario del Sistema',19,'add_usuariosistema'),(42,'Can change Usuario del Sistema',19,'change_usuariosistema'),(43,'Can delete Usuario del Sistema',19,'delete_usuariosistema'),(44,'Can view Usuario del Sistema',19,'view_usuariosistema'),(45,'Can add orden servicio',13,'add_ordenservicio'),(46,'Can change orden servicio',13,'change_ordenservicio'),(47,'Can delete orden servicio',13,'delete_ordenservicio'),(48,'Can view orden servicio',13,'view_ordenservicio'),(49,'Can add producto',15,'add_producto'),(50,'Can change producto',15,'change_producto'),(51,'Can delete producto',15,'delete_producto'),(52,'Can view producto',15,'view_producto'),(53,'Can add factura',10,'add_factura'),(54,'Can change factura',10,'change_factura'),(55,'Can delete factura',10,'delete_factura'),(56,'Can view factura',10,'view_factura'),(57,'Can add detalle orden producto',9,'add_detalleordenproducto'),(58,'Can change detalle orden producto',9,'change_detalleordenproducto'),(59,'Can delete detalle orden producto',9,'delete_detalleordenproducto'),(60,'Can view detalle orden producto',9,'view_detalleordenproducto'),(61,'Can add Detalle de Servicio en Orden',14,'add_ordenserviciodetalle'),(62,'Can change Detalle de Servicio en Orden',14,'change_ordenserviciodetalle'),(63,'Can delete Detalle de Servicio en Orden',14,'delete_ordenserviciodetalle'),(64,'Can view Detalle de Servicio en Orden',14,'view_ordenserviciodetalle'),(65,'Can add vehiculo',20,'add_vehiculo'),(66,'Can change vehiculo',20,'change_vehiculo'),(67,'Can delete vehiculo',20,'delete_vehiculo'),(68,'Can view vehiculo',20,'view_vehiculo'),(69,'Can add Seguimiento de Mantenimiento',17,'add_seguimientomantenimiento'),(70,'Can change Seguimiento de Mantenimiento',17,'change_seguimientomantenimiento'),(71,'Can delete Seguimiento de Mantenimiento',17,'delete_seguimientomantenimiento'),(72,'Can view Seguimiento de Mantenimiento',17,'view_seguimientomantenimiento'),(73,'Can add notificacion',12,'add_notificacion'),(74,'Can change notificacion',12,'change_notificacion'),(75,'Can delete notificacion',12,'delete_notificacion'),(76,'Can view notificacion',12,'view_notificacion'),(77,'Can add compatibilidad producto',7,'add_compatibilidadproducto'),(78,'Can change compatibilidad producto',7,'change_compatibilidadproducto'),(79,'Can delete compatibilidad producto',7,'delete_compatibilidadproducto'),(80,'Can view compatibilidad producto',7,'view_compatibilidadproducto'),(81,'Can add Perfil de Usuario',21,'add_perfilusuario'),(82,'Can change Perfil de Usuario',21,'change_perfilusuario'),(83,'Can delete Perfil de Usuario',21,'delete_perfilusuario'),(84,'Can view Perfil de Usuario',21,'view_perfilusuario'),(85,'Can add log entry',22,'add_logentry'),(86,'Can change log entry',22,'change_logentry'),(87,'Can delete log entry',22,'delete_logentry'),(88,'Can view log entry',22,'view_logentry'),(89,'Can add Producto del Proveedor',23,'add_proveedorproducto'),(90,'Can change Producto del Proveedor',23,'change_proveedorproducto'),(91,'Can delete Producto del Proveedor',23,'delete_proveedorproducto'),(92,'Can view Producto del Proveedor',23,'view_proveedorproducto'),(93,'Can add compra detalle',24,'add_compradetalle'),(94,'Can change compra detalle',24,'change_compradetalle'),(95,'Can delete compra detalle',24,'delete_compradetalle'),(96,'Can view compra detalle',24,'view_compradetalle');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caja` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) NOT NULL,
  `monto` decimal(12,2) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `metodo_pago` varchar(20) NOT NULL,
  `comprobante` varchar(100) DEFAULT NULL,
  `observaciones` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
INSERT INTO `caja` VALUES (1,'Compra Factura 123456789',28000.00,'EGRESO','2026-06-19 01:13:46.514403','Proveedores','Efectivo','',NULL),(2,'Factura FAC-0003 â€” Orden de Servicio',77000.00,'INGRESO','2026-06-19 12:29:44.852934','Servicios','Efectivo','',NULL),(3,'Factura FAC-0004 â€” Orden de Servicio',127000.00,'INGRESO','2026-06-20 21:39:31.537238','Servicios','Efectivo','',NULL),(4,'Factura FAC-0005 â€” Orden de Servicio',50000.00,'INGRESO','2026-06-20 22:02:56.128528','Servicios','Efectivo','',NULL),(5,'Factura FAC-0007 â€” Orden de Servicio',77000.00,'INGRESO','2026-06-21 16:50:01.109654','Servicios','Nequi','',NULL),(6,'Factura FAC-0008 â€” Orden de Servicio',77000.00,'INGRESO','2026-06-21 16:57:50.879861','Servicios','Transferencia','',NULL),(7,'Compra Factura 123456788',20000.00,'EGRESO','2026-06-21 23:57:33.917991','Proveedores','Efectivo','',NULL),(8,'Compra Factura 900000',500000.00,'EGRESO','2026-06-21 23:57:56.913845','Proveedores','Efectivo','',NULL),(9,'Compra Factura 963852741',140000.00,'EGRESO','2026-06-22 00:04:29.576197','Proveedores','Efectivo','',NULL),(10,'Compra Factura 30059285250',100000.00,'EGRESO','2026-06-22 00:35:52.835159','Proveedores','Efectivo','',NULL),(11,'Compra Factura 209554566df',4000.00,'EGRESO','2026-06-22 02:55:53.117897','Proveedores','Efectivo','',NULL),(12,'Factura FAC-0009 â€” Orden de Servicio',137000.00,'INGRESO','2026-06-22 14:53:16.244087','Servicios','Nequi','',NULL),(13,'Compra Factura 464646',4560000.00,'EGRESO','2026-06-23 15:43:05.426758','Proveedores','Nequi','',NULL),(14,'Factura FAC-0010 â€” Orden de Servicio',77000.00,'INGRESO','2026-06-23 22:54:16.617355','Servicios','Efectivo','',NULL),(15,'Factura FAC-0011 â€” Orden de Servicio',45200.00,'INGRESO','2026-06-23 22:55:37.182459','Servicios','TarjetaDebito','',NULL),(16,'Factura FAC-0012 â€” Orden de Servicio',40000.00,'INGRESO','2026-06-26 23:39:20.187552','Servicios','Efectivo','',NULL),(17,'Factura FAC-0013 â€” Orden de Servicio',40000.00,'INGRESO','2026-06-26 23:42:31.188239','Servicios','Efectivo','',NULL),(18,'Factura FAC-0014 â€” Orden de Servicio',40000.00,'INGRESO','2026-06-29 14:40:24.282398','Servicios','Efectivo','',NULL),(19,'Compra Factura fac-009',340000.00,'EGRESO','2026-06-30 16:54:40.109879','Proveedores','Efectivo','',NULL),(20,'Factura FAC-0015 â€” Orden de Servicio',77000.00,'INGRESO','2026-06-30 16:58:01.716676','Servicios','Nequi','',NULL);
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_documento` (`numero_documento`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (2,'julian','CC','1019234567','+573107928074','danielmelomolinamolina@gmail.com'),(3,'pepe','CC','108372636','+573215486789','melomolinaricardo@gmail.com'),(4,'Carlos Alberto Mendoza','CC','1023948576','+573129685236','p46030410@gmail.com'),(5,'Diana Valentina Ruiz','CC','30058214','+573209876543','danyel8902@gmail.com'),(6,'Roberto GÃ³mez BolaÃ±os','CC','1020304050','+573101234567','noseeeeeeeuyu@gmail.com'),(7,'Luisa Fernanda Herrera','CC','1098765432','+573207654321','pedrazayuliana198@gmail.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compatibilidad_producto`
--

DROP TABLE IF EXISTS `compatibilidad_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compatibilidad_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `marca_vehiculo_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  `tipo_servicio_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `compatibilidad_producto_producto_id_marca_vehicu_0b706a94_uniq` (`producto_id`,`marca_vehiculo_id`,`tipo_servicio_id`),
  KEY `compatibilidad_producto_marca_vehiculo_id_50d58ec7_fk_marca_id` (`marca_vehiculo_id`),
  KEY `compatibilidad_produ_tipo_servicio_id_905e4d0f_fk_tipo_serv` (`tipo_servicio_id`),
  CONSTRAINT `compatibilidad_produ_tipo_servicio_id_905e4d0f_fk_tipo_serv` FOREIGN KEY (`tipo_servicio_id`) REFERENCES `tipo_servicio` (`id`),
  CONSTRAINT `compatibilidad_producto_marca_vehiculo_id_50d58ec7_fk_marca_id` FOREIGN KEY (`marca_vehiculo_id`) REFERENCES `marca` (`id`),
  CONSTRAINT `compatibilidad_producto_producto_id_9bfe011d_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compatibilidad_producto`
--

LOCK TABLES `compatibilidad_producto` WRITE;
/*!40000 ALTER TABLE `compatibilidad_producto` DISABLE KEYS */;
INSERT INTO `compatibilidad_producto` VALUES (7,2,1,1),(8,6,1,5),(6,7,1,1),(2,2,2,1),(3,6,6,1),(4,2,7,6),(5,6,8,2);
/*!40000 ALTER TABLE `compatibilidad_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `num_factura_proveedor` varchar(50) NOT NULL,
  `metodo_pago` varchar(20) DEFAULT NULL,
  `total_pagado` decimal(12,2) NOT NULL,
  `estado_pago` varchar(10) NOT NULL,
  `fecha_pago` datetime(6) DEFAULT NULL,
  `archivo_factura` varchar(100) DEFAULT NULL,
  `proveedor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `num_factura_proveedor` (`num_factura_proveedor`),
  KEY `compra_proveedor_id_11336635_fk_proveedor_id` (`proveedor_id`),
  CONSTRAINT `compra_proveedor_id_11336635_fk_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (2,'2026-06-19 01:17:20.000000','123456788','Efectivo',20000.00,'Pagada','2026-06-21 23:57:33.902476','',1),(3,'2026-06-21 16:09:39.000000','900000','Efectivo',500000.00,'Pagada','2026-06-21 23:57:56.898817','',3),(4,'2026-06-22 00:04:20.124563','963852741','Efectivo',140000.00,'Pagada','2026-06-22 00:04:29.558723','',3),(5,'2026-06-22 00:14:11.839064','84515646546546',NULL,2000.00,'Pendiente',NULL,'',1),(7,'2026-06-22 02:14:02.617544','wdewiemfiojewiufiueh',NULL,120000.00,'Pendiente',NULL,'',3),(9,'2026-06-22 02:35:38.064099','////-.-.-.--2662',NULL,2000.00,'Pendiente',NULL,'',1),(10,'2026-06-22 02:39:41.285001','fac-9210//////',NULL,1000.00,'Pendiente',NULL,'',1),(13,'2026-06-23 15:42:50.606169','464646','Nequi',4560000.00,'Pagada','2026-06-23 15:43:05.394658','',5),(14,'2026-06-30 16:54:24.671899','fac-009','Efectivo',340000.00,'Pagada','2026-06-30 16:54:40.086694','',5);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra_detalle`
--

DROP TABLE IF EXISTS `compra_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra_detalle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(12,2) NOT NULL,
  `compra_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `compra_detalle_compra_id_producto_id_6d15ecb6_uniq` (`compra_id`,`producto_id`),
  KEY `compra_detalle_producto_id_88b5e7b6_fk_producto_id` (`producto_id`),
  CONSTRAINT `compra_detalle_compra_id_d3411346_fk_compra_id` FOREIGN KEY (`compra_id`) REFERENCES `compra` (`id`),
  CONSTRAINT `compra_detalle_producto_id_88b5e7b6_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra_detalle`
--

LOCK TABLES `compra_detalle` WRITE;
/*!40000 ALTER TABLE `compra_detalle` DISABLE KEYS */;
INSERT INTO `compra_detalle` VALUES (1,2,25000.00,4,1),(2,3,30000.00,4,2),(3,2,1000.00,5,1),(7,2,1000.00,9,1),(8,1,1000.00,10,1),(11,12,380000.00,13,6),(12,1,340000.00,14,6);
/*!40000 ALTER TABLE `compra_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_orden_producto`
--

DROP TABLE IF EXISTS `detalle_orden_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_orden_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `orden_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `detalle_orden_producto_orden_id_c0323597_fk_orden_servicio_id` (`orden_id`),
  KEY `detalle_orden_producto_producto_id_4b1655ab_fk_producto_id` (`producto_id`),
  CONSTRAINT `detalle_orden_producto_orden_id_c0323597_fk_orden_servicio_id` FOREIGN KEY (`orden_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `detalle_orden_producto_producto_id_4b1655ab_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `detalle_orden_producto_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_orden_producto`
--

LOCK TABLES `detalle_orden_producto` WRITE;
/*!40000 ALTER TABLE `detalle_orden_producto` DISABLE KEYS */;
INSERT INTO `detalle_orden_producto` VALUES (10,1,32000.00,13,2),(11,1,32000.00,14,2),(12,1,200.00,17,6),(13,1,32000.00,18,2),(14,1,32000.00,19,2);
/*!40000 ALTER TABLE `detalle_orden_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usuario_sistema_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_sistema_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_sistema` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (22,'admin','logentry'),(5,'app','caja'),(6,'app','cliente'),(7,'app','compatibilidadproducto'),(8,'app','compra'),(24,'app','compradetalle'),(9,'app','detalleordenproducto'),(10,'app','factura'),(11,'app','marca'),(12,'app','notificacion'),(13,'app','ordenservicio'),(14,'app','ordenserviciodetalle'),(15,'app','producto'),(16,'app','proveedor'),(23,'app','proveedorproducto'),(17,'app','seguimientomantenimiento'),(18,'app','tiposervicio'),(19,'app','usuariosistema'),(20,'app','vehiculo'),(1,'auth','group'),(2,'auth','permission'),(3,'contenttypes','contenttype'),(4,'sessions','session'),(21,'usuario','perfilusuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-18 23:57:55.417889'),(2,'contenttypes','0002_remove_content_type_name','2026-06-18 23:57:55.575646'),(3,'auth','0001_initial','2026-06-18 23:57:56.209103'),(4,'auth','0002_alter_permission_name_max_length','2026-06-18 23:57:56.429335'),(5,'auth','0003_alter_user_email_max_length','2026-06-18 23:57:56.447240'),(6,'auth','0004_alter_user_username_opts','2026-06-18 23:57:56.463949'),(7,'auth','0005_alter_user_last_login_null','2026-06-18 23:57:56.477470'),(8,'auth','0006_require_contenttypes_0002','2026-06-18 23:57:56.488868'),(9,'auth','0007_alter_validators_add_error_messages','2026-06-18 23:57:56.499791'),(10,'auth','0008_alter_user_username_max_length','2026-06-18 23:57:56.514599'),(11,'auth','0009_alter_user_last_name_max_length','2026-06-18 23:57:56.529854'),(12,'auth','0010_alter_group_name_max_length','2026-06-18 23:57:56.569818'),(13,'auth','0011_update_proxy_permissions','2026-06-18 23:57:56.580439'),(14,'auth','0012_alter_user_first_name_max_length','2026-06-18 23:57:56.590712'),(15,'app','0001_initial','2026-06-18 23:58:02.968980'),(16,'admin','0001_initial','2026-06-18 23:58:03.335766'),(17,'admin','0002_logentry_remove_auto_add','2026-06-18 23:58:03.360496'),(18,'admin','0003_logentry_add_action_flag_choices','2026-06-18 23:58:03.388126'),(19,'sessions','0001_initial','2026-06-18 23:58:03.472354'),(20,'usuario','0001_initial','2026-06-18 23:58:03.692134'),(21,'app','0002_alter_ordenservicio_km_actual','2026-06-20 20:56:06.998265'),(22,'app','0003_remove_producto_proveedor_proveedorproducto','2026-06-21 15:30:04.358340'),(23,'app','0004_factura_comprobante_pago','2026-06-21 16:37:52.763930'),(24,'app','0005_alter_compra_options_remove_compra_cantidad_and_more','2026-06-21 23:03:48.237240'),(25,'app','0006_usuariosistema_debe_cambiar_password','2026-06-26 23:56:52.844625');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('seb943tz0bkbpsbzdh3puy6y1a8bk362','.eJxVjDkOwjAQAP-yLWCtvfFZ0tPRW75CDCGR4oQG8XeERAHtzGie4MO2Dn5rZfE1g4MO9r8shnQr00fka5guM0vztC41sk_Cvrax05zLePy2f4MhtAEcKKk0t1knTlJEI1HzzK2MyaKOkpMwIvXFqJAy9ZYkJVNsH9GQ7KOSCvawjWu9B7-UR211nnwYy7KGBg4ECnVAdSA8c-U64TrNSAtDuEN0iPB6AzkHSDY:1webXr:VdQwLC2hneWWA69kkP-OwPaX9jyEVI1QgfgNEvk_MeM','2026-07-14 16:42:47.461298');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(10) NOT NULL,
  `numero_factura` varchar(20) NOT NULL,
  `fecha_emision` datetime(6) NOT NULL,
  `cantidad` int unsigned NOT NULL,
  `subtotal` decimal(12,2) NOT NULL,
  `iva` decimal(12,2) NOT NULL,
  `total` decimal(12,2) NOT NULL,
  `estado_pago` varchar(10) NOT NULL,
  `metodo_pago` varchar(20) DEFAULT NULL,
  `fecha_pago` datetime(6) DEFAULT NULL,
  `compra_id` bigint DEFAULT NULL,
  `orden_servicio_id` bigint DEFAULT NULL,
  `producto_id` bigint DEFAULT NULL,
  `comprobante_pago` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_factura` (`numero_factura`),
  UNIQUE KEY `compra_id` (`compra_id`),
  KEY `factura_orden_servicio_id_35d209fc_fk_orden_servicio_id` (`orden_servicio_id`),
  KEY `factura_producto_id_8e907400_fk_producto_id` (`producto_id`),
  CONSTRAINT `factura_compra_id_d41cea05_fk_compra_id` FOREIGN KEY (`compra_id`) REFERENCES `compra` (`id`),
  CONSTRAINT `factura_orden_servicio_id_35d209fc_fk_orden_servicio_id` FOREIGN KEY (`orden_servicio_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `factura_producto_id_8e907400_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `factura_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,'COMPRA','123456789','2026-06-19 01:13:38.589748',1,28000.00,0.00,28000.00,'Pagada','Efectivo','2026-06-19 01:13:46.533363',NULL,NULL,NULL,NULL),(2,'COMPRA','123456788','2026-06-19 01:17:55.325435',1,20000.00,0.00,20000.00,'Pendiente',NULL,NULL,2,NULL,NULL,NULL),(3,'SERVICIO','FAC-0003','2026-06-19 12:29:25.126343',1,77000.00,0.00,77000.00,'Pagada','Efectivo','2026-06-19 12:29:44.791358',NULL,NULL,NULL,NULL),(4,'SERVICIO','FAC-0004','2026-06-20 21:39:15.824851',1,127000.00,0.00,127000.00,'Pagada','Efectivo','2026-06-20 21:39:31.512884',NULL,NULL,NULL,NULL),(5,'SERVICIO','FAC-0005','2026-06-20 22:02:48.596718',1,50000.00,0.00,50000.00,'Pagada','Efectivo','2026-06-20 22:02:56.108256',NULL,NULL,NULL,NULL),(6,'COMPRA','900000','2026-06-21 16:10:11.561318',1,500000.00,0.00,500000.00,'Pendiente',NULL,NULL,3,NULL,NULL,NULL),(7,'SERVICIO','FAC-0007','2026-06-21 16:32:55.312632',1,77000.00,0.00,77000.00,'Pagada','Nequi','2026-06-21 16:50:01.032747',NULL,NULL,NULL,'facturas_comprobantes/facturas-y-recibos-para-talleres-screenshot_1_1.png'),(8,'SERVICIO','FAC-0008','2026-06-21 16:57:28.303265',1,77000.00,0.00,77000.00,'Pagada','Transferencia','2026-06-21 16:57:50.835288',NULL,NULL,NULL,'facturas_comprobantes/facturas-y-recibos-para-talleres-screenshot_1_1_Ni40FwH.png'),(9,'SERVICIO','FAC-0009','2026-06-21 18:04:00.114844',1,137000.00,0.00,137000.00,'Pagada','Nequi','2026-06-22 14:53:16.223025',NULL,NULL,NULL,'facturas_comprobantes/descarga_1.png'),(10,'SERVICIO','FAC-0010','2026-06-23 22:54:10.455868',1,77000.00,0.00,77000.00,'Pagada','Efectivo','2026-06-23 22:54:16.601966',NULL,13,NULL,''),(11,'SERVICIO','FAC-0011','2026-06-23 22:55:29.090682',1,45200.00,0.00,45200.00,'Pagada','TarjetaDebito','2026-06-23 22:55:37.173378',NULL,NULL,NULL,''),(12,'SERVICIO','FAC-0012','2026-06-26 23:39:11.938298',1,40000.00,0.00,40000.00,'Pagada','Efectivo','2026-06-26 23:39:20.164459',NULL,NULL,NULL,''),(13,'SERVICIO','FAC-0013','2026-06-26 23:42:23.736186',1,40000.00,0.00,40000.00,'Pagada','Efectivo','2026-06-26 23:42:31.139857',NULL,NULL,NULL,''),(14,'SERVICIO','FAC-0014','2026-06-29 14:40:14.315821',1,40000.00,0.00,40000.00,'Pagada','Efectivo','2026-06-29 14:40:24.193637',NULL,16,NULL,''),(15,'SERVICIO','FAC-0015','2026-06-30 16:57:36.846288',1,77000.00,0.00,77000.00,'Pagada','Nequi','2026-06-30 16:58:01.661945',NULL,19,NULL,'facturas_comprobantes/toyotaa.png');
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca`
--

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `categoria` varchar(10) NOT NULL,
  `pais_origen` varchar(50) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `descripcion` longtext,
  `estado` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES (2,'renault clio','AUTO','Francia','marcas_logos/Renault_logo.jpg','VehÃ­culo hatchback Ã¡gil y eficiente para ciudad.',1,'2026-06-19 00:28:09.924298'),(3,'Mobil','REPUESTO','Estados Unidos','marcas_logos/images_2.jpg','Aceites para vehÃ­culos y aditivos de alto rendimiento.',1,'2026-06-19 00:42:52.425248'),(4,'castrol','REPUESTO','Reino Unido','marcas_logos/castrol-logo-0.png','Aceites y lubricantes para motor de alta calidad.',1,'2026-06-19 01:02:31.044193'),(5,'michelin','REPUESTO','Francia','marcas_logos/descarga_1.png','Llantas de alta durabilidad y excelente agarre.',1,'2026-06-22 02:09:32.504334'),(6,'Chevrolet Tracker','AUTO','Otro','marcas_logos/images_5.jpg','Camioneta SUV compacta y versÃ¡til.',1,'2026-06-22 02:59:08.039861'),(7,'Toyota Hilux','AUTO','Japon','marcas_logos/toyotaa.png','Camioneta pick-up 4x4 fuerte y todoterreno.',1,'2026-06-23 01:06:20.498620'),(8,'Havoline','REPUESTO','Estados Unidos','marcas_logos/havoline-racing-logo-png_seeklogo-289391.png','Lubricantes protectores para el cuidado del motor.',1,'2026-06-23 01:12:08.732870'),(9,'Brembo','REPUESTO','Italia','marcas_logos/brenbo.png','Sistemas de frenado premium y discos de alto desempeÃ±o.',1,'2026-06-23 01:14:18.786883'),(10,'Bendix','REPUESTO','Estados Unidos','marcas_logos/bendix.png','Pastillas y repuestos de frenos de alto rendimiento.',1,'2026-06-23 01:15:09.886345');
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacion`
--

DROP TABLE IF EXISTS `notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notificacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL,
  `origen` varchar(10) NOT NULL,
  `titulo` varchar(150) NOT NULL,
  `mensaje` longtext NOT NULL,
  `leido` tinyint(1) NOT NULL,
  `fecha` date NOT NULL,
  `vehiculo_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `notificacion_vehiculo_id_eeb53247_fk_vehiculo_id` (`vehiculo_id`),
  CONSTRAINT `notificacion_vehiculo_id_eeb53247_fk_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=191 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacion`
--

LOCK TABLES `notificacion` WRITE;
/*!40000 ALTER TABLE `notificacion` DISABLE KEYS */;
INSERT INTO `notificacion` VALUES (155,'Mantenimiento','SISTEMA','Servicio completado â€” QWE123','El servicio de la orden #15 ha sido completado y el pago registrado. El vehÃ­culo QWE123 (renault clio 2020) ya puede ser retirado.',1,'2026-06-26',2),(156,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 2 dÃ­as.',1,'2026-06-26',7),(157,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(158,'Mantenimiento','SISTEMA','Mantenimiento VENCIDO â€” XYZ123','El vehÃ­culo XYZ123 superÃ³ la fecha lÃ­mite (2026-06-24).',1,'2026-06-26',7),(159,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(160,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(161,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(162,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(163,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(164,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(165,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(166,'Urgente','SISTEMA','Mantenimiento vencido â€” XYZ123','El mantenimiento venciÃ³ hace 3 dÃ­as.',1,'2026-06-26',7),(168,'Mantenimiento','SISTEMA','Servicio completado â€” POI123','El servicio de la orden #16 ha sido completado y el pago registrado. El vehÃ­culo POI123 (renault clio 2026) ya puede ser retirado.',1,'2026-06-29',4),(171,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” KLI562','Faltan 2 dÃ­as para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-29',11),(172,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” XYZ123','Faltan 2 dÃ­as para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-29',7),(173,'Mantenimiento','SISTEMA','Mantenimiento prÃ³ximo â€” KLI562','El vehÃ­culo KLI562 tiene su mantenimiento prÃ³ximo. Faltan 2 dÃ­as (fecha: 2026-07-01).',1,'2026-06-29',11),(174,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” XYZ123','El vehÃ­culo XYZ123 tiene su prÃ³ximo servicio el 2026-07-01 (2 dÃ­as restantes).',1,'2026-06-29',7),(175,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” KLI562','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-29',11),(176,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” XYZ123','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-29',7),(177,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” KLI562','El vehÃ­culo KLI562 tiene su prÃ³ximo servicio el 2026-07-01 (2 dÃ­as restantes).',1,'2026-06-29',11),(178,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” XYZ123','El vehÃ­culo XYZ123 tiene su prÃ³ximo servicio el 2026-07-01 (2 dÃ­as restantes).',1,'2026-06-29',7),(179,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” KLI562','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-29',11),(180,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” XYZ123','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-29',7),(181,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” KLI562','El vehÃ­culo KLI562 tiene su prÃ³ximo servicio el 2026-07-01 (2 dÃ­as restantes).',1,'2026-06-29',11),(182,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” XYZ123','El vehÃ­culo XYZ123 tiene su prÃ³ximo servicio el 2026-07-01 (2 dÃ­as restantes).',1,'2026-06-29',7),(183,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” KLI562','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-30',11),(184,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” XYZ123','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-30',7),(185,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” KLI562','El vehÃ­culo KLI562 tiene su prÃ³ximo servicio el 2026-07-01 (1 dÃ­as restantes).',1,'2026-06-30',11),(186,'Mantenimiento','SISTEMA','Mantenimiento PRÃ“XIMO â€” XYZ123','El vehÃ­culo XYZ123 tiene su prÃ³ximo servicio el 2026-07-01 (1 dÃ­as restantes).',1,'2026-06-30',7),(188,'Urgente','SISTEMA','Mantenimiento prÃ³ximo â€” QWE123','Faltan 1 dÃ­a para el mantenimiento (fecha: 01/07/2026).',1,'2026-06-30',2),(189,'Informacion','ADMIN','Descuento','Descuento por eÃ± dia de hoy',1,'2026-06-30',NULL),(190,'Mantenimiento','SISTEMA','Servicio completado â€” QWE123','El servicio de la orden #19 ha sido completado y el pago registrado. El vehÃ­culo QWE123 (renault clio 2020) ya puede ser retirado.',0,'2026-06-30',2);
/*!40000 ALTER TABLE `notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_servicio`
--

DROP TABLE IF EXISTS `orden_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_servicio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `km_actual` int DEFAULT NULL,
  `estado` varchar(20) NOT NULL,
  `observaciones` longtext,
  `empleado_id` bigint DEFAULT NULL,
  `vehiculo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orden_servicio_vehiculo_id_1f8a455d_fk_vehiculo_id` (`vehiculo_id`),
  KEY `orden_servicio_empleado_id_e6e8f574_fk_usuario_sistema_id` (`empleado_id`),
  CONSTRAINT `orden_servicio_empleado_id_e6e8f574_fk_usuario_sistema_id` FOREIGN KEY (`empleado_id`) REFERENCES `usuario_sistema` (`id`),
  CONSTRAINT `orden_servicio_vehiculo_id_1f8a455d_fk_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_servicio`
--

LOCK TABLES `orden_servicio` WRITE;
/*!40000 ALTER TABLE `orden_servicio` DISABLE KEYS */;
INSERT INTO `orden_servicio` VALUES (13,'2026-06-23 22:52:46.486562',5000,'Terminado',NULL,NULL,2),(14,'2026-06-23 22:58:39.216872',30,'Pendiente',NULL,NULL,10),(16,'2026-06-29 14:39:46.352059',NULL,'Terminado',NULL,6,4),(17,'2026-06-29 22:38:11.388748',1000,'Pendiente',NULL,6,7),(18,'2026-06-29 22:41:17.209814',100,'Pendiente',NULL,6,11),(19,'2026-06-30 16:49:00.891712',30000,'Terminado',NULL,6,2);
/*!40000 ALTER TABLE `orden_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_servicio_detalle`
--

DROP TABLE IF EXISTS `orden_servicio_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_servicio_detalle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `precio_mano_obra` decimal(12,2) NOT NULL,
  `orden_id` bigint NOT NULL,
  `tipo_servicio_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orden_servicio_detalle_orden_id_tipo_servicio_id_5f1a29fc_uniq` (`orden_id`,`tipo_servicio_id`),
  KEY `orden_servicio_detal_tipo_servicio_id_43136163_fk_tipo_serv` (`tipo_servicio_id`),
  CONSTRAINT `orden_servicio_detal_tipo_servicio_id_43136163_fk_tipo_serv` FOREIGN KEY (`tipo_servicio_id`) REFERENCES `tipo_servicio` (`id`),
  CONSTRAINT `orden_servicio_detalle_orden_id_7cb4619f_fk_orden_servicio_id` FOREIGN KEY (`orden_id`) REFERENCES `orden_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_servicio_detalle`
--

LOCK TABLES `orden_servicio_detalle` WRITE;
/*!40000 ALTER TABLE `orden_servicio_detalle` DISABLE KEYS */;
INSERT INTO `orden_servicio_detalle` VALUES (19,45000.00,13,1),(20,45000.00,14,1),(22,40000.00,16,5),(23,45000.00,17,1),(24,45000.00,18,1),(25,45000.00,19,1);
/*!40000 ALTER TABLE `orden_servicio_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil_usuario`
--

DROP TABLE IF EXISTS `perfil_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfil_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rol` varchar(20) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `perfil_usuario_user_id_a77a2a33_fk_usuario_sistema_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_sistema` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil_usuario`
--

LOCK TABLES `perfil_usuario` WRITE;
/*!40000 ALTER TABLE `perfil_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `perfil_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext,
  `precio` decimal(10,2) NOT NULL,
  `stock` int unsigned NOT NULL,
  `stock_minimo` int unsigned NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `unidad_medida` varchar(5) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  `marca_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `producto_marca_id_2793ee53_fk_marca_id` (`marca_id`),
  CONSTRAINT `producto_marca_id_2793ee53_fk_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `marca` (`id`),
  CONSTRAINT `producto_chk_1` CHECK ((`stock` >= 0)),
  CONSTRAINT `producto_chk_2` CHECK ((`stock_minimo` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Aceite Castrol Edge 5W-40','Aceite sintÃ©tico para motores modernos de alta exigencia.',38000.00,58,10,'001','LT','productos/images_3.jpg',1,4),(2,'Aceite Castrol 5W-20','',32000.00,19,10,'002','UND','productos/61wg3ZXgDpL.jpg',1,4),(6,'aceite mobil 10w -30','',200.00,14,10,'51654564545654','UND','productos/shopping_1_TkW2r0Y.webp',1,3),(7,'Llanta Michelin 205/55 R16','Llanta de alto desempeÃ±o para automÃ³viles y SUV.',320000.00,0,10,'5156155665','UND','productos/images_6.jpg',1,5),(8,'Pastillas de freno Chevrolet Tracker','Pastillas de freno cerÃ¡micas de alta durabilidad.',145000.00,0,10,'65632151515','JGO','productos/kl.jpeg',1,10),(9,'llantas','ewqudwudu',700000.00,0,12,'74374734','PAR','productos/toyotaa.png',1,5);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `nit` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion` varchar(150) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nit` (`nit`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'Distribuidora Automotriz del Llano','9001234561','+573144567890','Carrera 15 # 8-32, Yopal',0),(3,'Distribuidora Automotriz','200009558','+573107928074','calle 608',0),(5,'llantitas','7373773777','+573232444444','calle -8',0);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor_producto`
--

DROP TABLE IF EXISTS `proveedor_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `precio_proveedor` decimal(10,2) NOT NULL,
  `producto_id` bigint NOT NULL,
  `proveedor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `proveedor_producto_proveedor_id_producto_id_e2e965f1_uniq` (`proveedor_id`,`producto_id`),
  KEY `proveedor_producto_producto_id_fcec900d_fk_producto_id` (`producto_id`),
  CONSTRAINT `proveedor_producto_producto_id_fcec900d_fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `proveedor_producto_proveedor_id_f19d751f_fk_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor_producto`
--

LOCK TABLES `proveedor_producto` WRITE;
/*!40000 ALTER TABLE `proveedor_producto` DISABLE KEYS */;
INSERT INTO `proveedor_producto` VALUES (1,25000.00,1,3),(2,30000.00,2,3),(4,1000.00,1,1),(11,6000.00,8,1),(12,20000.00,7,3),(13,340000.00,6,5);
/*!40000 ALTER TABLE `proveedor_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seguimiento_mantenimiento`
--

DROP TABLE IF EXISTS `seguimiento_mantenimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seguimiento_mantenimiento` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `km_al_momento` int NOT NULL,
  `km_proximo_mantenimiento` int DEFAULT NULL,
  `fecha_proximo_mantenimiento` date DEFAULT NULL,
  `estado` varchar(15) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `observaciones` longtext,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `orden_servicio_id` bigint DEFAULT NULL,
  `tipo_servicio_id` bigint DEFAULT NULL,
  `vehiculo_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `seguimiento_mantenim_orden_servicio_id_b19382b4_fk_orden_ser` (`orden_servicio_id`),
  KEY `seguimiento_mantenim_tipo_servicio_id_3a1d9c73_fk_tipo_serv` (`tipo_servicio_id`),
  KEY `seguimiento_mantenimiento_vehiculo_id_4de7b801_fk_vehiculo_id` (`vehiculo_id`),
  CONSTRAINT `seguimiento_mantenim_orden_servicio_id_b19382b4_fk_orden_ser` FOREIGN KEY (`orden_servicio_id`) REFERENCES `orden_servicio` (`id`),
  CONSTRAINT `seguimiento_mantenim_tipo_servicio_id_3a1d9c73_fk_tipo_serv` FOREIGN KEY (`tipo_servicio_id`) REFERENCES `tipo_servicio` (`id`),
  CONSTRAINT `seguimiento_mantenimiento_vehiculo_id_4de7b801_fk_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seguimiento_mantenimiento`
--

LOCK TABLES `seguimiento_mantenimiento` WRITE;
/*!40000 ALTER TABLE `seguimiento_mantenimiento` DISABLE KEYS */;
INSERT INTO `seguimiento_mantenimiento` VALUES (7,2000,15000,'2026-06-24','Completado',0,'Creado automÃ¡ticamente desde Orden #10. Km al momento: 2,000. PrÃ³ximo cambio a los 15,000 km (13,000 km restantes). Uso del vehÃ­culo: Carga / Transporte (intensivo) (~400 km/dÃ­a, cambio cada 15,000 km). Estimado: 32 dÃ­as.','2026-06-23 02:15:12.179856','2026-06-23 02:15:12.179961',NULL,1,9),(8,6000,10000,'2026-06-23','Completado',0,'Creado automÃ¡ticamente desde Orden #11. Km al momento: 6,000. PrÃ³ximo cambio a los 10,000 km (4,000 km restantes). Uso del vehÃ­culo: Uso bajo (ciudad, poco uso) (~30 km/dÃ­a, cambio cada 5,000 km). Estimado: 133 dÃ­as.','2026-06-23 02:22:02.484314','2026-06-23 02:22:02.484341',NULL,1,2),(9,62222,65000,'2026-06-24','Completado',0,'Creado automÃ¡ticamente desde Orden #12. Km al momento: 62,222. PrÃ³ximo cambio a los 65,000 km (2,778 km restantes). Uso del vehÃ­culo: Uso normal (estÃ¡ndar) (~50 km/dÃ­a, cambio cada 5,000 km). Estimado: 55 dÃ­as.','2026-06-23 15:35:49.020134','2026-06-23 15:35:49.020189',NULL,1,7),(10,5000,10000,'2026-12-06','Pendiente',0,'Creado automÃ¡ticamente desde Orden #13. Km al momento: 5,000. PrÃ³ximo cambio a los 10,000 km (5,000 km restantes). Uso del vehÃ­culo: Uso bajo (ciudad, poco uso) (~30 km/dÃ­a, cambio cada 5,000 km). Estimado: 166 dÃ­as.','2026-06-23 22:52:46.564695','2026-06-23 22:52:46.564733',13,1,2),(11,30,5000,'2026-12-05','Pendiente',1,'Creado automÃ¡ticamente desde Orden #14. Km al momento: 30. PrÃ³ximo cambio a los 5,000 km (4,970 km restantes). Uso del vehÃ­culo: Uso bajo (ciudad, poco uso) (~30 km/dÃ­a, cambio cada 5,000 km). Estimado: 165 dÃ­as.','2026-06-23 22:58:39.287846','2026-06-23 22:58:39.287900',14,1,10),(12,1000,5000,'2026-07-01','Pendiente',1,'Creado automÃ¡ticamente desde Orden #17. Km al momento: 1,000. PrÃ³ximo cambio a los 5,000 km (4,000 km restantes). Uso del vehÃ­culo: Uso normal (estÃ¡ndar) (~50 km/dÃ­a, cambio cada 5,000 km). Estimado: 80 dÃ­as.','2026-06-29 22:38:11.515735','2026-06-29 22:38:11.515862',17,1,7),(13,100,5000,'2026-07-01','Pendiente',1,'Creado automÃ¡ticamente desde Orden #18. Km al momento: 100. PrÃ³ximo cambio a los 5,000 km (4,900 km restantes). Uso del vehÃ­culo: Uso bajo (ciudad, poco uso) (~30 km/dÃ­a, cambio cada 5,000 km). Estimado: 163 dÃ­as.','2026-06-29 22:41:17.348786','2026-06-29 22:41:17.348842',18,1,11);
/*!40000 ALTER TABLE `seguimiento_mantenimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_servicio`
--

DROP TABLE IF EXISTS `tipo_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_servicio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext,
  `precio_mano_obra` decimal(12,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `requiere_seguimiento` tinyint(1) NOT NULL,
  `requiere_productos` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_servicio`
--

LOCK TABLES `tipo_servicio` WRITE;
/*!40000 ALTER TABLE `tipo_servicio` DISABLE KEYS */;
INSERT INTO `tipo_servicio` VALUES (1,'Cambio de aceite y filtro','Cambio de aceite y filtro segÃºn especificaciones del fabricante.',45000.00,1,1,1,'2026-06-19 00:35:52.427348','2026-06-30 16:47:49.316297'),(2,'RevisiÃ³n de frenos','nspecciÃ³n completa del sistema de frenado para garantizar seguridad.',50000.00,1,0,1,'2026-06-19 00:37:19.400803','2026-06-29 22:35:53.665038'),(3,'Balanceo de llantas','Balanceo dinÃ¡mico y estÃ¡tico para evitar vibraciones al conducir.',60000.00,1,0,0,'2026-06-22 12:22:02.556018','2026-06-23 01:47:24.043212'),(4,'RevisiÃ³n general','InspecciÃ³n visual y funcional de los componentes principales del vehÃ­culo.',20000.00,1,0,0,'2026-06-22 12:30:14.314696','2026-06-23 01:49:17.049216'),(5,'AlineaciÃ³n','Ajuste de los Ã¡ngulos de las ruedas para asegurar un desgaste uniforme y correcta direcciÃ³n.',40000.00,1,0,0,'2026-06-23 01:50:19.615973','2026-06-23 01:50:19.616001'),(6,'Montaje de llantas','Desmonte, montaje y vÃ¡lvula nueva para llantas.',15000.00,1,0,1,'2026-06-23 01:51:08.293069','2026-06-23 01:51:08.293237');
/*!40000 ALTER TABLE `tipo_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_sistema`
--

DROP TABLE IF EXISTS `usuario_sistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_sistema` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `cedula` varchar(20) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `cargo` varchar(20) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `debe_cambiar_password` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `cedula` (`cedula`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema`
--

LOCK TABLES `usuario_sistema` WRITE;
/*!40000 ALTER TABLE `usuario_sistema` DISABLE KEYS */;
INSERT INTO `usuario_sistema` VALUES (1,'pbkdf2_sha256$1200000$oDiT83YhdXnEv2hA8umLCF$Am68P67+YC6cL1BLyO5mrLHcwxjGa7YZqwvEFSfoUMM=','2026-06-30 13:16:53.916858',1,'Daniel','','','daniel@gmail.com',1,1,'2026-06-18 23:59:25.044283','CC',NULL,NULL,'ADMIN',1,'',0),(4,'pbkdf2_sha256$1200000$aQmZrQpaaVv4nzgN8rGmXW$1iKMLYJogs2tC5woIefyPZN9bGyjynVq7OOHIT1ChTM=','2026-06-30 16:42:47.319681',0,'pepe','pepe','lopez','melomolinaricardo@gmail.com',0,1,'2026-06-19 16:07:32.656218','CC','987456123','3107928075','ADMIN',1,'usuarios/fotos/perfil_J6p0Dbp.jpg',0),(5,'pbkdf2_sha256$1200000$EhfMhlx0B2Q0nIa7Boigkr$mcGki7b2/5pVKfQB9vor82sgJvlh7F3mMVc04V+DEUY=','2026-06-27 00:15:39.580515',0,'pepes','pepe','pepe','pepe@gmail.com',0,1,'2026-06-20 21:45:40.937292','CC','123456789','3205698741','MECANICO',1,'usuarios/fotos/perfil_liMz3w5.jpg',0),(6,'pbkdf2_sha256$1200000$o6Iygab4Mxvi1eZTNBypf6$YzGSAl/bfBbodmTL3KljU434zkKug61wamX6eJ3lcUA=','2026-06-27 00:02:03.964358',0,'carlos','carlos','perez','p46030410@gmail.com',0,0,'2026-06-27 00:01:40.200134','CC','1025962311','3108956212','MECANICO',1,'',0);
/*!40000 ALTER TABLE `usuario_sistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_sistema_groups`
--

DROP TABLE IF EXISTS `usuario_sistema_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_sistema_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuariosistema_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_sistema_groups_usuariosistema_id_group_id_22de142c_uniq` (`usuariosistema_id`,`group_id`),
  KEY `usuario_sistema_groups_group_id_3639004b_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuario_sistema_grou_usuariosistema_id_dcbe40e6_fk_usuario_s` FOREIGN KEY (`usuariosistema_id`) REFERENCES `usuario_sistema` (`id`),
  CONSTRAINT `usuario_sistema_groups_group_id_3639004b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema_groups`
--

LOCK TABLES `usuario_sistema_groups` WRITE;
/*!40000 ALTER TABLE `usuario_sistema_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_sistema_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_sistema_user_permissions`
--

DROP TABLE IF EXISTS `usuario_sistema_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_sistema_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuariosistema_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_sistema_user_per_usuariosistema_id_permis_4d7098b0_uniq` (`usuariosistema_id`,`permission_id`),
  KEY `usuario_sistema_user_permission_id_408f8403_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuario_sistema_user_permission_id_408f8403_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuario_sistema_user_usuariosistema_id_1619ab8b_fk_usuario_s` FOREIGN KEY (`usuariosistema_id`) REFERENCES `usuario_sistema` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_sistema_user_permissions`
--

LOCK TABLES `usuario_sistema_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuario_sistema_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_sistema_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo`
--

DROP TABLE IF EXISTS `vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiculo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `placa` varchar(10) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `tipo_uso` varchar(10) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `cliente_id` bigint NOT NULL,
  `marca_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `placa` (`placa`),
  KEY `vehiculo_cliente_id_967a1a09_fk_cliente_id` (`cliente_id`),
  KEY `vehiculo_marca_id_4c86da34_fk_marca_id` (`marca_id`),
  CONSTRAINT `vehiculo_cliente_id_967a1a09_fk_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`),
  CONSTRAINT `vehiculo_marca_id_4c86da34_fk_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `marca` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo`
--

LOCK TABLES `vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo` DISABLE KEYS */;
INSERT INTO `vehiculo` VALUES (2,'QWE123','2020','BAJO','2026-06-19 00:28:37.046817','2026-06-21 13:43:18.578761',2,2),(4,'POI123','2026','CARGA','2026-06-21 14:44:27.776433','2026-06-21 14:44:27.776487',2,2),(5,'LOP123','2026','NORMAL','2026-06-21 15:12:28.513869','2026-06-21 15:12:28.514048',2,2),(6,'JKL789','2026','NORMAL','2026-06-22 02:59:49.414871','2026-06-22 02:59:49.415014',3,6),(7,'XYZ123','2022','NORMAL','2026-06-23 01:44:04.272026','2026-06-23 01:44:04.272380',7,6),(8,'ABC456','2019','BAJO','2026-06-23 01:44:35.431661','2026-06-23 11:40:22.543624',4,2),(9,'ZZZ789','2026','CARGA','2026-06-23 01:45:08.602579','2026-06-23 11:40:10.408555',4,7),(10,'FEC511','2000','BAJO','2026-06-23 15:29:11.915235','2026-06-23 15:29:11.915280',2,2),(11,'KLI562','2026','BAJO','2026-06-29 22:40:42.371956','2026-06-29 22:40:42.372141',5,2);
/*!40000 ALTER TABLE `vehiculo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-30 11:59:03
