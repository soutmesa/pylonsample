-- Create the database
CREATE DATABASE PylonProductionData_ForTesting;
GO

-- Use the database
USE PylonProductionData_ForTesting;
GO

-- Create the schema if it does not exist
IF NOT EXISTS (SELECT schema_name
               FROM information_schema.schemata
               WHERE schema_name = 'test')
    BEGIN
        EXEC sp_executesql N'CREATE SCHEMA test';
    END;
GO

-- Create the SampleManpowerList table
CREATE TABLE [test].[SampleManpowerList]
(
    id          INT IDENTITY (1,1) PRIMARY KEY,
    nric4Digit  NVARCHAR(50) NOT NULL,
    name        NVARCHAR(50) NOT NULL,
    manpowerId  NVARCHAR(50) NOT NULL,
    designation NVARCHAR(50),
    project     NVARCHAR(50),
    team        NVARCHAR(50),
    supervisor  NVARCHAR(50),
    joinDate    DATE         NOT NULL,
    resignDate  DATE
);
GO