Selected = 
SWITCH(
    TRUE(),
    [Measure_Selected] = "YTD", 
        VAR MaxDate = MAX(DimDate[Date])
        VAR FiscalYearStart = DATE(YEAR(MaxDate) - IF(MONTH(MaxDate) < 4, 1, 0), 4, 1)
        RETURN
            IF(
                SELECTEDVALUE(DimDate[Date]) >= FiscalYearStart && SELECTEDVALUE(DimDate[Date]) <= TODAY(),
                "YTD",
                BLANK()
            ),
    [Measure_Selected] = "FTM", 
        VAR MaxDate_MTD = MAX(DimDate[Date])
        RETURN
            IF(
                MONTH(SELECTEDVALUE(DimDate[Date])) = MONTH(MaxDate_MTD) && YEAR(SELECTEDVALUE(DimDate[Date])) = YEAR(MaxDate_MTD),
                "FTM",
                BLANK()
            ),
    BLANK()
)
