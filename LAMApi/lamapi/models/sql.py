AUTHOR_SQL_TABLE_CREATE = """CREATE TABLE `author` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"""

TYPE_SQL_TABLE_CREATE = """CREATE TABLE `type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"""

MUSIC_SQL_TABLE_CREATE = """CREATE TABLE `music` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `author` int NOT NULL,
  `type1` int NOT NULL,
  `type2` int DEFAULT NULL,
  `type3` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`author`) REFERENCES `author`(`id`),
  FOREIGN KEY (`type1`) REFERENCES `type`(`id`),
  FOREIGN KEY (`type2`) REFERENCES `type`(`id`),
  FOREIGN KEY (`type3`) REFERENCES `type`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;"""

MUSIC_SQL_TABLE_COLUMNS = """SELECT cols.COLUMN_NAME, cols.DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS cols
WHERE cols.TABLE_SCHEMA = '%s'
AND cols.TABLE_NAME = 'music';
"""