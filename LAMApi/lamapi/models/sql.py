AUTHOR_SQL_TABLE_CREATE = """CREATE TABLE `Author` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"""

TYPE_SQL_TABLE_CREATE = """CREATE TABLE `Type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"""

MUSIC_SQL_TABLE_CREATE = """CREATE TABLE `Music` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `author` int NOT NULL,
  `type1` int NOT NULL,
  `type2` int DEFAULT NULL,
  `type3` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`author`) REFERENCES `Author`(`id`),
  FOREIGN KEY (`type1`) REFERENCES `Type`(`id`),
  FOREIGN KEY (`type2`) REFERENCES `Type`(`id`),
  FOREIGN KEY (`type3`) REFERENCES `Type`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"""