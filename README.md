# hkdistrictcouncil2019
Hong Kong District Council 2019 Data and Web Scraper

The project includes a web scraper to consolidate the data of Hong Kong District Council 2019 to a single CSV file from several files.

## Statistics from Reference Websites and Sample Data

|Item|Count|Percentage|Remarks|
|-|-:|-:|-|
|No. of Registered Electors (Geographical Constituency) in 2019|[4,132,977](https://www.voterregistration.gov.hk/eng/statistic20191.html)|||
|No. of voter turnout|[2,943,842](https://www.elections.gov.hk/dc2019/eng/turnout.html)|71.23%||
|No. of valid votes to elected DC members (a)|1,678,119|||
|No. of valid votes to pro-Beijing DC members|171,737|10.23%|% of (a)|
|No. of valid votes to pro-Democracy DC members (b)|1,506,382|89.77%|% of (a)|
|No. of votes represented by active DC members (c)|646,156|38.50%|% of (a)|
|No. of votes represented by inactive DC members (d)|1,031,963|61.50%|% of (a)|
|No. of votes represented by active pro-Beijing DC members|171,737|26.58%|% of (c)|
|No. of votes represented by active pro-Democracy DC members|474,419|73.42%|% of (c)|
|No. of votes represented by active pro-Democracy DC members|474,419|31.49%|% of (b)|

Above statistics are for reference only, as of 2021/7/22.

Note (d): All inactive DC members are also from pro-Democracy camp.

## Sample Data

* [Hong Kong District Council 2019 Election (Basic) Data](https://github.com/sammyfung/hkdistrictcouncil2019/blob/main/sample-data/hkdistrictcouncil2019-election-sorted.csv) including district name & code, candidate/member name, candidate no., alias, affiliation, no. of votes, win/not win.
* [Hong Kong District Council 2019 Election Data with Advanced Data](https://github.com/sammyfung/hkdistrictcouncil2019/blob/main/sample-data/hkdistrictcouncil2019-election-sorted-advance.csv) from [Wikipedia](https://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E5%8D%80%E8%AD%B0%E6%9C%83) and etc, including all data from basic data file and additionally including active/Inactive member, political camps, status of inactive members, date of registration.

Above sample data are for reference only, as of 2021/7/22, please contribute if any data update or correction.

## Contribute

Please [create issues](https://github.com/sammyfung/hkdistrictcouncil2019/issues) on GitHub.

## LICENSE

Apache License 2.0 excluding the sample data.

