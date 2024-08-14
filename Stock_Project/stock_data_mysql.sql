create database stock;
use stock;

CREATE TABLE stock_data (
		Date DATE,
        Symbol VARCHAR(10),
        Series VARCHAR(5),
        Prev_Close FLOAT,
        Open FLOAT,
        High FLOAT,
        Low FLOAT,
        Last FLOAT,
        Close FLOAT,
        VWAP FLOAT,
        Volume BIGINT,
        Turnover DOUBLE,
        Trades INT,
        Deliverable_Volume BIGINT,
        Percent_Deliverable FLOAT
    );
select * from stock_data;