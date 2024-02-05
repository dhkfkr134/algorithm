-- year(date또는 datetime) :년도만 뜻함
SELECT BOOK_ID,date_format(PUBLISHED_DATE,'%Y-%m-%d') PUBLISHED_DATE
from BOOK
where YEAR(PUBLISHED_DATE)='2021' and CATEGORY='인문'
order by PUBLISHED_DATE ASC;
