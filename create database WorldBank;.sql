create database WorldBank;
SHOW SESSION VARIABLES LIKE 'lower_case_table_names'
SHOW DATABASES
SHOW SESSION VARIABLES LIKE 'lower_case_table_names'
CREATE TABLE `worldbank`.`gdp growth (annual %)` (`MyUnknownColumn` int, `economy` text, `Country` text, `Time` int, `NY.GDP.MKTP.KD.ZG` double)
PREPARE stmt FROM 'INSERT INTO `worldbank`.`gdp growth (annual %)` (`MyUnknownColumn`,`economy`,`Country`,`Time`,`NY.GDP.MKTP.KD.ZG`) VALUES(?,?,?,?,?)'
CREATE TABLE `worldbank`.`gdp per capita` (`MyUnknownColumn` int, `economy` text, `Country` text, `Time` int, `NY.GDP.PCAP.CN` double)
PREPARE stmt FROM 'INSERT INTO `worldbank`.`gdp per capita` (`MyUnknownColumn`,`economy`,`Country`,`Time`,`NY.GDP.PCAP.CN`) VALUES(?,?,?,?,?)'
CREATE TABLE `worldbank`.`gdp per person employed` (`MyUnknownColumn` int, `economy` text, `Country` text, `Time` int, `SL.GDP.PCAP.EM.KD` double)
PREPARE stmt FROM 'INSERT INTO `worldbank`.`gdp per person employed` (`MyUnknownColumn`,`economy`,`Country`,`Time`,`SL.GDP.PCAP.EM.KD`) VALUES(?,?,?,?,?)'
CREATE TABLE `worldbank`.`gdp` (`MyUnknownColumn` int, `economy` text, `Country` text, `Time` int, `NY.GDP.MKTP.CD` double)
PREPARE stmt FROM 'INSERT INTO `worldbank`.`gdp` (`MyUnknownColumn`,`economy`,`Country`,`Time`,`NY.GDP.MKTP.CD`) VALUES(?,?,?,?,?)'
CREATE TABLE `worldbank`.`inflation, gdp deflator(annual %)` (`MyUnknownColumn` int, `economy` text, `Country` text, `Time` int, `NY.GDP.DEFL.KD.ZG.AD` double)
PREPARE stmt FROM 'INSERT INTO `worldbank`.`inflation, gdp deflator(annual %)` (`MyUnknownColumn`,`economy`,`Country`,`Time`,`NY.GDP.DEFL.KD.ZG.AD`) VALUES(?,?,?,?,?)'
DEALLOCATE PREPARE stmt